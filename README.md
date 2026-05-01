# SGCUF — Structural Gradient Compression Unit Format
Version: 0.9.0 (public preview)

SGCUF is a hybrid image format combining structural analysis (edges, suprapixels) with traditional JPEG compression.  
It is designed for images where **structure matters more than pixel-level fidelity**.

---

| Original | SGCUF reconstruction (T=20, Q=75) | Difference heatmap |
|----------|-----------------------------------|--------------------|
| ![](docs/real_test.png) | ![](docs/out_T20_Q75.png) | ![](docs/heatmap_diff_inverted.png) |
The difference heatmap is inverted...

---

## 📌 Why SGCUF Exists

Traditional formats (JPEG, PNG, WebP) compress **pixels**, not **structure**.  
This causes problems in:

- maps  
- UI elements  
- diagrams  
- technical drawings  
- textures with sharp edges  

SGCUF solves this by storing **structural layers** separately and losslessly.
## Quick Results

SGCUF is not just a concept – it produces significantly higher quality than baseline JPEG at comparable conditions.

| Method        | PSNR    | SSIM   |
|---------------|---------|--------|
| JPEG Q=75     | 32.7 dB | 0.976  |
| SGCUF T=20    | 41.3 dB | 0.991  |

---

## 🧠 High-Level Concept

SGCUF is built on the SGCU algorithm:

- detects edges  
- segments suprapixels  
- extracts structural relationships  
- compresses color channels via JPEG  
- stores everything in a unified container  

This results in:

- sharper edges  
- cleaner shapes  
- fewer artifacts  
- better readability for technical content  

---

## 🏗️ SGCUF File Structure

A `.sgcu` file contains:

1. **Header**  
   - version  
   - flags  
   - structural metadata  

2. **Structural Layers**  
   - edge map  
   - suprapixel map  

3. **Color Layers (YCbCr)**  
   - each compressed via JPEG  

4. **Optional Compression**  
   - RLE for edges (planned)  
   - delta compression for suprapixels (planned)  

---

## 🚀 Installation

SGCUF is implemented in Python.

```
## How to Run

```bash
git clone https://github.com/remitakac/SGCUF
cd SGCUF
python sgcu_core.py

```

*(package name placeholder — adjust when published)*

---

## 🧪 Usage Example

### Encode PNG → SGCUF

```python
from sgcuf import encode

encode("input.png", "output.sgcu")
```

### Decode SGCUF → PNG

```python
from sgcuf import decode

decode("input.sgcu", "output.png")
```

---

## 🔧 Command-Line Interface (planned)

```
sgcuf encode input.png output.sgcu
sgcuf decode input.sgcu output.png
```

---

## 🛠️ Pipeline Overview

1. RGB → YCbCr  
2. Edge detection  
3. Suprapixel segmentation  
4. JPEG compression of Y/Cb/Cr  
5. Structural layers stored  
6. Packed into SGCUF container  

---

## 📂 Repository Structure

```
/encoder
/decoder
/specification
/examples
/tests
/docs
```

---

## 🗺️ Roadmap (v1.1)

- RLE compression for edge maps  
- delta compression for suprapixel layers  
- CLI tool  
- performance improvements  
- experimental SGCU variants  

---

## 📄 License

Licensed under the MIT License.

---
## Performance Analysis
Detailed quality, size and stability graphs for SGCUF are available in:
[docs/performance](docs/performance/README.md)

---

## 👤 Author

Milan T. —System Architect--This project is part of a broader development line focused on deterministic approaches and new concepts in the field of meta‑architectures.



