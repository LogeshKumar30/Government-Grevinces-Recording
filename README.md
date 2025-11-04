
# Government Grievance Recording Chatbot (Proof-of-Concept)

## 📘 Overview
The Government Grievance Recording Chatbot is an AI-driven system designed to simplify and digitize the process of citizen grievance reporting. Instead of relying on traditional paper-based or static web forms, this chatbot offers an **interactive, dialogue-based interface** to collect user details and grievances efficiently.  
The chatbot guides users through a structured conversation to record their **Name, Phone Number, Address**, and one or more **grievances**, validates the data in real-time, and securely stores it in a **SQLite database**. This proof-of-concept demonstrates how conversational AI can enhance public grievance redressal through accessibility, structured data handling, and automation.

---

## ⚙️ Features
- Interactive chatbot interface built with **Streamlit**
- Sequential data collection (Name, Phone, Address, Grievance)
- Input validation for accuracy (10-digit phone number check)
- Real-time error handling and user feedback
- Data stored in **SQLite** using **SQLAlchemy ORM**
- Confirmation summary after successful submission
- Modular Python structure for easy maintenance
- Optional integration with **LLM (Llama 3.3 via SambaNova)** for natural dialogue enhancement

---

## 🧩 Project Structure
Government-Grievance-Chatbot/
│
├── app.py                   # Main Streamlit application (frontend + chatbot flow)
│
├── db_init.py               # Database schema and initialization script
│
├── models.py                # Database operations using SQLAlchemy
│
├── utils.py                 # Input validation and helper functions
│
├── llm_integration.py       # Optional LLM (Llama 3.3) integration module
│
├── grievances.db            # SQLite database file (stores recorded grievances)
│
├── requirements.txt         # Python dependencies
│
├── .env.example             # Example environment configuration (API keys, DB path)
│
├── README.md                # Project documentation
│
└── sample_transcript.txt    # Example chatbot conversation transcript


**##🚀 Future Enhancements**

  1)Integration with government portals via REST APIs
  2)Admin dashboard for grievance management
  3)SMS/email notifications for grievance tracking
  4)Multi-language support using LLM translation features

**🗄️ Database Schema**

| Field Name     | Type     | Description                       |
| -------------- | -------- | --------------------------------- |
| id             | Integer  | Unique grievance ID (Primary Key) |
| name           | String   | User’s full name                  |
| phone_number   | String   | Validated 10-digit phone number   |
| address        | Text     | Residential address               |
| grievance_text | Text     | One or more grievances            |
| timestamp      | DateTime | Record creation time              |


🏁 Conclusion
  This project demonstrates a scalable and efficient way to record citizen grievances using conversational AI. The chatbot enhances user accessibility, data accuracy, and administrative transparency, paving the way for a future-ready citizen-centric governance system.

## 📬 Contact

For any queries, reach out to \[[logeshkumar974@gmail.com](mailto:logeshkumar974@gmail.com)] or connect on [LinkedIn](https://linkedin.com/in/logeshkumarp)


