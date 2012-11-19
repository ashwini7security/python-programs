from collections import deque

queue = deque(["Ashu" , "Vikas" , "jyoti"])
print queue
queue.append("lakshay")
queue.append("vivek")
print queue
queue.popleft() #the first to arrive now leave
print queue
