class PlayfairEncrypter:
    matrix: list[list[str]] = []
    
    def __init__(self, key: str) -> None:
        if not key:
            raise ValueError("Key must not be empty")

        key = ''.join(c for c in key.upper() if c.isalpha() and c != 'J')

        if len(key) != len(set(key)) or len(key) != 25:
            raise ValueError("Key must be 25 distinct characters long")
        
        self.matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
        
    def find_chr(self, c: str) -> tuple[int, int]:
        for i, row in enumerate(self.matrix):
            for j, col in enumerate(row):
                if col == c:
                    return i, j
        
    def encrypt_pair(self, a: str, b: str) -> str:
        
        a_i, a_j = self.find_chr(a)
        b_i, b_j = self.find_chr(b)
        
        # TODO: Implement encryption logic
        
        

playfair = PlayfairEncrypter("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(playfair.matrix)