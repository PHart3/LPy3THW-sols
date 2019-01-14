i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    i= i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

print("New try.")

numbs = []

for i in range(0, 6):
    print(f"At the top i is {i}")
    numbs.append(i)
    i= i + 1
    print("Numbers now: ", numbs)
    print(f"At the bottom i is {i}")

print("Last time.")

new_numbers = []

def new(numb, num, nik):
    print(f"At the top i is {numb}")
    new_numbers.append(numb)
    print("Numbers now: ", new_numbers)    
    if numb + num < nik:
        print(f"At the bottom i is {numb+num}")
        return new(numb + num, num , nik)
    elif numb + num  ==  nik:
        print(f"At the bottom i is {numb+num}")

new(0, 1, 6)
