class Stack:
    stack_list = []
    max_size = 0
    top = 0

    def __init__(self):
        max_size = 20
        self.stack_list = [" "] * max_size
        self.top = -1

    def push(self, perintah):
        self.top += 1
        self.stack_list[self.top] = perintah

    def pop(self):
        temp = self.stack_list[self.top]
        self.top -= 1
        return temp

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def peek_top(self):
        return self.stack_list[self.top]

    def histori(self):
        i = 0
        while self.stack_list:
            # print(self.stack_list[i])
            return self.stack_list[i]


photoshop = Stack()

photoshop.push("Blur")
photoshop.push("Crop")
photoshop.push("Delete")

print(photoshop.pop())
print(photoshop.histori())
print(photoshop.peek_top())
