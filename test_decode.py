from sgcuf_format import decode_sgcuf

# Decodes an SGCUF file and saves the resulting PNG
img = decode_sgcuf("output/real_test.sgcuf")
img.save("output/real_test_decoded.png")

print("Done: decoded → output/real_test_decoded.png")
