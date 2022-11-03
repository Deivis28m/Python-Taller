def getArea(radio):
    Pi = 3.1416
    Area = float(radio) ** 2 * Pi
    return Area
    
def getPerimetro(radio):
    Pi = 3.1416
    perimetro = 2 * Pi * float(radio)
    return perimetro

N = int(input(""))
for i in range(N):
    radio = (input(""))
    print(f"Circulo {i+1} : su perimetros es {round(getPerimetro(radio), 2)} y su area es {round(getArea(radio), 2)}") 