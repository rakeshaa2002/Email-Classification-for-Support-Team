# 📧 Email Classification for Support Team

This project is designed to automatically classify incoming support emails into predefined categories such as Billing Issues, Technical Support, and Account Management. It also masks any Personally Identifiable Information (PII) before classification and provides the original data back after processing.

---

## 🚀 Features

- ✅ PII Detection and Masking (Full Name, Email, Phone, Aadhar, Card Info, etc.)
- ✅ Email Classification using Machine Learning (Random Forest)
- ✅ REST API built with FastAPI
- ✅ Compliant with strict JSON format for evaluation
- ✅ Deployable on Hugging Face Spaces

---

## 📂 Project Structure


---

## 🧠 How It Works

1. Input email is passed to the API
2. All PII is masked using regex-based methods
3. Masked email is classified into a support category using a trained ML model
4. API returns:
   - Original email
   - List of masked entities with positions and types
   - Masked email
   - Predicted category

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/rakeshaa2002/Email-Classification-for-Support-Team.git
cd Email-Classification-for-Support-Team

python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
python models.py
uvicorn app:app --reload

##POST /classify
Request JSON:

{
  "input_email_body": "...",
  "list_of_masked_entities": [
    {
      "position": [start_index, end_index],
      "classification": "entity_type",
      "entity": "original_value"
    }
  ],
  "masked_email": "...",
  "category_of_the_email": "..."
}

Rakesha N

GitHub: @rakeshaa2002

