while True:

    print(" ")
    num = int(input("Informe um número: "))
    print(" ")
    print(f"Tabuada do {num} ")
    print(" ")

    for i in range (1, 11):
        result = num * i 
        print(f"{num} * {i} = {result}")
        i += 1

    continuar = input("\nDeseja calcular outra tabuad2a (s/n): ")
    if continuar.lower() != "s":
        print("Encerrando o programa.")
        break