class Payroll:
    def __init__(self):
        self.employee_list = []
    def add(self, employee):
        self.employee_list.append(employee)
    def print(self):
        for i in self.employee_list:
            print(f"{i.full_name}\t ${i.get_salary()}")