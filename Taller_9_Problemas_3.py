def getModulo(vector):
    sum_de_cuadrados= 0
    listaNueva = list(map(int,vector))
    for i in listaNueva:
        sum_de_cuadrados += i**2
    normal = sum_de_cuadrados **0.5
        
    return normal
    
N = int(input(""))
for i in range(N):
    vector = input("").split()
    print(f"la normal del vector {i+1} es {float(getModulo(vector)):.1f}")
