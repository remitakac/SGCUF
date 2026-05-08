# SGCUF — Structural Graphics Compression Unified Format
## Format Specification (Version 1.0.0)

SGCUF is a hybrid structural–raster image format designed for images where structural information (edges, suprapixels, topology) is more important than pixel‑level fidelity. The format combines structural layers (edge map, suprapixel map) with JPEG‑compressed Y, Cb, Cr channels and deterministic reconstruction rules. This document defines the complete binary layout of SGCUF version 1.0.0.

## 1. File Overview
All SGCUF files begin with a fixed header, followed by size descriptors for each segment, and finally the raw segment payloads. The format is fully sequential and does not require random access. All multi‑byte fields use big‑endian encoding.

---

Binary Layout Summary
+----------------------+-------------------------------+
| Field                | Size (bytes)                  |
+----------------------+-------------------------------+
| MAGIC                | 8                             |
| VERSION              | 2                             |
| ORIG_WIDTH           | 4                             |
| ORIG_HEIGHT          | 4                             |
| PADDED_WIDTH         | 4                             |
| PADDED_HEIGHT        | 4                             |
| T (threshold)        | 2                             |
| Q (JPEG quality)     | 2                             |
| RESERVED             | 8                             |
+----------------------+-------------------------------+
| LEN_Y                | 4                             |
| LEN_CB               | 4                             |
| LEN_CR               | 4                             |
| LEN_EDGE             | 4                             |
| LEN_SUPRA            | 4                             |
+----------------------+-------------------------------+
| JPEG_Y               | LEN_Y                         |
| JPEG_CB              | LEN_CB                        |
| JPEG_CR              | LEN_CR                        |
| EDGE_MAP             | LEN_EDGE                      |
| SUPRAPIXEL_MAP       | LEN_SUPRA                     |
+----------------------+-------------------------------+

---

## 3. Header Fields

### MAGIC (8 bytes)
Literal ASCII sequence: "SGCUFMT\n"

### VERSION (uint16)
Current version: 1

### ORIG_WIDTH, ORIG_HEIGHT (uint32)
Original image dimensions before padding.

### PADDED_WIDTH, PADDED_HEIGHT (uint32)
Even dimensions required for JPEG 8×8 block alignment.

### T — Structural Threshold (uint16)
Threshold used for edge detection and suprapixel segmentation.

### Q — JPEG Quality (uint16)
Quality factor used for Y, Cb, Cr compression.

### RESERVED (uint64)
Reserved for future use. Must be zero.

## 4. Segment Length Table
Immediately after the header, SGCUF stores the sizes of all variable‑length segments:
LEN_Y: size of JPEG‑compressed Y channel  
LEN_CB: size of JPEG‑compressed Cb channel  
LEN_CR: size of JPEG‑compressed Cr channel  
LEN_EDGE: size of edge map (H × W bytes)  
LEN_SUPRA: size of suprapixel map (H × W bytes)  
All values are uint32, big‑endian.

## 5. Segment Payloads

### JPEG Y Channel
Raw JPEG bitstream of the luminance channel.

### JPEG Cb, Cr Channels
Raw JPEG bitstreams of chroma channels.

### EDGE_MAP
Raw uint8 buffer of shape (PADDED_HEIGHT × PADDED_WIDTH). Values represent structural edges detected from the Y channel.

### SUPRAPIXEL_MAP
Raw uint8 buffer of shape (PADDED_HEIGHT × PADDED_WIDTH). Values represent suprapixel region assignments.

## 6. Decoding Procedure (Deterministic)
1. Read MAGIC and verify.  
2. Parse header fields.  
3. Parse segment lengths.  
4. Read JPEG Y, Cb, Cr payloads.  
5. Read EDGE_MAP and SUPRAPIXEL_MAP.  
6. JPEG‑decompress Y, Cb, Cr.  
7. Convert YCbCr → RGB.  
8. Crop to (ORIG_WIDTH × ORIG_HEIGHT).  
Structural layers are available for downstream processing but do not modify raster reconstruction.

## 7. Padding Rules
SGCUF requires even dimensions for JPEG block alignment. If the input image has odd width or height, the last row/column is duplicated. PADDED_WIDTH/HEIGHT store the padded size, ORIG_WIDTH/HEIGHT store the original size. Decoder crops the final image back to original dimensions.

## 8. Endianness
All multi‑byte fields use big‑endian encoding.

## 9. Future Extensions (Reserved)
The following fields are reserved for future SGCUF versions:
RESERVED (8 bytes)  
potential additional structural layers  
optional metadata blocks  
optional compression of structural maps  
These extensions will not break backward compatibility.

## 10. Versioning Policy
SGCUF follows a strict versioning model:
VERSION increments only when the binary layout changes.  
Documentation updates do not affect VERSION.  
Structural algorithms (SGCU) may evolve independently of SGCUF.  
Current stable version: 1.0.0


