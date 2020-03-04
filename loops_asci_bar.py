from time import sleep
import os


for i in range(1,101):

    os.system("cls")
    print(i*"|")
    print(str(i) +"%")
    sleep(0.02)

    if i == 100:
        os.system("cls")
        print("COMPLETE!")





