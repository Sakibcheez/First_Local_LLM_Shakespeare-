# 📊 Visual Reference & Architecture

## Full Pipeline Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                    YOUR LLM TRAINING PIPELINE                     │
└──────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: DATA PREPARATION (1_setup.py)                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Download Shakespeare Dataset                                   │
│  (from Hugging Face)                                            │
│         ↓                                                         │
│  ┌────────────────────┐                                          │
│  │ shakespeare.txt    │ (600 KB)                                │
│  │ "To be or not..."  │                                         │
│  └────────────────────┘                                          │
│         ↓                                                         │
│  Tokenization                                                   │
│  "To be or" → [T, o, Ġb, e, ...]                              │
│         ↓                                                         │
│  ┌─────────────────────────────────────────┐                    │
│  │ Train/Validation Split (90/10)          │                    │
│  │ train.txt (540KB)   validation.txt (60KB)                   │
│  └─────────────────────────────────────────┘                    │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘

                              ↓

┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: TRAINING (2_train.py)                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Load Pre-trained Model (DistilGPT-2)                           │
│  ┌──────────────────────────────────────┐                       │
│  │ Pre-trained on 40GB of English text  │                       │
│  │ Parameters: 82 million               │                       │
│  │ Vocab: 50,257 tokens                 │                       │
│  └──────────────────────────────────────┘                       │
│         ↓                                                         │
│  For Each Epoch (3 times):                                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ EPOCH 1/3                                                │   │
│  │                                                          │   │
│  │ Forward Pass:                                            │   │
│  │ Text → Tokenize → Embed → Transformer → Logits         │   │
│  │                                       ↓                 │   │
│  │ "To be or" → [284, 572, 393] → Hidden States → Pred   │   │
│  │                                       ↓                 │   │
│  │ Calculate Loss: |Predicted - Actual| = 3.45            │   │
│  │                                       ↓                 │   │
│  │ Backward Pass:                                          │   │
│  │ Calculate Gradients → Update Weights                   │   │
│  │ (18 million parameters updated per batch)              │   │
│  │                                                          │   │
│  │ Loss: 3.45 → 3.32 → 3.18 → ... (decreasing)           │   │
│  │                                                          │   │
│  │ After Epoch: Validate on 60KB test data                │   │
│  │ Validation Loss: 3.12                                   │   │
│  │ 💾 Save Best Model                                      │   │
│  └──────────────────────────────────────────────────────────┘   │
│         ↓                                                         │
│  ┌──────────────────────────────────────┐                       │
│  │ EPOCH 2/3 & 3/3 (same process)       │                       │
│  │ Final Loss: 2.87                     │                       │
│  └──────────────────────────────────────┘                       │
│         ↓                                                         │
│  ┌──────────────────────────────────────┐                       │
│  │ Trained Model Saved                  │                       │
│  │ ├── pytorch_model.bin (330 MB)       │                       │
│  │ ├── config.json                      │                       │
│  │ └── tokenizer_config.json            │                       │
│  └──────────────────────────────────────┘                       │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘

                              ↓

┌─────────────────────────────────────────────────────────────────┐
│ PHASE 3: INFERENCE (3_inference.py)                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Load Trained Model                                             │
│         ↓                                                         │
│  User Input: "To be or not to be"                              │
│         ↓                                                         │
│  ┌──────────────────────────────────────────┐                   │
│  │ GENERATION LOOP (100 iterations)         │                   │
│  │                                          │                   │
│  │ Iteration 1:                             │                   │
│  │ Context: [To, be, or, not, to, be]      │                   │
│  │ Model: "Next token?"                     │                   │
│  │ Output: "that" (probability: 0.92)       │                   │
│  │                                          │                   │
│  │ Iteration 2:                             │                   │
│  │ Context: [To, be, or, not, to, be, that]│                   │
│  │ Model: "Next token?"                     │                   │
│  │ Output: "is" (probability: 0.88)         │                   │
│  │                                          │                   │
│  │ ... (98 more iterations)                 │                   │
│  │                                          │                   │
│  │ Final tokens: 100                        │                   │
│  └──────────────────────────────────────────┘                   │
│         ↓                                                         │
│  Decode Tokens Back to Text                                     │
│  [284, 572, ..., 103] → "To be or not to be..."               │
│         ↓                                                         │
│  Output to User                                                 │
│  ┌────────────────────────────────────────────────┐             │
│  │ Generated: "To be or not to be that is the    │             │
│  │ question: Whether 'tis nobler in the mind to  │             │
│  │ suffer The slings and arrows of outrageous..."│             │
│  └────────────────────────────────────────────────┘             │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Transformer Architecture (Simplified)

