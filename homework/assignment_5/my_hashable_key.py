class MyHashableKey:
    def __init__(self, int_value, string_value) -> None:
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        return (
            self.int_value == other.int_value
            and self.string_value == other.string_value
            and hash(self) == hash(other)
        )

    def __hash__(self):
        """The code is from the book DSA for Python page 375
        - The mask is created by shiftin the 1 up by 32 bits
        and there by createing a 32 but mask with all 1's
        The mask ensures that the hash stays a 32 bit value
        - Each character in the string gets shifted to the left by 5 then a bitwise
        AND operation is perforemd with the mask to get only the least significant
        bit and discarding any overflow.
        - The hash is then shifted 27 bits to the right to create more diversity in the hash function
        - A bitvice XOR operation is perfored on a char value and a int to ad dmore randomeness to the hash. The char value is a unicode character.
        """
        mask = (1 << 32) - 1
        h = 0
        for char in self.string_value:
            h = (h << 5 & mask) | (h >> 27)
            h += ord(char) ^ self.int_value

        return h
