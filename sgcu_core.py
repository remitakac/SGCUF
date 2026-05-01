import numpy as np
from PIL import Image
import io

# -----------------------------
# YCbCr conversions
# -----------------------------

def rgb_to_ycbcr(img):
    arr = np.asarray(img).astype(np.float32)
    R, G, B = arr[...,0], arr[...,1], arr[...,2]

    Y  =  0.299*R + 0.587*G + 0.114*B
    Cb = -0.1687*R - 0.3313*G + 0.5*B + 128
    Cr =  0.5*R - 0.4187*G - 0.0813*B + 128

    return Y, Cb, Cr

def ycbcr_to_rgb(Y, Cb, Cr):
    R = Y + 1.402*(Cr-128)
    G = Y - 0.344136*(Cb-128) - 0.714136*(Cr-128)
    B = Y + 1.772*(Cb-128)

    arr = np.stack([R,G,B], axis=-1)
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGB")

# -----------------------------
# SGCU edge detection
# -----------------------------

def detect_edges_y(Y, T):
    H, W = Y.shape
    edges = np.zeros((H, W), dtype=np.uint8)

    for y in range(0, H-1):
        for x in range(0, W-1):
            block = Y[y:y+2, x:x+2]
            if block.max() - block.min() > T:
                edges[y:y+2, x:x+2] = 1

    return edges

# -----------------------------
# SGCU suprapixel detection
# -----------------------------

def detect_suprapixels_y(Y, T):
    H, W = Y.shape
    supra = np.zeros((H, W), dtype=np.uint8)

    for y in range(0, H-1, 2):
        for x in range(0, W-1, 2):
            block = Y[y:y+2, x:x+2]
            if block.max() - block.min() <= T:
                supra[y:y+2, x:x+2] = 1

    return supra

# -----------------------------
# JPEG compression of a single channel
# -----------------------------

def jpeg_compress_channel(channel, Q):
    img = Image.fromarray(channel.astype(np.uint8))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=Q)
    return buf.getvalue()

def jpeg_decompress_channel(jpeg_bytes):
    buf = io.BytesIO(jpeg_bytes)
    img = Image.open(buf)
    return np.asarray(img).astype(np.float32)

# -----------------------------
# Hybrid reconstruction
# -----------------------------

def sgcu_hybrid_ycbcr(Y_jpeg, Cb_jpeg, Cr_jpeg, edges, supra):
    # JPEG decoded channels
    Yd = Y_jpeg
    Cbd = Cb_jpeg
    Crd = Cr_jpeg

    # Hybrid reconstruction (placeholder logic for now)
    Y_final = np.where(edges == 1, Yd, Yd)
    Cb_final = Cbd
    Cr_final = Crd

    return Y_final, Cb_final, Cr_final
