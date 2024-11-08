while(True):
   

    mSel = int(input("Ingrese el numero de mes del 1 al 12 "))
    mDia =  int(input("Ingrese el numero de dia del 1 al 31 "))

    if (mSel>=1 and mSel<=12) and (mDia >= 1 and mDia <= 31):
        break
    else:
        print("el mes (1-12) o el dia (1-31) estan incorrectos")

meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
signo = ["aries","tauro","geminis","cancer","leo","virgo","libra","Escorpio","Sagitario","Capricornio","acuario ","piscis"]

match mSel:
    case 1:
        sodiacal = signo[9] if (mDia<=18) else signo[10]
    case 2:
        sodiacal = signo[10] if (mDia<=17) else signo[11]
    case 3:
        sodiacal = signo[11] if (mDia<=20) else signo[0]
    case 4:
        sodiacal = signo[0] if (mDia<=19) else signo[1]
    case 5:
        sodiacal = signo[1] if (mDia<=20) else signo[2]
    case 6:
        sodiacal = signo[2] if (mDia<=20) else signo[3]
    case 7:
        sodiacal = signo[3] if (mDia<=22) else signo[4]
    case 8:
        sodiacal = signo[4] if (mDia<=22) else signo[5]
    case 9:
        sodiacal = signo[5] if (mDia<=22) else signo[6]
    case 10:
        sodiacal = signo[6] if (mDia<=22) else signo[7]
    case 11:
        sodiacal = signo[7] if (mDia<=21) else signo[8]
    case 12:
        sodiacal = signo[8] if (mDia<=21) else signo[9]

print(f"El dia = {mDia} del mes {meses[mSel-1]} y el signo es {sodiacal}")