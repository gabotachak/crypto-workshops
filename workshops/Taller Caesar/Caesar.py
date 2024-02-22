class CaesarEncrypter:

    def is_letter(self, a: str | int) -> bool:
        if not isinstance(a, int):
            a = ord(a)

        return ord("A") <= a and a <= ord("Z")

    def encrypt_chr(self, a: str, k: int) -> str:
        a = a.upper()

        if self.is_letter(a):
            n = ord(a)
            n += k
            n = n if self.is_letter(n) else n - 26
            return chr(n)
        return a

    def decrypt_chr(self, a: str, k: int) -> str:
        a = a.upper()

        if self.is_letter(a):
            n = ord(a)
            n -= k
            n = n if self.is_letter(n) else n + 26
            return chr(n)
        return a

    def encrypt_str(self, t: str, m: int, k: int) -> str:
        t = t.replace(" ", "")

        r = "".join([self.encrypt_chr(a, k) for a in t.upper()])
        return " ".join([r[i : i + m] for i in range(0, len(r), m)])

    def decrypt_str(self, t: str, _: int, k: int) -> str:
        t = t.replace(" ", "")
        
        return "".join([self.decrypt_chr(a, k) for a in t.upper()])


caesar = CaesarEncrypter()

print(f"Encrypting 'HELLO' with m=5 and k=3: {caesar.encrypt_str('HELLO', 5, 3)}")
print(f"Decrypting 'KHOOR' with m=5 and k=3: {caesar.decrypt_str('KHOOR', 5, 3)}")

print("Encrypting text with key")

t = input("Enter text: ")
m = input("Enter m:    ")
k = input("Enter k:    ")

print(f"Encrypting '{t}' with m={m} and k={k}: {caesar.encrypt_str(t, int(m), int(k))}")

print("Decrypting text with key")

t = input("Enter text: ")
m = input("Enter m:    ")
k = input("Enter k:    ")

print(f"Decrypting '{t}' with m={m} and k={k}: {caesar.decrypt_str(t, int(m), int(k))}")
