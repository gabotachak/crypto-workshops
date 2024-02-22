class OTPEncrypter:
    A: int = ord("A")

    def encrypt_chr(self, t: str, k: str) -> str:
        t = ord(t.upper()) - self.A
        k = ord(k.upper()) - self.A
        return chr((t + k) % 26 + self.A)

    def decrypt_chr(self, t: str, k: str) -> str:
        t = ord(t.upper()) - self.A
        k = ord(k.upper()) - self.A
        return chr((t - k) % 26 + self.A)

    def encrypt_str(self, t: str, k: str) -> str:
        if len(t) != len(k):
            raise ValueError("Key must be the same length as the text")
        
        return "".join([self.encrypt_chr(i, j) for i, j in zip(t, k)])

    def decrypt_str(self, s: str, k: int) -> str:
        if len(s) != len(k):
            raise ValueError("Key must be the same length as the text")
        
        return "".join([self.decrypt_chr(i, j) for i, j in zip(s, k)])

otp_encrypter = OTPEncrypter()

print(f"Encrypting 'HELLO' with key 'EOXJF': {otp_encrypter.encrypt_str('HELLO', 'EOXJF')}")
print(f"Decrypting 'LSIUT' with key 'EOXJF': {otp_encrypter.decrypt_str('LSIUT', 'EOXJF')}")

print("Encrypting text with key")

t = input("Enter text: ")
k = input("Enter key:  ")

print(f"Encrypting '{t}' with key '{k}': {otp_encrypter.encrypt_str(t, k)}")

print("Decrypting text with key")

t = input("Enter text: ")
k = input("Enter key:  ")

print(f"Decrypting '{t}' with key '{k}': {otp_encrypter.decrypt_str(t, k)}")