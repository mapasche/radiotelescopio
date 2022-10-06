import time

intervalos = 1

print("\n"*3 + "wena como estamos wn??"+ "\n"*2)

texto = "...."
for i in range(len(texto)):
    print(texto[0:i], end="\r")
    time.sleep(intervalos)

print(texto, end="\r")

time.sleep(intervalos)

print("\n")
time.sleep(intervalos)

print("Espero que muy bien mi rey/reina")

time.sleep(intervalos*2)