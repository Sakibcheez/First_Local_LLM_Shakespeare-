# Building Your First Local LLM - Complete Guide

## Overview
You'll build a small language model using:
- **Framework**: Hugging Face Transformers
- **Model**: DistilGPT-2 (lightweight, perfect for beginners)
- **Dataset**: A small Shakespeare text dataset (~1MB)
- **Task**: Fine-tune the model on Shakespeare text, then generate predictions

## Step-by-Step Setup Instructions

### Step 1: Create Project Structure
```
my_llm/
├── data/
│   └── shakespeare.txt
├── models/
│   └── (fine-tuned model will be saved here)
├── requirements.txt
├── 1_setup.py           # Data download
├── 2_train.py           # Training script
├── 3_inference.py       # Generate text with your model
└── config.py            # Configuration file
```

### Step 2: Install Python & VS Code
1. Download Python 3.10+ from python.org
2. Download VS Code from code.visualstudio.com
3. Install Python extension in VS Code

### Step 3: Create Virtual Environment
```bash
cd D:\My Code\LLM
python -m venv venv
# On Windows:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run Scripts in Order
```bash
python 1_setup.py        # Download & prepare data
python fix_data.py 
python 2_train.py        # Fine-tune the model (5-10 mins)
python 3_inference.py    # Generate text with your trained model
```

## What Each Script Does

### `1_setup.py` - Downloads & prepares data
- Fetches Shakespeare dataset from Hugging Face
- Splits into train/validation
- Prepares tokenized format for training

### `2_train.py` - Fine-tunes the model
- Loads pre-trained DistilGPT-2
- Fine-tunes on Shakespeare data
- Saves the trained model locally

### `3_inference.py` - Generates text
- Loads your trained model
- Takes a prompt and generates continuations
- Interactive mode to test your LLM

## Expected Results
After training (~5-10 minutes):
```
Prompt: "To be or not to be"
Output: "To be or not to be, that is the question...
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune..."
```

## Key Concepts Explained Later in Code Comments
- Tokenization
- Embeddings
- Training loops
- Validation metrics
- Model saving/loading
