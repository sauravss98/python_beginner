class Main:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def employeeDetail(self):
        return self.id,self.name

    def employeecheck(self):
        if self.id>5000:
            return "Valid employee"
        else:
            return "Invalid employee"

class Secondary(Main):
    def collectData(self):
        print("End")

emp1=Secondary("employee1",9000)
print(emp1.employeeDetail(),emp1.employeecheck())
emp2=Secondary("employee2",33)
print(emp2.employeeDetail(),emp2.employeecheck())
emp2.collectData()
