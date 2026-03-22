# 📦 Project Dependencies

## Project Requirements

This file documents all Python dependencies needed for the LLM project.

---

## 🎯 Current Dependencies (Specified in requirements.txt)

```
torch==2.0.0
transformers==4.35.0
datasets==2.14.0
numpy==1.24.0
tqdm==4.66.0
```

---

## 📋 Dependency Details

### 1. **torch** (v2.0.0)
- **Purpose**: Deep Learning Framework
- **Used for**:
  - Neural network computations
  - Tensor operations
  - GPU acceleration (CUDA)
  - Model training and inference
- **Size**: ~500 MB
- **Install alone**: `pip install torch==2.0.0`
- **Homepage**: https://pytorch.org

### 2. **transformers** (v4.35.0)
- **Purpose**: Pre-trained Language Models from Hugging Face
- **Used for**:
  - Loading DistilGPT-2 model
  - Tokenization
  - Model fine-tuning
  - Model inference
- **Dependencies**: Requires torch, numpy
- **Size**: ~50 MB
- **Install alone**: `pip install transformers==4.35.0`
- **Homepage**: https://huggingface.co/transformers

### 3. **datasets** (v2.14.0)
- **Purpose**: Dataset Management from Hugging Face
- **Used for**:
  - Downloading Shakespeare dataset
  - Dataset preparation
  - Data splitting
  - Caching
- **Dependencies**: Requires requests, tqdm, pandas
- **Size**: ~20 MB
- **Install alone**: `pip install datasets==2.14.0`
- **Homepage**: https://huggingface.co/datasets

### 4. **numpy** (v1.24.0)
- **Purpose**: Numerical Computing Library
- **Used for**:
  - Array operations
  - Mathematical computations
  - Data manipulation
- **Dependencies**: None (core library)
- **Size**: ~50 MB
- **Install alone**: `pip install numpy==1.24.0`
- **Homepage**: https://numpy.org

### 5. **tqdm** (v4.66.0)
- **Purpose**: Progress Bars
- **Used for**:
  - Training progress visualization
  - Data loading progress
  - Iteration progress tracking
- **Dependencies**: None
- **Size**: ~1 MB
- **Install alone**: `pip install tqdm==4.66.0`
- **Homepage**: https://github.com/tqdm/tqdm

---

## 🔗 Dependency Tree

```
Your LLM Project
│
├── torch (2.0.0)
│   └── Core deep learning engine
│
├── transformers (4.35.0)
│   ├── torch (required)
│   ├── numpy (required)
│   └── Other Hugging Face dependencies
│
├── datasets (2.14.0)
│   ├── requests
│   ├── tqdm (required)
│   └── pandas (optional, for better support)
│
├── numpy (1.24.0)
│   └── Core numerical library
│
└── tqdm (4.66.0)
    └── Display progress bars
```

---

## ⚙️ Installation Methods

### Method 1: Install All at Once (Recommended)
```bash
pip install -r requirements.txt
```

### Method 2: Install Individually
```bash
pip install torch==2.0.0
pip install transformers==4.35.0
pip install datasets==2.14.0
pip install numpy==1.24.0
pip install tqdm==4.66.0
```

### Method 3: Install Latest (Not Recommended - May Break Code)
```bash
pip install torch transformers datasets numpy tqdm
```

---

## 📊 System Requirements

### Minimum RAM
- **For CPU training**: 4 GB RAM
- **For GPU training**: 2 GB VRAM (recommended 4 GB)

### Disk Space
- **PyTorch**: ~500 MB
- **Transformers**: ~50 MB
- **Other dependencies**: ~100 MB
- **Virtual environment**: ~200-300 MB
- **Total**: ~1 GB minimum

### Python Version
- **Minimum**: Python 3.8
- **Recommended**: Python 3.10+

---

## 🔄 Version Information

### Current Versions (As Specified)
| Package | Version | Release Date |
|---------|---------|--------------|
| torch | 2.0.0 | March 2023 |
| transformers | 4.35.0 | October 2023 |
| datasets | 2.14.0 | October 2023 |
| numpy | 1.24.0 | December 2022 |
| tqdm | 4.66.0 | September 2023 |

---

## ✅ Verify Installation

After installing, verify everything works:

```bash
# Check each package
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import transformers; print(f'Transformers: {transformers.__version__}')"
python -c "import datasets; print(f'Datasets: {datasets.__version__}')"
python -c "import numpy; print(f'NumPy: {numpy.__version__}')"
python -c "import tqdm; print(f'tqdm: {tqdm.__version__}')"

# Or list all installed packages
pip list
```

---

## 🆕 Adding New Dependencies

If you need to add a new package:

1. **Install it**:
   ```bash
   pip install package_name
   ```

2. **Test it works**:
   ```bash
   python -c "import package_name"
   ```

