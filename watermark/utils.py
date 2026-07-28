def batch_to_binary(batch_id: int) -> str:
    """
    Converts a batch ID (0-255) into an 8-bit binary string.

    Example:
        47 -> '00101111'
    """
    if not (0 <= batch_id <= 255):
        raise ValueError("Batch ID must be between 0 and 255.")

    return format(batch_id, "08b")

def binary_to_bits(binary: str) -> list[int]:
    """
    Converts a binary string into a list of integer bits.

    Example:
        '00101111' -> [0, 0, 1, 0, 1, 1, 1, 1]
    """
    if any(bit not in ("0", "1") for bit in binary):
        raise ValueError("Input must contain only 0 and 1.")

    return [int(bit) for bit in binary]

if __name__ == "__main__":
    test_batch = 47

    binary = batch_to_binary(test_batch)
    bits = binary_to_bits(binary)

    print(f"Batch ID : {test_batch}")
    print(f"Binary   : {binary}")
    print(f"Bits     : {bits}")

