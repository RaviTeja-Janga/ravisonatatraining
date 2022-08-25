from day4.day4A import Leave
class RestrictedLeave(Leave):
    def __init__(self,employeeid,name,leaveBalance,dateOfBirth):
        super().__init__(employeeid,name,leaveBalance)
        self.dob=dateOfBirth
    def display_dob(self):
        return self.dob