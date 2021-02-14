ENQUEUE = 1
DEQUEUE = 2
PRINT = 3


class Stack:
    def __init__(self):
        self.lst = []

    def push(self, data):
        self.lst.append(data)
        
    
    def pop(self):
        self.lst.pop()

    def peek(self):
        return(self.lst[-1])
    
    def put_to_another_stack(self, stack_lst):
        while (self.lst):
            stack_lst.append(self.lst.pop())
    
    
    

class Queue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
    
    def Enqueue(self, data):
        if self.stack_1.lst == [] and self.stack_2.lst == []:
            self.stack_2.push(data)
        elif self.stack_2.lst != []:
            if (self.stack_1.lst != []):
                self.stack_1.put_to_another_stack(self.stack_2.lst) 
            self.stack_2.push(data)

    def Dequeue(self):
        if self.stack_2.lst != []:
            return self.stack_2.lst.pop(0)   
        return self.stack_2.put_to_another_stack(self.stack_1.lst).pop()

    def Print(self):
        if self.stack_1.lst != []:
            print(self.stack_1.peek())
        elif self.stack_2.lst != []:
            print(self.stack_2.lst[0])
    

        

def read_command():
    user_input = input().strip().split(' ')

    try:
        command = int(user_input[0])
    except TypeError:
        command = user_input[0]
    
    if len(user_input) == 1:
        return (command, None)
    try:
        arg = int(user_input[1])
    except ValueError:
        arg = user_input[1]
        
    return command, arg

def main():
    
    my_queue = Queue()

    n_commands = int(input().strip())
    for _ in range(n_commands):
        command, arg = read_command()
        if command == ENQUEUE:
            my_queue.Enqueue(arg)
        elif command == DEQUEUE:
            my_queue.Dequeue()
        elif command == PRINT:
            my_queue.Print()

if __name__ == "__main__":
    main() 