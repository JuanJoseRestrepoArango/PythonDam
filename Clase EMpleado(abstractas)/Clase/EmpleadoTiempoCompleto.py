from Empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):

    def __init__(self, first_name, last_name,salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary