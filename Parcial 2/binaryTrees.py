class BinaryTreeNode:
    """Nodo de un árbol binario de búsqueda."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Implementación de un árbol binario de búsqueda."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserta un valor en el árbol."""
        if self.root is None:
            self.root = BinaryTreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BinaryTreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def find(self, value) -> bool:
        """Verifica si un valor existe en el árbol."""
        return self._find_recursive(self.root, value)

    def _find_recursive(self, node, value) -> bool:
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._find_recursive(node.left, value)
        else:
            return self._find_recursive(node.right, value)

    def in_order_traversal(self) -> list:
        """Devuelve una lista con los valores en orden in-order."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)

    def height(self) -> int:
        """Calcula la altura del árbol."""
        return self._height_recursive(self.root)

    def _height_recursive(self, node) -> int:
        if node is None:
            return -1
        return max(self._height_recursive(node.left), self._height_recursive(node.right)) + 1