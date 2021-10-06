# Link to the problem: https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.mem = []
        self.currentMin = float('inf')
        self.prevMins = []

    def push(self, val: int) -> None:
        self.mem.append(val)
        if val <= self.currentMin:
            self.prevMins.append(self.currentMin)
            self.currentMin = val

    def pop(self) -> None:
        if self.mem[-1] == self.currentMin:
            self.currentMin = self.prevMins.pop()
        self.mem.pop()

    def top(self) -> int:
        return self.mem[-1]

    def getMin(self) -> int:
        return self.currentMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
