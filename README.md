# SGCUF — Structural Gradient Compression Unit Format
Version: 0.9.0 (Public Preview)

SGCUF is a hybrid structural–raster image format designed for images where
**structure is more important than pixel-perfect raster fidelity**.

Unlike traditional image formats that compress every pixel independently,
SGCUF stores:

- structural relationships
- edges
- suprapixel regions
- topology information

while color information is compressed separately.

SGCUF is especially suitable for:

- offline maps
- GIS layers
- UI rendering
- technical drawings
- symbolic imagery
- low-power embedded devices

---

# Why SGCUF Exists

Traditional formats such as
:contentReference[oaicite:0]{index=0},
:contentReference[oaicite:1]{index=1} and
:contentReference[oaicite:2]{index=2}
compress raster pixel data.

For structurally dominated images this often means storing large amounts of
redundant information.

SGCUF uses a different approach:

```text
Store structure explicitly.
Store color separately.
Reconstruct deterministically.

Instead of treating the image as a dense raster,
SGCUF represents the image as a combination of:

structural edges
stable regions
suprapixel groups
local relationships

This significantly reduces the amount of information required for many
map-like and technical image types.

Core Idea

SGCUF is based on the SGCU algorithm:

Detect structural edges
Segment stable regions
Create suprapixel groups
Compress color channels separately
Store all layers in a unified container

The decoder reconstructs the image deterministically from these layers.

SGCUF does not rely on interpolation heuristics or AI reconstruction.

Use Cases

SGCUF is designed primarily for:

Offline Maps

Efficient storage and rendering of structured map data on low-power devices.

GIS Systems

Structural map representation with reduced data transfer requirements.

Smart Watches and Embedded Devices

Lower bandwidth and lower rendering cost compared to raster tiles.

Technical Drawings

Preservation of sharp edges and geometric clarity.

UI and Symbolic Graphics

Cleaner representation of icons, lines and interface elements.

Visual Comparison

Quick Results

SGCUF is not intended to replace photographic codecs.

It is optimized for structurally dominated imagery.

Example comparison:

Method	PSNR	SSIM
JPEG Q=75	32.7 dB	0.976
SGCUF T=20	41.3 dB	0.991

Additional bitrate and performance analysis is available in:

docs/performance/
Important Note

SGCUF is NOT a general-purpose photographic codec.

Natural photography, noise-heavy scenes and complex textures are still better
handled by traditional raster codecs.

SGCUF performs best when:

structure dominates texture
edges are important
topology matters more than fine raster detail
SGCUF File Structure

A .sgcu container contains:

1. Header
version
flags
structural metadata
2. Structural Layers
edge map
suprapixel map
topology information
3. Color Layers (YCbCr)

Compressed independently using JPEG.

4. Optional Compression Layers (planned)
RLE edge compression
delta compression
structural dictionaries
Pipeline Overview
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
Deterministic Reconstruction

SGCUF reconstruction is deterministic.

The decoder does not use:

hallucination
probabilistic reconstruction
AI inference
adaptive interpolation

The same structural data always produces the same output.

Installation

SGCUF is currently implemented in Python.

Clone Repository
git clone https://github.com/remitakac/SGCUF
cd SGCUF
Usage Example
Encode PNG → SGCUF
from sgcuf import encode

encode("input.png", "output.sgcu")
Decode SGCUF → PNG
from sgcuf import decode

decode("input.sgcu", "output.png")
Command-Line Interface (Planned)
sgcuf encode input.png output.sgcu
sgcuf decode input.sgcu output.png
Repository Structure
/encoder
/decoder
/specification
/examples
/tests
/docs
Roadmap
v1.1
RLE edge compression
delta compression
CLI tools
performance optimizations
experimental SGCU variants
Future Research
embedded rendering
low-power rendering pipelines
robotic scene representation
structural streaming
SGCUF hardware acceleration
Project Positioning

SGCUF should not be viewed as a replacement for traditional image codecs.

It represents a different approach to image representation:

Raster codecs store pixels.
SGCUF stores structure.

The project explores deterministic and structurally aware representations
for systems where meaning and topology are more important than raster fidelity.

License

MIT License

Author

Milan T. — System Architect

This project is part of a broader research direction focused on deterministic
architectures and structural representations of visual information.
