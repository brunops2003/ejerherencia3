from clases.herencia1.taxi import Taxi 
from clases.herencia1.auto_particular import Autoparticular
def main(): 
    coche = Taxi("123-GTO","Versa",1000,"123-a") 
    print(coche) 
    coche.encender() 
    coche.subirPasajeros() 
    coche.acelerar() 
    coche.frenar() 
    coche.cobrarCuota() 

    ap = Autoparticular("123","Bruno",15,"volvo","plata","987-G")
    print(ap)
    ap.subirseAuto()
    ap.arrancarAuto()
    ap.llegarDestino()
    

if __name__ == '__main__': 
    main()