import matplotlib.pyplot as plt

x = [27,              100,         500,            1000,           10000,        100000,           1000000]
y = [4.744529724e-5,  5.292892e-5, 0.000109434127, 0.000182628631, 0.0014934539, 0.01445579528808, 0.01445579528808]
#y2 = [5,6,3,7,8,5,3,10,8,3]


plt.plot(x,y, label = "Tiempo en generar CRC")
#plt.plot(x,y2, label = "Secuencial")
plt.xlabel("Numero de bytes")
plt.ylabel("Tiempo en segundos")
plt.title("Generacion de codigo CRC")
plt.legend()
plt.show()
