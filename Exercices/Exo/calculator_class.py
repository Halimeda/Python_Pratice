class Calculator:

    def __init__(self, initial_value):
        self.result = initial_value

    def add(self, value):
        self.result += value
        return(self.result)
    
    def sub(self, value):
        self.result -= value
        return(self.result)

    def mult(self, value):
        self.result *= value
        return(self.result)
    
    def div(self, value):
        self.result /= value
        return(self.result)
    
    def reset(self):
        self.result = 0
        return(self.result)

calc = Calculator(0)
print(calc.add(15))
print(calc.sub(3))
print(calc.reset())
print(calc.add(15))
print(calc.div(5))
print(calc.mult(3))