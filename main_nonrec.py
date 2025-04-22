from pprint import pprint

class BuildTree:
    def __init__(self, root, height):
        self.root = root
        self.height = height
        self.tree = {}

    def build(self):
        if not isinstance(self.root, int):
            raise TypeError("Корень дерева должен быть целым числом.")
        if not isinstance(self.height, int) or self.height <= 0:
            raise TypeError("Высота дерева должна быть положительным целым числом.")
        
        count = 0
        self.tree[self.root] = {"left": {}, "right": {}}
        queue = [(self.root, self.tree[self.root])]

        while count < 2**self.height - 1:
            current_node, current_dict = queue.pop(0)

            left_child = current_node * 3
            right_child = current_node + 4

            if count * 2 + 1 < 2**self.height - 1:
                current_dict["left"] = {left_child: {"left": {}, "right": {}}}
                queue.append((left_child, current_dict["left"][left_child]))

            if count * 2 + 2 < 2**self.height - 1:
                current_dict["right"] = {right_child: {"left": {}, "right": {}}}
                queue.append((right_child, current_dict["right"][right_child]))

            count += 1

        return self.tree

try:
    a = BuildTree("efef", 2)
    tree = a.build()
except TypeError as e:
    print(f"Ошибка: {e}")



