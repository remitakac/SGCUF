from sgcuf_format import decode_sgcuf

# Dekóduje SGCUF súbor a uloží výsledný PNG
img = decode_sgcuf("output/real_test.sgcuf")
img.save("output/real_test_decoded.png")

print("Hotovo: decoded → output/real_test_decoded.png")

