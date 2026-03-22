# 🚀 QUICK START GUIDE - Your First LLM in 5 Minutes

## Prerequisites
- Python 3.8+ installed
- VS Code installed

## Step 1: Setup Environment (2 minutes)

Open terminal in VS Code and run:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

You should see `(venv)` at the start of your terminal line when active.

---

## Step 2: Prepare Data (1 minute)

```bash
python 1_setup.py
```

This will:
- ✅ Download Shakespeare data automatically from Hugging Face
- ✅ Split into train/validation sets
- ✅ Show you dataset statistics

**Example output:**
```
📊 Dataset Statistics:
   File size: 120.3 KB
   Total characters: 123,456
   Total words: 23,456
   Lines: 2,456
```

---

## Step 3: Train Your Model (5-10 minutes)

```bash
python 2_train.py
```

This will:
- 🤖 Load pre-trained DistilGPT-2 model
- 🔥 Fine-tune it on Shakespeare data (3 epochs)
- 📊 Show training progress
- 💾 Save the best model

**Example output:**
```
📅 Epoch 1/3
Training: 100%|████████| 123/123 [02:34<00:00, 0.79/s]
   Train Loss: 3.2145 | Val Loss: 3.1234
   💾 Best model saved!

📅 Epoch 2/3
...
✓ Training Complete!
💾 Models saved to: ./models/
```

---

## Step 4: Generate Text (Interactive!)

```bash
python 3_inference.py
```

This launches an interactive generator:

```
📝 Enter prompt: To be or not to be
⏳ Generating text...

────────────────────────────────────────────
Generated text:
────────────────────────────────────────────
To be or not to be that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
────────────────────────────────────────────

📝 Enter prompt: _
```

**Try these prompts:**
```
"To be or not to be"
"The quality of mercy"
"All the world's a stage"
"Friends, Romans, countrymen"
```

Type `quit` to exit.

---

## 📂 Project Structure After Setup

```
my_llm/
├── data/
│   ├── shakespeare.txt
│   ├── train.txt
│   └── validation.txt
├── models/
│   ├── best_model/
│   │   ├── pytorch_model.bin
│   │   └── config.json
│   └── final_model/
│       ├── pytorch_model.bin
│       └── config.json
├── config.py
├── 1_setup.py
├── 2_train.py
├── 3_inference.py
└── requirements.txt
```

---

## 🎯 What Happens at Each Step

### Step 1_setup.py
**Input:** Empty data/ folder
**Output:** Shakespeare dataset split into train/validation
**Time:** ~10 seconds

### Step 2_train.py
**Input:** Text files
**Process:**
- Tokenize text (convert to numbers)
- Train for 3 epochs
- Validate after each epoch
- Save best model

**Output:** Trained model files
**Time:** ~10 minutes on CPU, ~2 minutes on GPU

### Step 3_inference.py
**Input:** Your prompts
**Output:** Generated Shakespeare-style text
**Time:** 1-2 seconds per generation

---

## ⚡ Optional: Customize Training

Edit `config.py` to change behavior:

```python
# Make training faster (but lower quality)
NUM_EPOCHS = 1
BATCH_SIZE = 4

# Make training slower (but higher quality)
NUM_EPOCHS = 10
BATCH_SIZE = 16

# Control generation creativity
TEMPERATURE = 0.5  # More predictable
TEMPERATURE = 1.0  # Balanced
TEMPERATURE = 1.5  # More creative
```

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: torch` | Run `pip install -r requirements.txt` |
| Training is slow | Use CPU (already optimized) |
| Generation is gibberish | Set `TEMPERATURE = 0.5` in config.py |
| Model not found | Run `python 2_train.py` first |

---

## 📚 Files in This Project

| File | Purpose |
|------|---------|
| `config.py` | Settings you can change |
| `1_setup.py` | Download & prepare data |
| `2_train.py` | Train the model |
| `3_inference.py` | Generate text |
| `COMPLETE_EXPLANATION.md` | Detailed explanation |
| `SETUP_GUIDE.md` | Setup instructions |
| `QUICK_START.md` | This file! |

---

## 🎓 Next: Read the Detailed Explanation

After running all three scripts, open and read:

**`COMPLETE_EXPLANATION.md`**

It explains:
- ✅ What is an LLM?
- ✅ How tokenization works
- ✅ What embeddings and transformers are
- ✅ Complete code walkthrough
- ✅ How to improve your model
- ✅ Key concepts explained simply

---

## 💾 Save Your Progress

After training completes, you can:

1. **Keep your trained model** for future inference
2. **Modify the data** to train on different text
3. **Adjust hyperparameters** in config.py and retrain
4. **Share with friends** - send them the `models/` folder

---

## 🚀 That's It!

You now have a working LLM that:
- Learned from 600KB of Shakespeare
- Generates creative text
- Runs entirely on your computer
- Shows you how massive models like ChatGPT work

**Congratulations!** 🎉

Next up: Modify the code, use different datasets, or scale it up!

---

## Quick Reference

```bash
# Activate environment
venv\Scripts\activate

# Run all steps
python 1_setup.py
python 2_train.py
python 3_inference.py

# Deactivate when done
deactivate
```

Good luck! 🚀
