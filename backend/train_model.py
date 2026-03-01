import os
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.model_selection import train_test_split
from torch.optim import AdamW

# Paths
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "cleaned_anxiety_dataset.csv")
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model", "anxiety_model")

# Hyperparameters
BATCH_SIZE = 8
MAX_LEN = 128
EPOCHS = 2
LEARNING_RATE = 2e-5

class AnxietyDataset(Dataset):
    def __init__(self, texts, labels, tokenizer):
        self.encodings = tokenizer(
            texts.tolist(),
            truncation=True,
            padding=True,
            max_length=MAX_LEN
        )
        self.labels = labels.tolist()

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)


def main():
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded dataset, shape {df.shape}")

    train_texts, val_texts, train_labels, val_labels = train_test_split(
        df["statement"],
        df["label"],
        test_size=0.2,
        random_state=42
    )

    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    train_dataset = AnxietyDataset(train_texts, train_labels, tokenizer)
    val_dataset = AnxietyDataset(val_texts, val_labels, tokenizer)

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = BertForSequenceClassification.from_pretrained(
        "bert-base-uncased", num_labels=3
    )
    model.to(device)

    optimizer = AdamW(model.parameters(), lr=LEARNING_RATE)

    model.train()
    for epoch in range(EPOCHS):
        print(f"\nEpoch {epoch+1}/{EPOCHS}")
        total_loss = 0
        for batch in train_loader:
            optimizer.zero_grad()
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)
            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels
            )
            loss = outputs.loss
            total_loss += loss.item()
            loss.backward()
            optimizer.step()
        print("Average loss:", total_loss / len(train_loader))

    # evaluate
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in val_loader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)
            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask
            )
            preds = torch.argmax(outputs.logits, dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    acc = correct / total
    print("Validation accuracy:", acc)

    os.makedirs(MODEL_DIR, exist_ok=True)
    model.save_pretrained(MODEL_DIR)
    tokenizer.save_pretrained(MODEL_DIR)
    print("Model saved to", MODEL_DIR)

if __name__ == "__main__":
    main()
