print("""
What does this \a do?
I don't know\b sir.
yeah \f dude.
what \r the hell.
\v bro.""")

for i in range(0, 5):
    if i == 3:
        break
    if i == 0:
        continue
    print(i)

def main(a, b):
    try:
        d = a / b
    except:
        print("Nope.")
        return
    return d
    if b == 6:
        raise Nosir("Bad idea.")

main(4, 0)
main(4, 6)
main(8, 23)

var = 32

def new():
    print(var)
def old():
    global var
    var = 23
def cool():
    var = 43

new()
print("Should be 32.")
old()
new()
print("Should be 23")
cool()
new()
print("Should be 23")

f = lambda x: x + 2*x*x
for i in range(0, 7):
    print(f(i))

def crap():
    pass

with open("ex15_sample.txt", "w") as my_file:
    my_file.write("Hey bro.")

def generator():
    for i in range(7):
        yield i**i
g = generator()
for i in g:
    print(i)

program = "m =4 \nn=10 \nprint('Sum = ', m*n)"
exec(program)
