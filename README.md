# SGCUF — Structural Graphics Compression Unified Format
**Stable Release:** 1.0.0  
**Documentation updated:** 2026‑05‑09

SGCUF is a structural image format based on the SGCU algorithm, designed for
deterministic reconstruction, precise edge preservation, and extremely low
data rates on technical and structure‑critical imagery.

This repository contains the reference implementation, format specification,
and research outlook for future SGCU specializations.

SGCUF is especially suitable for:

- offline maps  
- GIS layers  
- UI rendering  
- technical drawings  
- symbolic imagery  
- low-power embedded devices  

---

# Why SGCUF Exists

Traditional formats such as JPEG, PNG and WebP compress raster pixel data.  
For structurally dominated images this often means storing large amounts of redundant information.

SGCUF uses a different approach:

```text
Store structure explicitly.
Store color separately.
Reconstruct deterministically.
```

Instead of treating the image as a dense raster, SGCUF represents the image as a combination of:

- structural edges  
- stable regions  
- suprapixel groups  
- local relationships  

This significantly reduces the amount of information required for many map-like and technical image types.

---

## Core Idea

SGCUF is based on the SGCU algorithm:

- Detect structural edges  
- Segment stable regions  
- Create suprapixel groups  
- Compress color channels separately  
- Store all layers in a unified container  

The decoder reconstructs the image deterministically from these layers.  
SGCUF does not rely on interpolation heuristics or AI reconstruction.

---

## Use Cases

### Offline Maps
Efficient storage and rendering of structured map data on low-power devices.

### GIS Systems
Structural map representation with reduced data transfer requirements.

### Smart Watches and Embedded Devices
Lower bandwidth and lower rendering cost compared to raster tiles.

### Technical Drawings
Preservation of sharp edges and geometric clarity.

### UI and Symbolic Graphics
Cleaner representation of icons, lines and interface elements.

---

## Visual Comparison

SGCUF is not intended to replace photographic codecs.  
It is optimized for structurally dominated imagery.

### Example comparison

| Method     | PSNR     | SSIM   |
|------------|----------|--------|
| JPEG Q=75  | 32.7 dB  | 0.976  |
| SGCUF T=20 | 41.3 dB  | 0.991  |

Additional bitrate and performance analysis is available in:  
`docs/performance/`

---

## Important Note

SGCUF is NOT a general-purpose photographic codec.

Natural photography, noise-heavy scenes and complex textures are still better handled by traditional raster codecs.

SGCUF performs best when:

- structure dominates texture  
- edges are important  
- topology matters more than fine raster detail  

---

## SGCUF File Structure

A `.sgcu` container contains:

1. **Header**  
   - version  
   - flags  
   - structural metadata  

2. **Structural Layers**  
   - edge map  
   - suprapixel map  
   - topology information  

3. **Color Layers (YCbCr)**  
   - compressed independently using JPEG  

4. **Optional Compression Layers (planned)**  
   - RLE edge compression  
   - delta compression  
   - structural dictionaries  

---

## Pipeline Overview

```
RGB
 ↓
YCbCr conversion
 ↓
Structural edge detection
 ↓
Suprapixel segmentation
 ↓
Color compression
 ↓
SGCUF container packing
```

---

## Deterministic Reconstruction

SGCUF reconstruction is deterministic.

The decoder does NOT use:

- hallucination  
- probabilistic reconstruction  
- AI inference  
- adaptive interpolation  

The same structural data always produces the same output.

---

## Installation

SGCUF is currently implemented in Python.

### Clone Repository
```bash
git clone https://github.com/remitakac/SGCUF
cd SGCUF
```

---

## Usage Example

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

## Command-Line Interface (Planned)

```
sgcuf encode input.png output.sgcu
sgcuf decode input.sgcu output.png
```

---

## Repository Structure

```
/encoder
/decoder
/specification
/examples
/tests
/docs
```

---

## Roadmap

### v1.1
- RLE edge compression  
- delta compression  
- CLI tools  
- performance optimizations  
- experimental SGCU variants  

---

## Future Research

- embedded rendering  
- low-power rendering pipelines  
- robotic scene representation  
- structural streaming  
- SGCUF hardware acceleration  

---

## Project Positioning

SGCUF should not be viewed as a replacement for traditional image codecs.  
It represents a different approach to image representation:

- Raster codecs store pixels.  
- SGCUF stores structure.  

The project explores deterministic and structurally aware representations for systems where meaning and topology are more important than raster fidelity.

---

## Decode Determinism

SGCUF decoding is fully deterministic.  
The decoder performs no interpolation, no heuristics, and no probabilistic reconstruction.  
Every pixel is reconstructed exactly from the stored Y, Cb, Cr channels and the edge/suprapixel masks.

### Deterministic Encode → Decode Test

A full encode→decode cycle was executed on a real technical map (`real_test.png`):

- Input image successfully encoded into `out.sgcuf`
- The SGCUF file was decoded without errors
- Output image (`decoded.png`) preserved:
  - identical dimensions
  - correct color channels
  - correct edge structure
  - all technical details (text, lines, legend)

This confirms that the SGCUF big‑endian format is stable and produces a bit‑exact deterministic reconstruction of the visual structure.

---

## Future Directions & Research Outlook

The SGCU core algorithm and the SGCUF file format represent the stable foundation of
this project. The following areas are not part of the current release, but outline
potential directions for future research, specialization, and applied development.

### SGCU‑T — Technical Imagery

SGCU‑T represents a potential specialization of the SGCU algorithm for structure‑critical
visuals such as maps, CAD drawings, GIS layers, schematics, diagrams, and other technical
images where precise edges and deterministic reconstruction are essential.

This category also includes **IoT and small‑display environments** (embedded devices,
wearables, smart watches, low‑power UI systems), where extremely low data rates and
precise edge preservation are required for efficient rendering on limited hardware.

#### Research Note (bpp)
In internal experiments, the SGCU algorithm achieved very low data rates on technical
imagery, typically in the range of 0.03–0.10 bpp. Some datasets produced even lower
values; however, these extreme results are considered research observations rather than
guaranteed performance parameters. They indicate the potential of SGCU‑T for domains
where structural accuracy must be preserved with minimal data overhead.

#### Relation to MTA
The **MTA (Multi‑Topology Architecture)** project uses SGCU‑T‑style structural outputs
as deterministic input for higher‑level reasoning, robotic inspection, and industrial
decision systems. MTA is not part of this repository, but SGCU‑T provides the structural
foundation required by such systems.

---

### SGCU‑R — Industrial & Robotic Applications

A possible branch focused on industrial and robotic use cases, where precise detection
of edges, contours, and shapes is required. SGCU‑R could serve as a deterministic input
for machine‑vision pipelines, quality‑control systems, and real‑time 2D inspection
processes in manufacturing environments.

---

### SGCU‑X — Experimental & Research Branch

A research‑oriented space for experimenting with segmentation strategies, suprapixel
models, adaptive masks, hybrid structural layers, and new algorithmic approaches.
SGCU‑X is not intended for production use, but as a laboratory for testing new ideas
and exploring the limits of the SGCU concept.

---

## License

MIT License

---

## Author

**Milan T. — System Architect**

This project is part of a broader research direction focused on deterministic architectures and structural representations of visual information.

