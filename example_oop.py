
class Counter:
    def _init_(self, start: int = 0, step: int = 1) -> None:
        self.value = start
    
    def increment(self):
        self.value += 1

    def current(self) -> int:
        return self.value
    
    def increment_2(self):
        self.value += 2
    

c = Counter(start=5) #creating an object from the Counter class

c1 = Counter(start = 10)
c1.increment()

print(f"{c1.current()}")
print(f"{c.current()}")

c.increment_2()

print(f"{c.current()}")


#-----Session 2 of 00 - Employee Example
class Employee:
    def __init__(self, name : str, base_salary: float) -> None:
        self.name = name
        self.base_salary = base_salary

def cal_bonus(self, performance: float) -> float:
    return self.base_salary * performance


emp = Employee("Alice", 50000.0)

bonus = emp.cal_bonus(1.1)

print(f"Bonus for {emp.name} is {bonus}")



        