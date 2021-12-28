class Patterns:

    def print_top_left_triangle(self, size):
        print("*" * size)
        if size > 1:
            self.print_left_triangle(size - 1)

    def print_top_right_triangle(self, size, counter=0):
        print((" " * counter) + ("*" * size))
        if size > 1:
            self.print_right_triangle(size - 1, counter + 1)

    def print_left_triangle(self, size, counter=1):
        print("*" * counter)
        if size > counter:
            self.print_left_triangle(size, counter + 1)

    def print_right_triangle(self, size, counter=1):
        print((" " * (size - 1)) + ("*" * counter))
        if size > 1:
            self.print_right_triangle(size - 1, counter + 1)

    def print_tetragon(self, left, right, counter=0):
        print(("*" * left) + (" " * counter) + ("*" * left))
        if left > 1:
            self.print_tetragon(left - 1, right - 1, counter + 2)
            print(("*" * right) + (" " * counter) + ("*" * right))
