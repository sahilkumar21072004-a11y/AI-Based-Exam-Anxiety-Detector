from fastapi import FastAPI
from pydantic import BaseModel
import torch
import os
from transformers import BertTokenizer, BertForSequenceClassification

app = FastAPI()

# Load model from local directory
model_dir = os.path.join(os.path.dirname(__file__), "..", "model", "anxiety_model")
tokenizer = BertTokenizer.from_pretrained(model_dir)
model = BertForSequenceClassification.from_pretrained(model_dir)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

print("Model loaded successfully.")

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_anxiety(data: TextInput):
    inputs = tokenizer(
        data.text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )
    
    inputs = {key: value.to(device) for key, value in inputs.items()}
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    prediction = torch.argmax(outputs.logits, dim=1).item()
    
    label_map = {
        0: "Low Anxiety",
        1: "Moderate Anxiety",
        2: "High Anxiety"
    }
    
    anxiety_level = label_map[prediction]
    return {
        "input_text": data.text,
        "predicted_anxiety_level": anxiety_level,
        "anxiety_level": anxiety_level  # legacy key for frontend compatibility
    }