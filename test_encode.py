from sgcuf_format import encode_sgcuf

# Runs the encoder on the test image
encode_sgcuf(
    input_path="examples/real_test.png",
    output_path="output/real_test.sgcuf",
    T=20,
    Q=85
)

print("Done: encoded → output/real_test.sgcuf")
