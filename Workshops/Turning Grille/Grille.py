from typing import List


class TurningGrilleEncrypter:
    matrix: List[List[str]] = []

    def __init__(self, matrix: List[List[str]]) -> None:
        if not matrix:
            raise ValueError("Matrix must not be empty")

        if not all(len(row) == len(matrix) for row in matrix):
            raise ValueError("Matrix must be square")

        self.matrix = matrix

        sum_matrix = [[0] * len(matrix) for _ in range(len(matrix))]
        for side in range(4):
            temp_matrix = self.get_rotated_matrix(side)
            sum_matrix = [
                [sum(x) for x in zip(*rows)] for rows in zip(sum_matrix, temp_matrix)
            ]

        if len(sum_matrix) % 2 != 0:
            sum_matrix[len(sum_matrix) // 2][len(sum_matrix) // 2] = 1

        if any(cell > 1 for row in sum_matrix for cell in row):
            raise ValueError(
                "Grille must not have hole overlaps (except for the center)"
            )

    def get_rotated_matrix(
        self, times: int = 1, clockwise: bool = True
    ) -> List[List[str]]:
        times %= 4
        rotated_matrix = self.matrix
        for _ in range(times):
            if clockwise:
                rotated_matrix = list(zip(*rotated_matrix[::-1]))
            else:
                rotated_matrix = list(zip(*rotated_matrix))[::-1]

        return rotated_matrix

    def encrypt_message(self, message: str, clockwise: bool = True) -> str:
        message_list = list(filter(str.isalpha, message.upper()))
        if len(message_list) > (len(self.matrix) ** 2):
            raise ValueError("Message is bigger than the grille")

        message_list.extend(["X"] * (len(self.matrix) ** 2 - len(message)))

        encrypted_message = [["X"] * len(self.matrix) for _ in range(len(self.matrix))]
        for side in range(4):
            rotated_matrix = self.get_rotated_matrix(side, clockwise)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    if rotated_matrix[i][j] == 1:
                        encrypted_message[i][j] = message_list.pop(0)

        return " ".join(["".join(row) for row in encrypted_message])

    def decrypt_message(self, message: str, clockwise: bool = True) -> str:
        message_list = list(filter(str.isalpha, message.upper()))
        if len(message_list) > (len(self.matrix) ** 2):
            raise ValueError("Message is bigger than the grille")

        message_matrix = [
            list(message_list[i : i + len(self.matrix)])
            for i in range(0, len(message_list), len(self.matrix))
        ]

        decrypted_message = []
        for side in range(4):
            rotated_matrix = self.get_rotated_matrix(side, clockwise)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    if rotated_matrix[i][j] == 1:
                        decrypted_message.append(message_matrix[i][j])

        return "".join(decrypted_message)


grille = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]]

encrypter = TurningGrilleEncrypter(grille)

print(encrypter.encrypt_message("JIM ATTACKS AT DAWN", False))

grille = [
    [1, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
]

encrypter = TurningGrilleEncrypter(grille)

print(
    encrypter.decrypt_message(
        "TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM TLHIE I",
        False,
    )
)
