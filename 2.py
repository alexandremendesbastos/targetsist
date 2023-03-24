numero = int(input("Digite um número: "))
a, b, c, fib = 0, 1, 0, 0

while c <= numero:
    if c == numero:
        fib = 1
    a, b = b, c
    c = a + b

if fib == 1:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
