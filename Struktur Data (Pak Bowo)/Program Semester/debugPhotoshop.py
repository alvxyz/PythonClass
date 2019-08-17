class Stack:
    stack_list = []
    max_size = 0
    top = 0

    def __init__(self):
        max_size = 20
        self.stack_list = [0] * max_size
        self.top = -1

    # def push(self, perintah):
    #     self.top += 1
    #     self.stack_list[self.top] = perintah

    def push(self, perintah):
        # if not self.is_full():
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
        for i in range(0, len(self.stack_list)):
            print(self.stack_list[i])


    def redo(self):
        temp = self.stack_list[self.top + 1]
        self.top += 1
        return temp


photoshop = Stack()

# print(photoshop.top)
photoshop.push(10)
photoshop.push(10)
photoshop.push(10)


print(photoshop.top)

print(photoshop.histori())
# print(len(photoshop.stack_list))
# for i in range(1, 22):
#     print(photoshop.push(str(i)))

# print(photoshop[photoshop.top])

# print(photoshop.pop())
# print(photoshop.histori())
# print(photoshop.peek_top())
