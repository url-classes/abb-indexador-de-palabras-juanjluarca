from typing import Generic, TypeVar, Literal

T = TypeVar("T")


class Node:
    def __init__(self, data, filename):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1  # Número de veces que aparecerá una palabra en cada archivo
        self.files = {filename}  # Nombres de los archivos en los que aparece la palabra

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def hos_children(self) -> Literal["left", "right", "both", "none"]:
        if self.left is None and self.right is None:
            return "none"
        elif self.left is not None and self.right is not None:
            return "both"
        elif self.left is not None and self.right is None:
            return "left"
        elif self.left is None and self.right is not None:
            return "right"

    def __str__(self):
        return str(self.data)
