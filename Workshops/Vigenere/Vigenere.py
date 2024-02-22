class VigenereEncryption:
    A: int = ord("A")
    Z: int = ord("Z")

    def is_letter(self, a: str | int) -> bool:
        if not isinstance(a, int):
            a = ord(a)

        return self.A <= a <= self.Z
    
    def elongate_key(self, text: str, key: str) -> str:
        return key * (int(len(text) / len(key)) + 1)

    def encrypt_chr(self, a: str, b: str) -> str:
        if self.is_letter(a) and self.is_letter(b):
            a = ord(a) - self.A
            b = ord(b) - self.A

            c = ((a + b) % 26) + self.A
            c = chr(c)
            return c
        return a

    def decrypt_chr(self, a: str, b: str) -> str:
        if self.is_letter(a) and self.is_letter(b):
            a = ord(a) - self.A
            b = ord(b) - self.A

            c = ((a - b) % 26) + self.A
            c = chr(c)
            return c
        return a

    def encrypt_str(self, text: str, key: str, t: int) -> str:
        text = text.upper().replace(" ", "")
        key = key.upper().replace(" ", "")

        key = self.elongate_key(text, key)

        result = "".join([self.encrypt_chr(a, b) for a, b in zip(text, key)])
        return " ".join([result[i : i + t] for i in range(0, len(result), t)])

    def decrypt_str(self, text: str, key: str, _: int) -> str:
        text = text.upper().replace(" ", "")
        key = key.upper().replace(" ", "")
        
        key = self.elongate_key(text, key)
        
        return "".join([self.decrypt_chr(a, b) for a, b in zip(text, key)])


vigenere = VigenereEncryption()

text = "THERE IS A SECRET PASSAGE BEHIND THE PICTURE FRAME"
key = "CRYPTO"
t = 3

print(f"Encrypting '{text}' with key '{key}' and t={t}: {vigenere.encrypt_str(text, key, t)}")

text = "VYC GXW URQ TVF GKN PLG CXC QXV KEB IAS RZA INF GWP PFS"

print(f"Decrypting '{text}' with key '{key}' and t={t}: {vigenere.decrypt_str(text, key, t)}")

print("Encrypting text with key")

text = input("Enter text: ")
key = input("Enter key:  ")
t = input("Enter t:    ")

print(f"Encrypting '{text}' with key '{key}' and t={t}: {vigenere.encrypt_str(text, key, int(t))}")

print("Decrypting text with key")

text = input("Enter text: ")
key = input("Enter key:  ")
t = input("Enter t:    ")

print(f"Decrypting '{text}' with key '{key}' and t={t}: {vigenere.decrypt_str(text, key, int(t))}")

