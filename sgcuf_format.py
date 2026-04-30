import struct
import numpy as np
from PIL import Image
from sgcu_core import (
    rgb_to_ycbcr, ycbcr_to_rgb,
    detect_edges_y, detect_suprapixels_y,
    jpeg_compress_channel, jpeg_decompress_channel
)

MAGIC = b"SGCUFMT\n"
VERSION = 1

# -----------------------------------
# Padding na párne rozmery
# -----------------------------------

def pad_even(img):
    arr = np.asarray(img)
    H, W = arr.shape[:2]

    new_H = H + (H % 2)
    new_W = W + (W % 2)

    if new_H == H and new_W == W:
        return img, H, W

    padded = np.zeros((new_H, new_W, 3), dtype=np.uint8)
    padded[:H, :W] = arr
    padded[H:, :W] = arr[H-1:H]
    padded[:H, W:] = arr[:, W-1:W]
    padded[H:, W:] = arr[H-1, W-1]

    return Image.fromarray(padded), H, W

# -----------------------------------
# ENCODER
# -----------------------------------

def encode_sgcuf(input_path, output_path, T=20, Q=85):
    img = Image.open(input_path).convert("RGB")

    padded_img, orig_H, orig_W = pad_even(img)
    Y, Cb, Cr = rgb_to_ycbcr(padded_img)

    edges = detect_edges_y(Y, T)
    supra = detect_suprapixels_y(Y, T)

    Y_jpeg = jpeg_compress_channel(Y, Q)
    Cb_jpeg = jpeg_compress_channel(Cb, Q)
    Cr_jpeg = jpeg_compress_channel(Cr, Q)

    len_Y = len(Y_jpeg)
    len_Cb = len(Cb_jpeg)
    len_Cr = len(Cr_jpeg)
    len_edge = edges.size
    len_supra = supra.size

    with open(output_path, "wb") as f:
        f.write(MAGIC)
        f.write(struct.pack("<HIIIIHHQ",
            VERSION,
            orig_W, orig_H,
            padded_img.width, padded_img.height,
            T, Q,
            0
        ))

        f.write(struct.pack("<IIIII",
            len_Y, len_Cb, len_Cr,
            len_edge, len_supra
        ))

        f.write(Y_jpeg)
        f.write(Cb_jpeg)
        f.write(Cr_jpeg)
        f.write(edges.tobytes())
        f.write(supra.tobytes())

# -----------------------------------
# DECODER
# -----------------------------------

def decode_sgcuf(path):
    with open(path, "rb") as f:
        data = f.read()

    pos = 0
    assert data[:8] == MAGIC
    pos += 8

    (ver, orig_W, orig_H, W, H, T, Q, _) = struct.unpack_from("<HIIIIHHQ", data, pos)
    pos += 30

    len_Y, len_Cb, len_Cr, len_edge, len_supra = struct.unpack_from("<IIIII", data, pos)
    pos += 20

    Y_jpeg = data[pos:pos+len_Y]; pos += len_Y
    Cb_jpeg = data[pos:pos+len_Cb]; pos += len_Cb
    Cr_jpeg = data[pos:pos+len_Cr]; pos += len_Cr

    edges = np.frombuffer(data[pos:pos+len_edge], dtype=np.uint8).reshape(H, W)
    pos += len_edge

    supra = np.frombuffer(data[pos:pos+len_supra], dtype=np.uint8).reshape(H, W)

    Yd = jpeg_decompress_channel(Y_jpeg)
    Cbd = jpeg_decompress_channel(Cb_jpeg)
    Crd = jpeg_decompress_channel(Cr_jpeg)

    Yf, Cbf, Crf = Yd, Cbd, Crd

    rgb = ycbcr_to_rgb(Yf, Cbf, Crf)
    return rgb.crop((0, 0, orig_W, orig_H))
