# SGCUF — Structural–Raster Hybrid Image Format  
**Version: 0.9.0 (public preview)**

SGCUF is a **hybrid structural–raster image format** optimized for images where **structure matters more than pixel‑level fidelity**.  
It stores **explicit structural information** (edges, suprapixels, region transitions) and compresses color separately, resulting in significantly higher efficiency for maps, UI and technical imagery.

---

## 🔥 Use Case Highlight

**Offline maps on low‑power devices:**  
SGCUF reduces data size and improves rendering efficiency by storing only structural information instead of full raster tiles.

---

## Visual Comparison

**Original → SGCUF reconstruction → Difference heatmap**

![](docs/performance/triplets/visual_triplet_sgcu.png)

---

## 📌 Why SGCUF Exists

Traditional formats (JPEG, PNG, WebP) compress **pixels**, not **structure**.  
This leads to inefficiencies in:

- maps  
- UI elements  
- diagrams  
- technical drawings  
- vector‑like raster exports  

SGCUF avoids this by encoding **structural layers** explicitly and deterministically.

---

## Performance Summary

SGCUF is optimized for **structurally dominated images where raster compression is inefficient**.

| Method        | Bitrate (bpp) | PSNR    | SSIM   |
|---------------|----------------|---------|--------|
| JPEG Q=75     | 0.42           | 32.7 dB | 0.976  |
| SGCUF T=20    | 0.41           | 41.3 dB | 0.991  |

**Interpretation:**  
At the same bitrate, SGCUF preserves edges, symbols and technical shapes with significantly higher fidelity.

---

## 🧠 High‑Level Concept

SGCUF is built on the SGCU structural pipeline:

- edge detection  
- suprapixel segmentation  
- structural relationship extraction  
- color compression (YCbCr)  
- unified container format  

This results in:

- sharper edges  
- cleaner shapes  
- fewer artifacts  
- improved readability for technical content  

---

## 🧩 Decode Determinism

**SGCUF decoding is fully deterministic and does not rely on interpolation, prediction or reconstruction heuristics.**  
The same input always produces the same output.

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
   - each compressed independently  

4. **Optional Compression (planned)**  
   - RLE for edges  
   - delta compression for suprapixels  

---

## 🛠️ Pipeline Overview

1. RGB → YCbCr  
2. Edge detection  
3. Suprapixel segmentation  
4. Color compression  
5. Structural layers stored  
6. Packed into SGCUF container  

---

## ❌ When NOT to Use SGCUF

SGCUF is not suitable for:

- natural photographs  
- noisy images  
- high‑entropy textures (grass, stone, skin, clouds)  
- scenes with complex gradients  

For these, AVIF/WebP/JPEG XL are more efficient.

---

## 🚀 Installation

SGCUF is implemented in Python.

```bash
git clone https://github.com/remitakac/SGCUF
cd SGCUF
python sgcu_core.py
🧪 Usage Example
Encode PNG → SGCUF

python
from sgcuf import encode
encode("input.png", "output.sgcu")
Decode SGCUF → PNG

python
from sgcuf import decode
decode("input.sgcu", "output.png")
🔧 Command‑Line Interface (planned)
Kód
sgcuf encode input.png output.sgcu
sgcuf decode input.sgcu output.png
📂 Repository Structure
Kód
/encoder
/decoder
/specification
/examples
/tests
/docs
🗺️ Roadmap (v1.1)
RLE compression for edge maps

delta compression for suprapixel layers

CLI tool

performance improvements

experimental SGCU variants

📄 License
MIT License

# 📊 Performance Analysis

## PSNR vs JPEG
![PSNR all T](docs/performance/core/psnr_all_T_v1.png)

## SSIM vs JPEG
![SSIM all T](docs/performance/core/ssim_all_T_v1.png)

## Output Size vs JPEG
![Size all T](docs/performance/core/size_all_T_v1.png)

---

# Visual Triplets

## JPEG
![Visual triplet JPEG](docs/performance/triplets/visual_triplet_jpeg.png)

## SGCUF
![Visual triplet SGCUF](docs/performance/triplets/visual_triplet_sgcu.png)

---

# Heatmaps

![Heatmap PSNR](docs/performance/heatmaps/heatmap_psnr_v1.png)
![Heatmap SSIM](docs/performance/heatmaps/heatmap_ssim_v1.png)
![Heatmap Diff Inverted](docs/performance/heatmaps/heatmap_diff_inverted.png)

---

# Test Outputs

![Output T20 Q75](docs/performance/_tests/out_T20_Q75.png)
![Real Test](docs/performance/_tests/real_test.png)

👤 Author
Milan T. — System Architect
Part of a broader research line focused on deterministic approaches and structural meta‑architectures.
