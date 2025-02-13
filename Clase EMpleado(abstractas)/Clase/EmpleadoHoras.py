from Empleado import Empleado

class EmpleadoHoras(Empleado):
    def __init__(self, first_name, last_name, work_hours, rate):
        super().__init__(first_name, last_name)
        self.work_hours = work_hours
        self.rate = rate
    

    def get_salary(self):
        return self.work_hours * self.rate