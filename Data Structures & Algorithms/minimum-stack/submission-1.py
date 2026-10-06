class MinStack:

    def __init__(self):
        self.stiva = []
        self.minime = []

    def push(self, val: int) -> None:
        self.stiva.append(val)
        if self.minime:
            self.minime.append(min(val, self.minime[-1]))
        else:
            self.minime.append(val)

    def pop(self) -> None:
        self.stiva.pop()
        self.minime.pop()

    def top(self) -> int:
        return self.stiva[-1]

    def getMin(self) -> int:
        return self.minime[-1]