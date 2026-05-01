# SGCUF v1.0  
### Structural Gradient Compression Unit — File Format

---

## SLIDE 1 — Title
**SGCUF v1.0**  
Structural Gradient Compression Unit — File Format

---

## SLIDE 2 — The Problem
### The Problem with Current Formats
- they compress pixels, not structure  
- edges get blurred  
- suprapixels are lost  
- technical images suffer from artifacts  
- maps, UI, diagrams lose clarity  

---

## SLIDE 3 — What SGCU Is
### SGCU = the algorithm
SGCU analyzes the image as:
- edges  
- suprapixels  
- color layers  
- structural relationships  

SGCU = *how we understand the image*.

---

## SLIDE 4 — What SGCUF Is
### SGCUF = the file format
Contains:
- SGCU edges  
- SGCU suprapixels  
- YCbCr channels  
- JPEG compression  
- metadata  
- structural header  

---

## SLIDE 5 — Why It Works
Traditional formats:  
→ “How to store pixels?”

SGCUF:  
→ “How to store structure?”

Result:
- sharper edges  
- cleaner shapes  
- fewer artifacts  
- better readability  

---

## SLIDE 6 — Pipeline
1. RGB → YCbCr  
2. Edge detection  
3. Suprapixel segmentation  
4. JPEG compression  
5. Structural layers stored  
6. Packed into SGCUF  

---

## SLIDE 7 — Use Cases
- maps  
- UI elements  
- technical drawings  
- diagrams  
- textures  
- visualizations  

---

## SLIDE 8 — Project Status
### SGCUF v1.0 — completed
- encoder  
- decoder  
- specification  
- tests  
- examples  
- documentation  
- naming standard  
- public release  

---

## SLIDE 9 — Roadmap
- RLE for edge maps  
- delta compression for suprapixels  
- CLI tool  
- performance improvements  
- experimental variants  
