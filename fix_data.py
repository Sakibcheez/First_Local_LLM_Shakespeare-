# fix_data.py
from datasets import load_dataset
import os

os.makedirs("data", exist_ok=True)

print("Downloading tiny_shakespeare from Hugging Face...")

try:
    # Method 1: Hugging Face dataset
    dataset = load_dataset("karpathy/tiny_shakespeare")
    full_text = dataset["train"][0]["text"]
    print(f"✅ Downloaded via Hugging Face")

except Exception as e:
    print(f"HuggingFace failed: {e}")
    print("Trying direct download...")

    # Method 2: Direct URL fallback
    import urllib.request
    url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
    urllib.request.urlretrieve(url, "data/full.txt")
    with open("data/full.txt", "r", encoding="utf-8") as f:
        full_text = f.read()
    print(f"✅ Downloaded via direct URL")

print(f"Total characters: {len(full_text):,}")

# Split 90% train, 10% validation
split = int(len(full_text) * 0.90)
train_text = full_text[:split]
val_text   = full_text[split:]

# Save
with open("data/train.txt", "w", encoding="utf-8") as f:
    f.write(train_text)

with open("data/validation.txt", "w", encoding="utf-8") as f:
    f.write(val_text)

print(f"\n✅ train.txt      → {len(train_text):,} characters")
print(f"✅ validation.txt → {len(val_text):,} characters")
print("\nNow run: python 2_train.py")