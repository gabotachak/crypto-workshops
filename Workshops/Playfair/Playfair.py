class PlayfairEncrypter:
    matrix: list[list[str]] = []

    def __init__(self, key: str) -> None:
        if not key:
            raise ValueError("Key must not be empty")

        key = "".join(c for c in key.upper() if c.isalpha() and c != "J")

        if len(key) != len(set(key)) or len(key) != 25:
            raise ValueError("Key must be 25 distinct characters long")

        self.matrix = [list(key[i : i + 5]) for i in range(0, 25, 5)]

    def find_chr(self, c: str) -> tuple[int, int]:
        c = c.upper()
        for i, row in enumerate(self.matrix):
            for j, col in enumerate(row):
                if col == c:
                    return i, j

    def get_chr(self, i: int, j: int) -> str:
        return self.matrix[i % 5][j % 5]

    def encrypt_pair(self, a: str, b: str) -> str:

        a_i, a_j = self.find_chr(a)
        b_i, b_j = self.find_chr(b)

        if a_j == b_j:
            return self.get_chr(a_i + 1, a_j) + self.get_chr(b_i + 1, b_j)
        elif a_i == b_i:
            return self.get_chr(a_i, a_j + 1) + self.get_chr(b_i, b_j + 1)
        else:
            return self.get_chr(a_i, b_j) + self.get_chr(b_i, a_j)

    def decrypt_pair(self, a: str, b: str) -> str:

        a_i, a_j = self.find_chr(a)
        b_i, b_j = self.find_chr(b)

        if a_j == b_j:
            return self.get_chr(a_i - 1, a_j) + self.get_chr(b_i - 1, b_j)
        elif a_i == b_i:
            return self.get_chr(a_i, a_j - 1) + self.get_chr(b_i, b_j - 1)
        else:
            return self.get_chr(a_i, b_j) + self.get_chr(b_i, a_j)

    def encrypt_str(self, text: str) -> str:
        text = "".join(c for c in text.upper() if c.isalpha())
        text = text.replace("J", "I")

        text += "X" if len(text) % 2 == 1 else ""

        return " ".join(
            self.encrypt_pair(text[i], text[i + 1]) for i in range(0, len(text), 2)
        )

    def decrypt_str(self, text: str) -> str:
        text = text.replace(" ", "").replace("J", "I")

        return "".join(
            self.decrypt_pair(text[i], text[i + 1]) for i in range(0, len(text), 2)
        )
    

DEFAULT_KEY = """
    YOANP
    IZBCD
    EFGHK
    LMQRS
    TUVWX
"""

playfair = PlayfairEncrypter(DEFAULT_KEY)  # You must declare the key here

print(f"Using default key: {DEFAULT_KEY}")

text = "THIS SECRET MESXSAGE IS ENCRYPTEDX"

print(f"Encrypting '{text}': {playfair.encrypt_str(text)}")

text = "WE DL LK HW LY LF XP QP HF DL HY HW OY YL KP"

print(f"Decrypting '{text}': {text}")

print("Encrypting text with key")

key = input("Enter the key (set to default if empty): ")
key = key if key else DEFAULT_KEY

text = input("Enter text: ")

operation = input("Enter operation (encrypt=1/decrypt=0): ")
if operation not in ["0", "1"]:
    raise ValueError("Operation must be 0 or 1")

playfair = PlayfairEncrypter(key)

if operation == "1":
    print(f"Encrypting '{text}': {playfair.encrypt_str(text)}")
else:
    print(f"Decrypting '{text}': {playfair.decrypt_str(text)}")