# 🧬 TF-COMB Custom Version

This repository contains a **customized version of the [TF-COMB](https://rakesh8050.github.io/tfcomb-custom/)** (Transcription Factor Co-Occurrence Mining and Benchmarking) package.

TF-COMB is a Python-based framework used to study **co-occurrence of transcription factors (TFs)** across genomic regions, such as ChIP-seq peaks or motif-based TF binding sites (TFBS). It applies *market basket analysis* to detect statistically significant TF–TF combinations.

---

## ✨ What's New in This Custom Version
- Fixed `ValueError: var_name=['TF2'] must be a scalar` error in `objects.py`  
- Improved compatibility with `pandas >= 2.0`
- Simplified `market_basket()` function for stable execution in Google Colab
- Added better readability and comments for beginners

---

## 🧠 Key Features
- Detect co-occurring transcription factors in genomic regions  
- Supports both **motif-derived** and **ChIP-seq-based** TFBS inputs  
- Generates heatmaps, bubble plots, and rule-based TF co-occurrence tables  
- Integrates well with downstream network visualization (e.g., Cytoscape)

---

## ⚙️ Installation

You can install this version directly from GitHub:
```bash
!pip install https://github.com/Rakesh8050/tfcomb-custom.git
