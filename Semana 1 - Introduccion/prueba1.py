def prueba_1():
    number= int(input("what your number: "))

    if number % 5 == 0 and number % 3 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print(number)

def prueba_2():
    sales = [1000, 1150, 1300, 900, 1600]

    total = 0
    count = 0
    for s in sales:
        total = total + s
        count = count + 1

    average = total / count
    print("total", total)
    print("average", average)
    print("sales above average:" )

    for s in sales:
        if s > average:
            print(s)

def prueba_3():
    valid_months = [
        "january","february","march","april","may","june",
        "july","august","september","october","november","december"
    ]

    months_data = []

    while True:
        month = input("Enter month (or p to terminate): ").strip().lower()

        if month == "p":
            break

        if month not in valid_months:
            print("Invalid month. Enter again.")
            continue

        try:
            sales = int(input(f"Enter sales for {month}: "))
            if sales < 0:
                print("Sales cannot be negative.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
        continue

        months_data.append((month, sales))

    growth = []

    if months_data:
        total = sum(sales for month, sales in months_data)
        average = total / len(months_data)
        print(months_data)
        print(f"total= {total}")
        print(f"average = {average}")

        for i in range(1, len(months_data)):
            prev = months_data[i-1][1]
            curr = months_data[i][1]

            if prev == 0:
                growth = None
            else:
                growth = ((curr - prev) / prev) * 100
            print(f"growth from {months_data[i-1][0]} to {months_data[i][0]} is: {growth}%")
    else:
        print("no data entered")

def prueba_4():
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def prueba_5():
    numeros_usuario = []

    for i in range(1, 6):
        numero = int(input("Pone 5 veces numeros"))
        numeros_usuario.append(numero)

    mayor = numeros_usuario[0]
    menor = numeros_usuario[0]
    total = 0

    for i in numeros_usuario:
        if i > mayor:
            mayor = i
        if i < menor:
            menor = i
        total += i

    promedio = total / len(numeros_usuario)

    print(f"mayor: {mayor}")
    print(f"menor: {menor}")
    print(f"promedio: {promedio}")

def prueba_6():
    text = "Python is powerful and python is simple"
    text = text.lower()
    letras = 0
    espacios = 0
    python = 0
    for char in text:
        if char.isalpha():
            letras += 1
        elif char == " ":
            espacios += 1

    python = text.count("python")

    print(f"letras: {letras}")
    print(f"espacios: {espacios}")
    print(f"python: {python}")    

def prueba_7():
    for i in range(1,6):
        for j in range(i):
            print("*", end="")
        print()

def prueba_8():        
    filas = 5
    for i in range(filas , 0, -1):   #5,4,3,2,1

        for j in range(filas - i):   # espacios 5-5, 5-4, 5-3, 5-2, 5-1
            print(" ", end="")
        for k in range(2 * i - 1):    # estrellas 10-1, 8-1,
            print("*", end="")

        print()

def prueba_9():
    for i in range(1, 11):   #numeros
        for j in range(1, 11):    #numeros que se multiplican
            print(f"{i} x {j} = {i*j}")
        print()

def prueba_10():
    numbers = [3, 7, 2, 9, 4]
    numeros_multi = []

    for i, j in enumerate(numbers):   #enumerate te da el indice (0,1,2,3,4) y el valor de la lista
        numeros_multi.append(j*i)
    print(numeros_multi)

def prueba_11():
    primos = []
    for i in range(2, 51):
        es_primo = True
    
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    print(primos)

