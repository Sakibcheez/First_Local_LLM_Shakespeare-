"""
STEP 3: Use your trained LLM for inference
This script loads your fine-tuned model and generates text.

You can:
1. Generate text from a prompt
2. Test different temperature settings
3. See how your model learned from the Shakespeare data
"""

import os
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from config import MODEL_DIR, DEVICE, MAX_NEW_TOKENS, TEMPERATURE

print("=" * 60)
print("STEP 3: INFERENCE - TESTING YOUR LLM")
print("=" * 60)

# Check if model exists
model_path = os.path.join(MODEL_DIR, "best_model")
if not os.path.exists(model_path):
    print(f"\n❌ Error: Model not found at {model_path}")
    print(f"   Please run python 2_train.py first to train the model!")
    exit(1)

# Check device
if torch.cuda.is_available():
    device = "cuda"
    print(f"\n🚀 Using GPU for inference")
else:
    device = "cpu"
    print(f"\n💻 Using CPU for inference")

# ==================== 1. LOAD MODEL ====================
print(f"\n📥 Loading model from: {model_path}")
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)
model.to(device)
model.eval()  # Evaluation mode (no dropout, etc.)
print(f"✅ Model loaded successfully")

# ==================== 2. INFERENCE FUNCTION ====================
def generate_text(prompt, max_length=MAX_NEW_TOKENS, temperature=TEMPERATURE):
    """
    Generate text continuation from a prompt.

    Args:
        prompt (str): Starting text
        max_length (int): How many new tokens to generate
        temperature (float):
            - < 1.0: More predictable, focused
            - 1.0: Neutral
            - > 1.0: More creative, diverse

    Returns:
        str: Generated text
    """
    # Tokenize input prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

    with torch.no_grad():  # Don't calculate gradients for inference
        # Generate tokens one at a time
        output_ids = model.generate(
            input_ids=input_ids,
            max_new_tokens=max_length,
            temperature=temperature,
            top_p=0.95,  # Nucleus sampling
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )

    # Decode token IDs back to text
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return generated_text

# ==================== 3. INTERACTIVE MODE ====================
print(f"\n{'=' * 60}")
print("🎭 SHAKESPEARE LLM GENERATOR")
print(f"{'=' * 60}")
print(f"\nYour model is ready! Enter prompts and it will continue them.")
print(f"Settings:")
print(f"   Max tokens: {MAX_NEW_TOKENS}")
print(f"   Temperature: {TEMPERATURE}")
print(f"   Type 'help' for options")
print(f"   Type 'quit' to exit\n")

while True:
    try:
        prompt = input("📝 Enter prompt: ").strip()

        if prompt.lower() == 'quit':
            print("\n👋 Goodbye!")
            break

        if prompt.lower() == 'help':
            print("""
Commands:
  quit          - Exit the program
  help          - Show this help message

Settings you can modify in config.py:
  MAX_NEW_TOKENS  - Length of generated text (default: 100)
  TEMPERATURE     - Creativity level (default: 0.7)
                    0.3 = Predictable, 0.7 = Balanced, 1.2 = Creative

Examples to try:
  "To be or not to be"
  "The quality of mercy"
  "Now is the winter"
  "All the world's a stage"
            """)
            continue

        if not prompt:
            print("⚠️  Please enter a prompt!")
            continue

        print("\n⏳ Generating text...")

        # Generate with current settings
        generated = generate_text(prompt, max_length=MAX_NEW_TOKENS, temperature=TEMPERATURE)

        print(f"\n{'─' * 60}")
        print(f"Generated text:")
        print(f"{'─' * 60}")
        print(generated)
        print(f"{'─' * 60}\n")

    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!")
        break
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please try again.\n")

# ==================== 4. BATCH EXAMPLES (Optional) ====================
print("\n✅ Program finished!")
