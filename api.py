from fastapi import FastAPI, Request
from pydantic import BaseModel
from utils import mask_pii
import pickle

app = FastAPI()

# Load model and vectorizer
with open("classifier.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

class EmailInput(BaseModel):
    email_body: str

@app.post("/classify")
async def classify_email(email_input: EmailInput):
    original_text = email_input.email_body
    masked_text, entities = mask_pii(original_text)

    X = vectorizer.transform([masked_text])
    category = model.predict(X)[0]

    return {
        "input_email_body": original_text,
        "list_of_masked_entities": entities,
        "masked_email": masked_text,
        "category_of_the_email": category
    }