```
Input Text: "To be or not"
      ↓
┌─────────────────────────────────────┐
│ TOKENIZATION LAYER                  │
│ "To be or not" → [T, o, Ġb, e, ...]│
└─────────────────────────────────────┘
      ↓
┌─────────────────────────────────────┐
│ EMBEDDING LAYER                     │
│ Each token becomes a 768-d vector   │
│ [0.2, -0.5, 0.1, ..., 0.3]          │
└─────────────────────────────────────┘
      ↓
┌─────────────────────────────────────┐
│ TRANSFORMER BLOCKS (12 times)       │  (DistilGPT-2 has 6)
│ ┌─────────────────────────────────┐ │
│ │ Attention Layer                 │ │
│ │ "Which tokens matter most?"     │ │
│ │ - "To" attends to grammar      │ │
│ │ - "be" attends to verbs        │ │
│ └─────────────────────────────────┘ │
│           ↓                         │
│ ┌─────────────────────────────────┐ │
│ │ Feed-Forward Network            │ │
│ │ Process & combine information   │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
      ↓
┌─────────────────────────────────────┐
│ OUTPUT LAYER                        │
│ Predict probability of next word    │
│ {                                   │
│   "that": 0.92,  ← Most likely      │
│   "is": 0.05,                       │
│   "or": 0.02,                       │
│   ...: ...,                         │
│ }                                   │
└─────────────────────────────────────┘
      ↓
Sample from distribution with TEMPERATURE
      ↓
Next Token: "that"
```

---

## Training vs Inference

### TRAINING MODE
```
Purpose: Learning

┌──────────────┐
│ Batch Data   │  Fixed training sequences
└──────────────┘
      ↓
┌──────────────────────┐
│ Forward Pass         │  Predict next token after each position
│                      │  Input: "To be or"
│ "To"  → Next = "be" │  Actual: "be"
│ "be"  → Next = "or" │  Actual: "or"
│ "or"  → Next = "not"│  Actual: "not"
└──────────────────────┘
      ↓
┌──────────────────────┐
│ Calculate Loss       │  How wrong? (0.0 = perfect, higher = wrong)
│ Loss = |Pred - Real|²│
│                      │  If all predictions correct: Loss ≈ 0
└──────────────────────┘
      ↓
┌──────────────────────┐
│ Backward Pass        │  Figure out what to fix
│ Calculate Gradients  │
│                      │  "Weight A caused error X"
│ Gradient = dL/dW     │  "Weight B caused error Y"
└──────────────────────┘
      ↓
┌──────────────────────┐
│ Update Weights       │  W_new = W_old - lr * gradient
│ optimizer.step()     │  Step in direction of lower loss
└──────────────────────┘
      ↓
Repeat for all batches → Epoch complete
```

### INFERENCE MODE
```
Purpose: Generating text

┌──────────────┐
│ User Prompt  │  "To be or not to be"
└──────────────┘
      ↓
┌────────────────────────────┐
│ Auto-regressive Generation │  One token at a time
│                            │
│ Iteration 1:               │
│ Input: prompt              │
│ Output: token (e.g., "that")
│                            │
│ Iteration 2:               │
│ Input: prompt + token      │
│ Output: next token         │
│                            │
│ ... repeat 100 times       │
└────────────────────────────┘
      ↓
┌──────────────────┐
│ Complete Output  │  "To be or not to be that is the question..."
└──────────────────┘
```

---

## Key Metrics

### Training Metrics

