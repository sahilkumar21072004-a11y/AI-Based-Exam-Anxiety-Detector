# 🧠 AI-Based Exam Anxiety Detector

An intelligent mental-wellness support system that detects and categorizes exam-related anxiety using a fine-tuned BERT model.

---

## 🚀 Features

- Real-time anxiety prediction
- 3-level classification (Low, Moderate, High)
- FastAPI backend
- Streamlit frontend
- Deep Learning using BERT
- Swagger API documentation

---

## 🏗 Tech Stack

- Python
- PyTorch
- HuggingFace Transformers
- FastAPI
- Streamlit
- Uvicorn

---

## 📊 Model Architecture

- Pre-trained: `bert-base-uncased`
- Fine-tuned for 3-class classification
- Custom PyTorch training loop

---

## 📂 Project Structure
# 🧠 AI-Based Exam Anxiety Detector

An intelligent mental-wellness support system that detects and categorizes exam-related anxiety using a fine-tuned BERT model.

---

## 🚀 Features

- Real-time anxiety prediction
- 3-level classification (Low, Moderate, High)
- FastAPI backend
- Streamlit frontend
- Deep Learning using BERT
- Swagger API documentation

---

## 🏗 Tech Stack

- Python
- PyTorch
- HuggingFace Transformers
- FastAPI
- Streamlit
- Uvicorn

---

## 📊 Model Architecture

- Pre-trained: `bert-base-uncased`
- Fine-tuned for 3-class classification
- Custom PyTorch training loop

---

## 📂 Project Structure
AI-BASED-EXAM-ANXIETY-DETECTOR/
│
├── .venv/
├── venv/
│
├── anxiety_model/
│
├── backend/
│   ├── __pycache__/
│   ├── app.py
│   ├── main.py
│   └── train_model.py
│
├── data/
│   ├── anxiety_dataset.csv
│   └── cleaned_anxiety_dataset.csv
│
├── frontend/
│   └── app.py
│
├── model/
│   └── anxiety_model/
│       ├── config.json
│       ├── model.safetensors
│       ├── tokenizer_config.json
│       └── tokenizer.json
│
├── notebooks/
│   ├── 02_preprocessing.py
│   ├── eda.py
│   └── Milestone_4_BERT_Training.ipynb
│
├── utils/
│
├── AI(AI-Based Exam Anxiety Detector).docx
├── Suitability for Real.docx
├── README.md
└── requirements.txt

---

## ▶ Running Locally

### 1️⃣ Start Backend

```bash
cd backend
uvicorn main:app --reload
2️⃣ Start Frontend
cd frontend
streamlit run app.py
⚠ Disclaimer

This system is a supportive AI tool and not a medical diagnostic system.👨‍💻 Developed By

Sahil Kumar


🔥 Portfolio level ready.

---

# 🌐 4️⃣ DEPLOYMENT (Render – Easiest)

## Step 1:
Push project to GitHub.

## Step 2:
Go to:
https://render.com

## Step 3:
Create → Web Service

Connect GitHub repo.

---

### Render Settings:

Build Command:

pip install -r requirements.txt


Start Command:

uvicorn backend.main:app --host 0.0.0.0 --port 10000


Deploy.

You get public URL 🎉

---

# 🏆 FINAL RESULT

You now have:

✔ Full-stack AI system  
✔ Professional UI  
✔ API backend  
✔ Deployment ready  
✔ Portfolio ready  
✔ Resume worthy  
