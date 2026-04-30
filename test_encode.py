from sgcuf_format import encode_sgcuf

# Spustí enkóder na testovacom obrázku
encode_sgcuf(
    input_path="examples/real_test.png",
    output_path="output/real_test.sgcuf",
    T=20,
    Q=85
)

print("Hotovo: encoded → output/real_test.sgcuf")