```
LOSS (Lower = Better)
┌─────────────────────────────────────┐
│ 4.0 ┤         Epoch 1 (Start)       │
│     │        ╱                       │
│ 3.0 ┤      ╱  ╲                      │
│     │    ╱      ╲  Epoch 2           │
│ 2.0 ┤  ╱  ╲    ╱╲  ╱                │
│     │╱      ╲╱    ╲╱  ╲              │
│ 1.0 ┤────────────── ╲ Epoch 3       │
│     │                ╲              │
│ 0.0 └────────────────────────────────┤
      0    50   100   150   200
      Training Batches

Good sign: Loss decreases over time
Bad sign: Loss increases (overfitting)
```

### Validation Metrics

```
PERPLEXITY (Lower = Better)

Perplexity = e^(Loss)
- Perplexity 5.0: Model is 5x uncertain about next word
- Perplexity 10.0: Model is 10x uncertain
- Shakespeare fine-tuned: ~8-15

GPT-2 on test set: ~35
ChatGPT (estimated): ~20-30
Human text: ~1-2 (very predictable)
```

---

## Data Flow Diagram

```
shakespeare.txt (Raw text)
      ↓
┌─────────────────────────┐
│ Tokenizer               │
│ vocab_size: 50,257      │
│ encodes: "To" → 284     │
└─────────────────────────┘
      ↓
[284, 572, 393, 401, 284, 572, ...]  (Token IDs)
      ↓
┌─────────────────────────────────────┐
│ Embedding Layer                     │
│ Each ID → 768-dimensional vector    │
│ Token 284 → [0.1, -0.2, 0.05, ...]  │
└─────────────────────────────────────┘
      ↓
Tensor shape: [batch_size=4, seq_len=128, hidden=768]
      ↓
┌─────────────────────────────────────┐
│ Transformer Blocks × 6              │
│ (each applies attention + FFN)       │
└─────────────────────────────────────┘
      ↓
Updated vectors: [batch=4, seq=128, hidden=768]
      ↓
┌─────────────────────────────────────┐
│ Output Layer                        │
│ vocab_size: 50,257                  │
│ Predicts: P(next_token | context)   │
└─────────────────────────────────────┘
      ↓
Logits shape: [batch=4, seq=128, vocab=50,257]
      ↓
For training: Compare predictions to actual next tokens → Loss
For inference: Sample from probability distribution → Next token
```

---

## Configuration Implications

```
CONFIG SETTING          EFFECT ON TRAINING        EFFECT ON QUALITY
───────────────────────────────────────────────────────────────
BATCH_SIZE = 8          Fast (fewer updates)      Medium
BATCH_SIZE = 4 *        Slower (more updates)     Better
                        (* Current default)
BATCH_SIZE = 32         Very fast                 Okay

NUM_EPOCHS = 1          1 pass through data       Undertrained
NUM_EPOCHS = 3 *        Balanced                  Good
                        (* Current default)
NUM_EPOCHS = 10         Thorough                  Very good
                                                  (Risk: overfitting)

LEARNING_RATE = 5e-5 *  Standard                  Good
                        (* Current default)
LEARNING_RATE = 1e-4    Too high - jumps around   Poor
LEARNING_RATE = 1e-5    Conservative              Better
                                                  (Slower)

MAX_SEQ_LENGTH = 64     Fast, limited context     Quick but short
MAX_SEQ_LENGTH = 128 *  Balanced                  Normal
                        (* Current default)
MAX_SEQ_LENGTH = 256    Slow, rich context        Better understanding
```

---

## Memory Usage

```
Model Parameters: 82 million
      ↓
Parameter Memory: 250 MB (fp16) to 330 MB (fp32)
      ↓
Total Memory for Training:
- Weights: 330 MB
- Optimizer state: 330 MB
- Gradient: 330 MB
- Activation: 100-200 MB
──────────────
Total: ~1.2 GB

Your System:
- RAM: 8 GB ✅ Plenty
- VRAM: 2 GB ✅ Should work
- CPU: Any modern (slower but works)
```

---

This visual reference should help you understand what's happening at each stage!
