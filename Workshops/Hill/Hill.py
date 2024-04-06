from typing import List
import numpy
import math
from sympy import Matrix


class HillEncrypter:
    key: List[List[int]]

    def __init__(self, key: List[int]) -> None:

        if len(key) != 4:
            raise ValueError("Key must have 4 elements")

        self.key = [key[:2], key[2:]]

        det = self.determinant()
        if det == 0:
            raise ValueError("Cannot encrypt because the determinant is 0")

        cop = self.coprimes()
        if cop != 1:
            raise ValueError(
                "Cannot encrypt because the gcd(detA,26) is different from 1"
            )

    def determinant(self) -> int:
        matrix = numpy.array(self.key)
        return int(numpy.linalg.det(matrix))

    def coprimes(self) -> int:
        det = self.determinant()
        return math.gcd(det, 26)

    @staticmethod
    def matrixInverseMod(matrix, mod):
        nr = matrix.shape[0]
        nc = matrix.shape[1]
        sympyMatrix = Matrix(matrix)
        sympyMatrixInv = sympyMatrix.inv_mod(mod)
        matrixInv = numpy.array(sympyMatrixInv)
        k = nr
        vmtest = [[1 for i in range(k)] for j in range(k)]
        vmtestInv = sympyMatrix * sympyMatrixInv
        for i in range(k):
            for j in range(k):
                vmtest[i][j] = vmtestInv[i, j] % mod
        return matrixInv

    def encrypt(self, message) -> str:
        message = message.upper()
        message = message.replace(" ", "")
        letterNumber = []
        addedNumber = []
        addedLetter = []
        for i in message:
            i = ord(i) - 65
            letterNumber.append(i)
        for j in range(0, len(letterNumber) - 1, 2):
            num1 = (letterNumber[j] * self.key[0][0]) + (
                letterNumber[j + 1] * self.key[1][0]
            )
            addedNumber.append(num1 % 26)
            num2 = (letterNumber[j] * self.key[0][1]) + (
                letterNumber[j + 1] * self.key[1][1]
            )
            addedNumber.append(num2 % 26)
        for k in range(len(addedNumber)):
            addedLetter.append(chr(addedNumber[k] + 65))
        return "".join(addedLetter)

    def decrypt(self, message):
        message = message.upper()
        message = message.replace(" ", "")
        letterNumber = []
        addedNumber = []
        addedLetter = []
        mod = 26
        matrix = numpy.array(self.key)
        matrixInv = self.matrixInverseMod(matrix, mod)
        print("The modular inverse matrix is:")
        print(matrixInv[0][0], "  ", matrixInv[0][1])
        print(matrixInv[1][0], "  ", matrixInv[1][1])
        for i in message:
            i = ord(i) - 65
            letterNumber.append(i)
        for j in range(0, len(letterNumber) - 1, 2):
            num1 = (letterNumber[j] * matrixInv[0][0]) + (
                letterNumber[j + 1] * matrixInv[1][0]
            )
            addedNumber.append(num1 % 26)
            num2 = (letterNumber[j] * matrixInv[0][1]) + (
                letterNumber[j + 1] * matrixInv[1][1]
            )
            addedNumber.append(num2 % 26)
        for k in range(len(addedNumber)):
            addedLetter.append(chr(addedNumber[k] + 65))
        return "".join(addedLetter)


print("Enter the four numbers of the key:")
key = []
for i in range(4):
    key.append(int(input(f"{i+1}: ")))

encrypter = HillEncrypter(key)

print("Press 0 to encrypt a message or 1 to decrypt it")
entry = int(input())

print("Please enter the message")
message = input()

# Encrypting
if entry == 0:
    result = encrypter.encrypt(message)
    print(f"Encrypted message: {result}")
# Decrypting
elif entry == 1:
    result = encrypter.decrypt(message)
    print(f"Decrypted message: {result}")
