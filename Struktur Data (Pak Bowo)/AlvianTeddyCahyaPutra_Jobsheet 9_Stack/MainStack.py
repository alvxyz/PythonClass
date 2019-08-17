# a = "ayam gorng tiga rasa".split(" ")
#
# print(a)
#
# stack_list = []
# max_size = 20
# top = -1
#
# for i in range(1, 20):
#     stack_list.add(i)
#
# if len(stack_list) != max_size + 1:
#     top += 1
#     stack_list[top] = i


def function(x):
    print(x)
    print("still in this function")
    return 2 * x


f = function(2)

print()
print(f)
