from day4.day4A import Leave
class BasketOfLeave(Leave):
    def __init__(self,employeeid,name,leaveBalance,applyingleave):
        super().__init__(employeeid,name,leaveBalance)
        self.Applyingleave=applyingleave
    def displayleave(self):
        return self.leaveBalance-self.applyingleave
