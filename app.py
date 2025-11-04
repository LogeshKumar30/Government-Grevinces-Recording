import streamlit as st
import re
from database import setup_database, insert_grievance
from llm_integration import get_llm_response, paraphrase_and_summarize

# --- Page Configuration ---
st.set_page_config(page_title="Grievance Chatbot", page_icon="✍️")
st.title("✍️ Government Grievance Chatbot")

# --- Database Setup ---
setup_database()

# --- Session State Initialization (N1: Coherence) ---
if "stage" not in st.session_state:
    st.session_state.stage = "GREETING"
    st.session_state.user_data = {}
    st.session_state.messages = []
    # F1: Initial greeting
    initial_prompt = get_llm_response("GREETING")
    st.session_state.messages.append({"role": "assistant", "content": initial_prompt})

# --- Chat History Display ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Main Chat Logic (F1: Flow, F2: Validation) ---
if prompt := st.chat_input("Your response..."):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Conversation State Machine ---
    current_stage = st.session_state.stage
    bot_response = None

    try:
        if current_stage == "GREETING":
            # F1: Collect Name
            st.session_state.user_data["name"] = prompt
            bot_response = get_llm_response("ASK_PHONE", user_input=prompt)
            st.session_state.stage = "ASK_PHONE"

        elif current_stage == "ASK_PHONE":
            # F1 & F2: Collect and Validate Phone
            if re.match(r"^\d{10}$", prompt):
                st.session_state.user_data["phone"] = prompt
                bot_response = get_llm_response("ASK_ADDRESS")
                st.session_state.stage = "ASK_ADDRESS"
            else:
                # F2: Error Handling
                bot_response = get_llm_response("ASK_PHONE_RETRY")
                st.session_state.stage = "ASK_PHONE" # Stay in this stage

        elif current_stage == "ASK_ADDRESS":
            # F1: Collect Address
            st.session_state.user_data["address"] = prompt
            bot_response = get_llm_response("ASK_GRIEVANCE")
            st.session_state.stage = "ASK_GRIEVANCE"

        elif current_stage == "ASK_GRIEVANCE":
            # F1: Collect Grievance
            st.session_state.user_data["grievance"] = prompt
            
            # F4: Use LLM to summarize
            summary, _ = paraphrase_and_summarize(st.session_state.user_data)
            
            # F3: Database Integration
            grievance_id = insert_grievance(
                st.session_state.user_data["name"],
                st.session_state.user_data["phone"],
                st.session_state.user_data["address"],
                st.session_state.user_data["grievance"]
            )
            
            if grievance_id:
                # F1: Confirmation Message
                confirmation_msg = f"**Your grievance has been successfully recorded.**\n\nYour Reference ID is: **{grievance_id}**\n\n{summary}"
                bot_response = confirmation_msg + "\n\n" + get_llm_response("GOODBYE")
                st.session_state.stage = "DONE"
            else:
                bot_response = "I'm sorry, there was an error saving your grievance to the database. Please try again later."
                st.session_state.stage = "ERROR"

        elif current_stage == "DONE" or current_stage == "ERROR":
            bot_response = "This conversation has ended. Please refresh the page to start a new grievance."

    except Exception as e:
        bot_response = f"An unexpected error occurred: {e}. Please refresh and try again."
        st.session_state.stage = "ERROR"

    # Display bot response
    if bot_response:
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant"):
            st.markdown(bot_response)