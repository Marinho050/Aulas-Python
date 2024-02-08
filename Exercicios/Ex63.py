# Ex63

from time import sleep

def tabuada(num):
    print(f"TABUADA DO {num}")
    sleep(1)
    print("~"*20)
    for c in range(1, 11):
        print(f"{num} x {c} = {num * c}")
        sleep(0.3)
    print("~" * 20)
    sleep(2)


tabuada(10)
tabuada(5)