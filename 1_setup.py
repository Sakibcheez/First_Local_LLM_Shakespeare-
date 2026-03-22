"""
STEP 1: Download and prepare your dataset
This script fetches the Shakespeare dataset from Hugging Face
and prepares it for training.
"""

import os
import urllib.request
from config import DATA_DIR, DATA_URL, TRAIN_TEST_SPLIT

print("=" * 60)
print("STEP 1: SETTING UP DATA")
print("=" * 60)

# Create data directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

# Download Shakespeare dataset
data_path = os.path.join(DATA_DIR, "shakespeare.txt")

if not os.path.exists(data_path):
    print(f"\n📥 Downloading Shakespeare dataset from Hugging Face...")
    print(f"   Source: {DATA_URL}")
    try:
        urllib.request.urlretrieve(DATA_URL, data_path)
        print(f"✅ Download complete! Saved to: {data_path}")
    except Exception as e:
        print(f"❌ Download failed. Using sample data instead.")
        print(f"Error: {e}")
        # Create sample data as fallback
        sample_text = """To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause—there's the respect
That makes calamity of so long life."""
        with open(data_path, 'w', encoding='utf-8') as f:
            f.write(sample_text)
        print(f"✅ Sample data created!")
else:
    print(f"\n✅ Data already exists at: {data_path}")

# Check file size and content
if os.path.exists(data_path):
    file_size = os.path.getsize(data_path) / 1024  # Convert to KB
    with open(data_path, 'r', encoding='utf-8') as f:
        text = f.read()

    print(f"\n📊 Dataset Statistics:")
    print(f"   File size: {file_size:.1f} KB")
    print(f"   Total characters: {len(text):,}")
    print(f"   Total words: {len(text.split()):,}")
    print(f"   Lines: {len(text.splitlines()):,}")
    print(f"\n📝 First 200 characters:")
    print(f"   {text[:200]}...")

# Split into train and validation
train_size = int(len(text) * TRAIN_TEST_SPLIT)
train_text = text[:train_size]
val_text = text[train_size:]

# Save splits
train_path = os.path.join(DATA_DIR, "train.txt")
val_path = os.path.join(DATA_DIR, "validation.txt")

with open(train_path, 'w', encoding='utf-8') as f:
    f.write(train_text)

with open(val_path, 'w', encoding='utf-8') as f:
    f.write(val_text)

print(f"\n✅ Data split into:")
print(f"   Training set: {len(train_text):,} characters ({train_size/len(text)*100:.1f}%)")
print(f"   Validation set: {len(val_text):,} characters ({(1-train_size/len(text))*100:.1f}%)")

print(f"\n{'=' * 60}")
print("✓ Step 1 Complete! Your data is ready.")
print("  Next: Run python 2_train.py")
print(f"{'=' * 60}\n")
