from array_deque import ArrayDeque
from my_linked_list import LinkedList
from my_stack import Stack
from my_queue import Queue

print("\nTESTING LINKED_LIST\n")

lis = LinkedList()
lis.push_back(3)
lis.push_back(1)
lis.push_back(6)
lis.push_back(9)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
lis.push_front(11)
lis.push_front(16)
lis.push_front(13)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print(lis.pop_back())
print(lis.pop_back())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_back())
print(lis.pop_front()) # none
print("container of size: " + str(lis.get_size()) + ":")
print(lis)


print("\nTESTING QUEUE\n")

queue = Queue()
queue.add(2)
queue.add(4)
queue.add(7)
print("the data structure is of size: " + str(queue.get_size()))
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
print("the data structure is of size: " + str(queue.get_size()))

print("\nTESTING STACK\n")

stack = Stack()
stack.push(2)
stack.push(4)
stack.push(7)
print("the data structure is of size: " + str(stack.get_size()))
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("the data structure is of size: " + str(stack.get_size()))