3. **Update requirements.txt**:
   ```bash
   pip freeze > requirements.txt
   ```

4. **Commit to git**:
   ```bash
   git add requirements.txt
   git commit -m "Add: new dependency package_name"
   ```

---

## 🗑️ Removing Unused Dependencies

If you want to remove a package:

1. **Uninstall it**:
   ```bash
   pip uninstall package_name
   ```

2. **Update requirements.txt**:
   ```bash
   pip freeze > requirements.txt
   ```

3. **Commit to git**:
   ```bash
   git add requirements.txt
   git commit -m "Remove: unused dependency package_name"
   ```

---

## 🔒 Version Pinning

### Why Pin Versions?
- **Reproducibility**: Same code runs the same way everywhere
- **Stability**: No breaking changes from package updates
- **Compatibility**: Ensures packages work together

### Our Approach
We use **exact version pinning** (`==`):
```
torch==2.0.0       # Must be exactly this version
transformers==4.35.0
datasets==2.14.0
numpy==1.24.0
tqdm==4.66.0
```

### Other Approaches
```
torch>=2.0.0       # Any version 2.0.0 or newer
torch>=2.0.0,<3.0  # Version 2.x
torch~=2.0         # Compatible version
```

---

## ⚠️ Common Issues

### Issue: "ModuleNotFoundError: No module named 'torch'"
**Solution**:
```bash
pip install -r requirements.txt
```

### Issue: "Different version installed than required"
**Solution**:
```bash
# Force reinstall exact version
pip install --force-reinstall torch==2.0.0
```

### Issue: "Wheel not available for your Python version"
**Solution**:
```bash
# Update pip first
python -m pip install --upgrade pip

# Then reinstall packages
pip install -r requirements.txt
```

### Issue: "CUDA version mismatch"
**Solution**:
```bash
# For CPU only (skip CUDA):
pip install torch==2.0.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
```

---

## 🚀 GPU Support (Optional)

If you have an NVIDIA GPU:

### Check Current PyTorch
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

### Install GPU Version
```bash
# Install PyTorch with CUDA 11.8 support
pip install torch::2.0.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Update your config.py:
DEVICE = "cuda"  # Instead of "cpu"
```

---

## 📝 requirements.txt Format

The `requirements.txt` file uses simple format:
```
package_name==exact.version
```

### Examples in Our File
```
torch==2.0.0              # Exact version
transformers==4.35.0      # Exact version
datasets==2.14.0          # Exact version
numpy==1.24.0             # Exact version
tqdm==4.66.0              # Exact version
```

### Alternative Formats
```
torch                      # Latest version (not recommended)
torch>=2.0.0             # Minimum version
torch>=2.0.0,<3.0        # Version range
torch~=2.0               # Compatible version
```

---

## 🔍 Check for Updates

Check which packages have newer versions:

```bash
pip list --outdated
```

Output will show:
```
Package      Current  Latest
torch        2.0.0    2.1.0
transformers 4.35.0   4.36.0
```

---

## 📦 Export Current Environment

Create a snapshot of everything installed:

```bash
# Export exact versions of all packages
pip freeze > current_environment.txt

# This will include all dependencies of dependencies
# More comprehensive than requirements.txt
```

---

## 🎯 Quick Reference

### Install & Verify
```bash
# 1. Activate venv
venv\Scripts\activate

# 2. Install all dependencies
pip install -r requirements.txt

# 3. Verify installation
python -c "import torch, transformers, datasets, numpy, tqdm; print('✅ All packages installed!')"
```

### Run Your Project
```bash
python 1_setup.py      # Download data
python 2_train.py      # Train model
python 3_inference.py  # Test model
```

---

## 📚 Documentation Links

- **PyTorch**: https://pytorch.org/docs
- **Transformers**: https://huggingface.co/docs/transformers
- **Datasets**: https://huggingface.co/docs/datasets
- **NumPy**: https://numpy.org/doc
- **tqdm**: https://tqdm.github.io

---

## ✅ Dependency Checklist

Before running your project, verify:

```
☐ Python 3.8+ installed
☐ Virtual environment created (venv/)
☐ requirements.txt exists
☐ All packages installed (pip list)
☐ torch version correct
☐ transformers version correct
☐ datasets version correct
☐ numpy version correct
☐ tqdm version correct
☐ Can import all packages without errors
```

---

## 🆘 Need Help?

### Common Commands

```bash
# See what's installed
pip list

# See specific package info
pip show torch

# See available versions
pip index versions torch

# Reinstall everything fresh
pip install --force-reinstall -r requirements.txt

# Upgrade pip (often fixes issues)
python -m pip install --upgrade pip
```

---

**Last Updated**: March 22, 2026
**Status**: ✅ All Dependencies Listed and Documented
