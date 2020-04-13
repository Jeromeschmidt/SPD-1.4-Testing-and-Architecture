# def FizzBuzz(targetnum):
#     for i in range(targetnum):
#         result = ""
#         if i%3 ==0:
#             result += "Fizz"
#         if i%5 ==0:
#             result += "Buzz"
#         if i%3 > 0 and i%5 > 0:
#             result = i
#
#         print(result)
#
# FizzBuzz(50)

from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.List = LinkedList()

    def push(self, new_item):
        self.List.prepend(new_item)

    def peek(self):
        if self.List.head == None:
            return None
        return self.List.head

    def pop(self):
        top_item = self.peek().data
        self.List.delete(top_item)
        return top_item

stack = Stack()
stack.push(5)
print(stack.peek())
print(stack.pop())
print(stack.peek())
