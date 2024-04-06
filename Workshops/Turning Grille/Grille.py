from typing import List


class TurningGrilleEncrypter:
    matrix: List[List[str]] = []

    def __init__(self, matrix: List[List[str]]) -> None:
        if not matrix:
            raise ValueError("Matrix must not be empty")

        for i in range(len(matrix)):
            if len(matrix[i]) != len(matrix):
                raise ValueError("Matrix must be square")

        self.matrix = matrix

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


with open("Workshops/Turning Grille/Grille.txt") as f:
    grille = [list(line.strip()) for line in f]

encrypter = TurningGrilleEncrypter(grille)
