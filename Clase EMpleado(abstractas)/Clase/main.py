from EmpleadoHoras import EmpleadoHoras as eh
from EmpleadoTiempoCompleto import EmpleadoTiempoCompleto as et
from Payroll import Payroll

payroll = Payroll()

payroll.add(et("john","dow",6000))

payroll.add(et("jane","dow",6500))
payroll.add(eh("jennifer","smith",200,50))
payroll.add(eh("david","wilson",150,100))
payroll.print()
