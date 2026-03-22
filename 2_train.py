"""
STEP 2: Train your LLM
This script fine-tunes a pre-trained model on your Shakespeare data.

Key Concepts:
- Tokenization: Converting text to numbers the model understands
- Forward pass: Data through the model
- Loss calculation: How wrong the model is
- Backward pass: Updating weights to reduce loss
- Validation: Testing on unseen data to avoid overfitting
"""

import os
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from torch.optim import AdamW
from tqdm import tqdm
from config import (
    MODEL_NAME, BATCH_SIZE, LEARNING_RATE, NUM_EPOCHS,
    MAX_SEQ_LENGTH, MODEL_DIR, DATA_DIR, DEVICE
)

print("=" * 60)
print("STEP 2: TRAINING YOUR LLM")
print("=" * 60)

# Create model directory
os.makedirs(MODEL_DIR, exist_ok=True)

# Check device availability
if torch.cuda.is_available():
    device = "cuda"
    print(f"\n🚀 GPU detected! Using CUDA for faster training")
else:
    device = "cpu"
    print(f"\n💻 Using CPU for training (slower, but works fine for small models)")

print(f"   Device: {device}")

# ==================== 1. LOAD TOKENIZER ====================
print(f"\n📚 Loading tokenizer...")
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)
# Add padding token (important for batch processing)
tokenizer.pad_token = tokenizer.eos_token
print(f"✅ Tokenizer loaded with vocabulary size: {len(tokenizer)}")

# ==================== 2. PREPARE DATASET ====================
class TextDataset(Dataset):
    """
    Custom dataset class that:
    1. Reads raw text
    2. Tokenizes it
    3. Creates sequences of fixed length
    """

    def __init__(self, file_path, tokenizer, max_length=MAX_SEQ_LENGTH):
        print(f"\n📖 Loading text from: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            self.text = f.read()

        print(f"   Text loaded: {len(self.text):,} characters")

        # Tokenize the entire text
        # token_ids: [101, 2054, 2003, 1996, ...] (numbers representing words)
        print(f"📝 Tokenizing text...")
        self.encodings = tokenizer(
            self.text,
            return_tensors=None,  # Return as lists, not tensors
            padding=False,
            truncation=False,
        )

        print(f"   Tokenization complete: {len(self.encodings['input_ids']):,} tokens")

        self.max_length = max_length
        self.tokenizer = tokenizer

    def __len__(self):
        # How many sequences we can create
        return len(self.encodings['input_ids']) - self.max_length

    def __getitem__(self, idx):
        # Get a sequence starting at position idx
        input_ids = self.encodings['input_ids'][idx:idx + self.max_length]
        attention_mask = [1] * len(input_ids)

        # Pad to max_length if needed
        if len(input_ids) < self.max_length:
            pad_length = self.max_length - len(input_ids)
            input_ids += [self.tokenizer.eos_token_id] * pad_length
            attention_mask += [0] * pad_length

        return {
            'input_ids': torch.tensor(input_ids, dtype=torch.long),
            'attention_mask': torch.tensor(attention_mask, dtype=torch.long),
            'labels': torch.tensor(input_ids, dtype=torch.long)  # Same as input for language modeling
        }

# Load datasets
train_dataset = TextDataset(
    os.path.join(DATA_DIR, 'train.txt'),
    tokenizer,
    max_length=MAX_SEQ_LENGTH
)

val_dataset = TextDataset(
    os.path.join(DATA_DIR, 'validation.txt'),
    tokenizer,
    max_length=MAX_SEQ_LENGTH
)

# Create data loaders (batching and shuffling)
train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,  # Randomize order for better learning
    drop_last=True  # Remove last incomplete batch
)

val_loader = DataLoader(
    val_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)

print(f"\n✅ Data prepared:")
print(f"   Training sequences: {len(train_dataset)}")
print(f"   Validation sequences: {len(val_dataset)}")
print(f"   Batches per epoch: {len(train_loader)}")

# ==================== 3. LOAD MODEL ====================
print(f"\n🤖 Loading pre-trained model: {MODEL_NAME}")
model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
model.to(device)
print(f"✅ Model loaded and moved to {device}")
print(f"   Total parameters: {sum(p.numel() for p in model.parameters()):,}")

# ==================== 4. SETUP TRAINING ====================
optimizer = AdamW(model.parameters(), lr=LEARNING_RATE)

print(f"\n⚙️  Training configuration:")
print(f"   Learning rate: {LEARNING_RATE}")
print(f"   Batch size: {BATCH_SIZE}")
print(f"   Epochs: {NUM_EPOCHS}")
print(f"   Max sequence length: {MAX_SEQ_LENGTH}")

# ==================== 5. TRAINING LOOP ====================
print(f"\n{'=' * 60}")
print("🔥 STARTING TRAINING")
print(f"{'=' * 60}")

best_val_loss = float('inf')

for epoch in range(NUM_EPOCHS):
    print(f"\n📅 Epoch {epoch + 1}/{NUM_EPOCHS}")

    # -------- TRAINING --------
    model.train()  # Enable training mode (dropout, batch norm, etc.)
    train_loss = 0

    progress_bar = tqdm(train_loader, desc="Training", unit="batch")
    for batch_idx, batch in enumerate(progress_bar):
        # Move batch to device
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)

        # Forward pass: get predictions
        # The model outputs the probability of the next token
        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels
        )
        loss = outputs.loss

        # Backward pass: calculate gradients
        optimizer.zero_grad()  # Clear previous gradients
        loss.backward()         # Calculate new gradients
        optimizer.step()        # Update weights

        train_loss += loss.item()
        avg_loss = train_loss / (batch_idx + 1)
        progress_bar.set_postfix({'loss': f'{avg_loss:.4f}'})

    train_loss = train_loss / len(train_loader)

    # -------- VALIDATION --------
    model.eval()  # Disable training mode
    val_loss = 0

    with torch.no_grad():  # Don't calculate gradients during validation
        progress_bar = tqdm(val_loader, desc="Validating", unit="batch")
        for batch in progress_bar:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels
            )
            val_loss += outputs.loss.item()

    val_loss = val_loss / len(val_loader)

    # Print epoch summary
    print(f"   Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f}")

    # Save best model
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        save_path = os.path.join(MODEL_DIR, f"best_model")
        model.save_pretrained(save_path)
        tokenizer.save_pretrained(save_path)
        print(f"   💾 Best model saved! (val_loss: {val_loss:.4f})")

# ==================== 6. FINAL SAVE ====================
print(f"\n{'=' * 60}")
print("✓ Training Complete!")
print(f"{'=' * 60}")

# Save final model
final_path = os.path.join(MODEL_DIR, "final_model")
model.save_pretrained(final_path)
tokenizer.save_pretrained(final_path)

print(f"\n💾 Models saved to:")
print(f"   - Best model: {os.path.join(MODEL_DIR, 'best_model')}")
print(f"   - Final model: {final_path}")
print(f"\n📊 Final Results:")
print(f"   Best validation loss: {best_val_loss:.4f}")
print(f"   Final training loss: {train_loss:.4f}")
print(f"\nNext: Run python 3_inference.py to test your model!")
