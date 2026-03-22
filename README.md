# 🚀 My First Local LLM - Shakespeare Text Generator

A complete beginner-friendly guide to building, training, and using your own language model locally using PyTorch and Hugging Face Transformers.

## Overview

This project teaches you how to:
- ✅ Download and prepare text data
- ✅ Fine-tune a pre-trained model (DistilGPT-2)
- ✅ Train on your local machine (CPU or GPU)
- ✅ Generate creative text using your trained model
- ✅ Understand how LLMs work at every step

**Dataset**: Shakespeare (~600KB of timeless literature)
**Model**: DistilGPT-2 (82M parameters, lightweight)
**Time**: 5-10 minutes to train on CPU

---

## 📁 Project Structure

```
my_llm/
├── data/                    # (Generated after setup)
│   ├── shakespeare.txt      # Raw dataset
│   ├── train.txt           # 90% for training
│   └── validation.txt      # 10% for testing
├── models/                 # (Generated after training)
│   ├── best_model/         # Best checkpoint
│   └── final_model/        # Final trained model
├── config.py              # Settings you can customize
├── 1_setup.py            # Download & prepare data
├── 2_train.py            # Train the model
├── 3_inference.py        # Generate text interactively
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── README.md            # This file
└── docs/
    ├── QUICK_START.md           # 5-minute quick start
    ├── SETUP_GUIDE.md           # Detailed setup
    ├── COMPLETE_EXPLANATION.md  # Deep dive explanations
    └── VISUAL_REFERENCE.md      # Architecture diagrams
```

---

## 🚀 Quick Start (5 Minutes)

### 1. Clone and Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/my-llm.git
cd my-llm

# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Three Steps

```bash
# Step 1: Download and prepare data (~10 seconds)
python 1_setup.py

# Step 2: Train the model (~5-10 minutes on CPU)
python 2_train.py

# Step 3: Generate text (interactive!)
python 3_inference.py
```

### 3. Try These Prompts

```
"To be or not to be"
"The quality of mercy"
"All the world's a stage"
"Had I but world enough and time"
```

---

## 📚 Documentation

This project includes extensive documentation:

| Document | Purpose |
|----------|---------|
| **QUICK_START.md** | 5-minute overview of how to run everything |
| **SETUP_GUIDE.md** | Step-by-step installation and setup instructions |
| **COMPLETE_EXPLANATION.md** | Deep-dive into LLMs, transformers, and all code |
| **VISUAL_REFERENCE.md** | Architecture diagrams and visual explanations |

Start with `QUICK_START.md`, then read `COMPLETE_EXPLANATION.md` to understand how everything works!

---

## 🎯 What You'll Learn

### Concepts
- **Tokenization**: How text becomes numbers
- **Embeddings**: Representing words as vectors
- **Transformers**: The architecture behind modern LLMs
- **Attention**: How models understand context
- **Training loops**: Forward pass, loss calculation, backpropagation
- **Inference**: Auto-regressive text generation

### Practical Skills
- Loading pre-trained models from Hugging Face
- Fine-tuning models on custom data
- Training on CPU and GPU
- Generating text with different temperature settings
- Evaluating model performance

### Code Understanding
- **1_setup.py**: Data preparation and tokenization
- **2_train.py**: Complete training pipeline with validation
- **3_inference.py**: Interactive text generation

---

## ⚙️ Configuration

Edit `config.py` to customize behavior:

```python
# Model
MODEL_NAME = "distilgpt2"  # Lightweight, CPU-friendly

# Training (adjust these!)
BATCH_SIZE = 4                # Lower = slower but stable
LEARNING_RATE = 5e-5          # Standard for fine-tuning
NUM_EPOCHS = 3                # More = better (but slower)
MAX_SEQ_LENGTH = 128          # Context window size

# Inference
TEMPERATURE = 0.7             # 0.3-0.5 = predictable, 0.7+ = creative
MAX_NEW_TOKENS = 100          # Length of generated text
```

### Customize Training

**For Better Quality (Slower)**:
```python
BATCH_SIZE = 2
NUM_EPOCHS = 5
LEARNING_RATE = 1e-5
```

**For Faster Training (Lower Quality)**:
```python
BATCH_SIZE = 8
NUM_EPOCHS = 1
MAX_SEQ_LENGTH = 64
```

**For More Creative Output**:
```python
TEMPERATURE = 1.2  # In 3_inference.py
```

---

## 📊 What Happens At Each Step

