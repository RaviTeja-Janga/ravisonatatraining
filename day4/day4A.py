class Leave:
    def __init__(self,employeeid,name,leaveBalance):
        self.employeeid=employeeid
        self.name=name
        self.leavebalance=leaveBalance
    def display(self):
        return self.employeeid,self.name,self.leavebalance
