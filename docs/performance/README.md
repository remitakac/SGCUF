# SGCUF Performance Analysis

## Overview
This folder contains the core performance visualizations of the SGCUF hybrid image format.  
The graphs demonstrate how SGCUF behaves across different values of **T** (transform depth) and **Q** (quality factor), focusing on:

- PSNR (Peak Signal-to-Noise Ratio)
- SSIM (Structural Similarity Index)
- Output size stability
- Global smoothness and monotonicity across the T×Q grid

These results confirm that SGCUF is stable, predictable, and robust across all tested configurations.

---

## 1. PSNR vs Q (all T)
![PSNR vs Q](psnr_all_T_v1.png)

## 2. SSIM vs Q (all T)
![SSIM vs Q](ssim_all_T_v1.png)

## 3. Output Size vs Q (all T)
![Size vs Q](size_all_T_v1.png)

## 4. PSNR Heatmap (T × Q)
![PSNR Heatmap](heatmap_psnr_v1.png)

## 5. SSIM Heatmap (T × Q)
![SSIM Heatmap](heatmap_ssim_v1.png)

---

## Conclusions
- SGCUF produces stable quality across all T values.
- Increasing Q increases quality monotonically.
- Output size remains nearly constant, independent of T and Q.
- Heatmaps confirm smooth, continuous behavior across the entire parameter space.

These properties make SGCUF suitable for predictable, high‑quality hybrid image encoding.