### Step 1: Data Preparation (`1_setup.py`)
- Downloads Shakespeare dataset from Hugging Face
- Tokenizes text (converts to numbers)
- Splits into 90% training, 10% validation
- **Output**: `data/train.txt` and `data/validation.txt`

### Step 2: Training (`2_train.py`)
- Loads pre-trained DistilGPT-2 model
- Fine-tunes on Shakespeare data for 3 epochs
- Monitors loss (should decrease)
- Saves best model checkpoint
- **Output**: `models/best_model/` and `models/final_model/`

### Step 3: Inference (`3_inference.py`)
- Loads trained model
- Takes your prompt
- Generates 100 tokens using auto-regressive sampling
- **Interactive**: Keep entering prompts until you quit

---

## 🔧 System Requirements

| Component | Requirement | Notes |
|-----------|------------|-------|
| **Python** | 3.8+ | 3.10+ recommended |
| **RAM** | 4 GB+ | 8 GB+ recommended |
| **Storage** | 2 GB | For venv + dependencies |
| **Disk (Training)** | 500 MB | temp files |
| **GPU** | Optional | CPU works fine (just slower) |

### GPU Support (Optional)

If you have an NVIDIA GPU:

```bash
# Install GPU version of PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Update config.py
DEVICE = "cuda"  # Instead of "cpu"
```

**GPU Training Speed**: ~2 minutes vs 10 minutes on CPU

---

## 📈 Expected Results

### After Step 1
```
✅ Dataset downloaded: 600 KB
✅ Total characters: 123,456
✅ Train/Val split: 90/10
```

### After Step 2
```
📅 Epoch 1/3
   Train Loss: 3.2145 | Val Loss: 3.1234
📅 Epoch 2/3
   Train Loss: 2.8934 | Val Loss: 2.7821
📅 Epoch 3/3
   Train Loss: 2.5643 | Val Loss: 2.4876
✅ Models saved to ./models/
```

### After Step 3
```
📝 Enter prompt: To be or not to be
Generated: "To be or not to be that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune..."
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: torch` | Run `pip install -r requirements.txt` |
| `CUDA out of memory` | Set `BATCH_SIZE = 2` in `config.py` |
| Generation is gibberish | Lower temperature: `TEMPERATURE = 0.5` |
| Model not found | Run `python 2_train.py` first |
| Windows: venv won't activate | Run PowerShell as admin first |
| Slow training | Use GPU if available; reduce `MAX_SEQ_LENGTH` |

---

## 📚 Learning Resources

- **Hugging Face Course**: https://huggingface.co/course
- **Attention is All You Need**: https://arxiv.org/abs/1706.03762
- **Language Models are Unsupervised**: https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf
- **Transformers Docs**: https://huggingface.co/docs/transformers

---

## 🎓 How This Relates to ChatGPT

| Aspect | Our Model | ChatGPT |
|--------|-----------|---------|
| **Parameters** | 82 million | 175 billion |
| **Training Data** | 600 KB Shakespeare | 300 billion tokens (all of internet) |
| **Training Time** | 10 minutes | Months on clusters |
| **Capability** | Mimics Shakespeare | Solves any problem |
| **Inference Speed** | 1-2 sec/100 tokens | Real-time |

**Key Insight**: Same architecture, just scaled up! Bigger data + bigger model = better results.

---

## 💡 Next Steps

1. ✅ Train on your own text (replace Shakespeare with your data)
2. ✅ Use a larger model (`gpt2` instead of `distilgpt2`)
3. ✅ Train longer (increase `NUM_EPOCHS`)
4. ✅ Use more data (combine multiple datasets)
5. ✅ Experiment with temperature and sampling
6. ✅ Deploy as a web service with FastAPI

---

## 📝 License

MIT License - feel free to use this for learning!

---

## 🤝 Contributing

Want to improve this project?
1. Fork it
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ❓ Questions?

Check the documentation files:
- Quick questions → `QUICK_START.md`
- Setup issues → `SETUP_GUIDE.md`
- How does it work? → `COMPLETE_EXPLANATION.md`
- Architecture deep-dive → `VISUAL_REFERENCE.md`

---

## 🎉 Congratulations!

You've just learned how to:
- ✅ Build an LLM from scratch
- ✅ Understand transformer architecture
- ✅ Fine-tune pre-trained models
- ✅ Generate creative text

This is the foundation for understanding ChatGPT, Claude, and all modern LLMs! 🚀

---

**Happy learning!** 📚
