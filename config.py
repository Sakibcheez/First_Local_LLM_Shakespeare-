# Configuration file for your LLM project

# Model Configuration
MODEL_NAME = "distilgpt2"         # Lightweight model, perfect for beginners

# Training Configuration
BATCH_SIZE = 4                    # Reduced: safer for CPU with small dataset
LEARNING_RATE = 5e-5              # How fast the model learns
NUM_EPOCHS = 3                    # How many times to go through the dataset
MAX_SEQ_LENGTH = 128              # Maximum input length for text

# Data Configuration
TRAIN_TEST_SPLIT = 0.9            # 90% training, 10% validation

# Paths
DATA_DIR = "data"
MODEL_DIR = "models"
DEVICE = "cpu"                    # Use "cuda" if you have NVIDIA GPU

# Inference Configuration
TEMPERATURE = 0.7                 # Higher = more creative, Lower = more predictable
MAX_NEW_TOKENS = 100              # How long the generated text should be