class MinStack:

    def __init__(self):
        stack=[]
        self.stack=stack
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or self.stack[-1]<=self.minstack[-1]:
            self.minstack.append(val)
        
        


        

    def pop(self) -> None:
        if self.minstack[-1]==self.stack[-1]:
            self.minstack.pop()
            self.stack.pop()
        else:
            self.stack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

        
