class Employee:
    def __init__(self, fullname, position) -> None:
        self.fullname = fullname
        self.position = position
    def sayhi(self):
        return 'Hello' + self.fullname
    def tell(self)
        return 'I am' + self.position
    
worker = Employee('Nguyen Van A', 'Leader')
worker2 = Employee('Nguyen Van B', 'Dev')
print(worker.sayhi())
print(worker2.sayhi())
print(worker2.tell())