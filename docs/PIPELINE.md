# SGCUF Pipeline Architecture
## Version 1.0.0

This document defines the complete, deterministic pipeline for the SGCUF format. The pipeline is universal, independent of the input image format, and consists of strictly defined steps for encoding and decoding. Each step has a clear input, output, and purpose.

## 1. Encode Pipeline (RGB → SGCUF)

### 1.1 Load Input Image
The input may be any supported image format (JPEG, PNG, WebP, TIFF, BMP).  
Output: RGB matrix (uint8) with dimensions H × W × 3.

### 1.2 Pad to Even Dimensions
If width or height is odd, the last row or column is duplicated.  
Output: RGB image with dimensions padded_H × padded_W and original dimensions orig_H × orig_W.

### 1.3 Convert RGB → YCbCr
The RGB image is converted into three channels: Y, Cb, Cr.  
Output: three 2D matrices (uint8).

### 1.4 Structural Analysis (Edges, Suprapixels)
From the Y channel, two structural layers are computed:
- edge map (uint8)
- suprapixel map (uint8)

Both have dimensions padded_H × padded_W.

### 1.5 JPEG Compression of Y, Cb, Cr
Each channel is compressed independently using JPEG with quality Q.  
Output: three bytestreams: Y_jpeg, Cb_jpeg, Cr_jpeg.

### 1.6 Compute Segment Lengths
Lengths are computed as:
- LEN_Y
- LEN_CB
- LEN_CR
- LEN_EDGE = padded_H × padded_W
- LEN_SUPRA = padded_H × padded_W

### 1.7 Build SGCUF Header
The header contains:
- MAGIC = "SGCUFMT\n"
- VERSION
- ORIG_WIDTH, ORIG_HEIGHT
- PADDED_WIDTH, PADDED_HEIGHT
- T (threshold)
- Q (JPEG quality)
- RESERVED = 0

### 1.8 Write Segment Length Table
The following values are written in order:
LEN_Y, LEN_CB, LEN_CR, LEN_EDGE, LEN_SUPRA.

### 1.9 Write Payloads
Payloads are written in this order:
1. JPEG Y
2. JPEG Cb
3. JPEG Cr
4. edge map (raw uint8)
5. suprapixel map (raw uint8)

The result is a complete SGCUF file.

---

## 2. Decode Pipeline (SGCUF → RGB)

### 2.1 Read File and Verify MAGIC
All data is loaded and the MAGIC identifier is validated.

### 2.2 Parse Header
The following values are extracted:
VERSION, ORIG_WIDTH, ORIG_HEIGHT, PADDED_WIDTH, PADDED_HEIGHT, T, Q.

### 2.3 Parse Segment Lengths
The following lengths are read:
LEN_Y, LEN_CB, LEN_CR, LEN_EDGE, LEN_SUPRA.

### 2.4 Extract Payloads
The file is sliced into:
- Y_jpeg
- Cb_jpeg
- Cr_jpeg
- edge map (raw)
- suprapixel map (raw)

### 2.5 Reconstruct Structural Maps
Edge and suprapixel maps are converted into 2D uint8 matrices.

### 2.6 JPEG Decompression
Each channel is decompressed:
Yd, Cbd, Crd.

### 2.7 Convert YCbCr → RGB
An RGB image of size padded_H × padded_W is reconstructed.

### 2.8 Crop to Original Size
The image is cropped to orig_H × orig_W.  
Output: final RGB image.

---

## 3. Pipeline Properties

### Deterministic
Each step has a single, unambiguous input and output.  
No randomness is used anywhere in the pipeline.

### Modular
Each step is an independent module that can be replaced without affecting the others.

### Extensible
The pipeline supports future extensions:
- additional structural layers
- alternative compression methods
- metadata blocks
- validation layers

### Input Format Independent
All inputs are converted to RGB, and the pipeline proceeds identically for all formats.

---

## 4. Summary
The SGCUF pipeline defines the complete flow of data from an input image to a binary SGCUF file and back.  
It is deterministic, modular, extensible, and independent of the input format.  
This document serves as the architectural foundation for implementation, validation, and future development of the SGCUF system.

