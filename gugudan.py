# gugudan.py
def gugudan():
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{i} x {j} = {i * j}")
        print()

if __name__ == "__main__":
    gugudan()
