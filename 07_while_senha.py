i=1
while i<=3:

    user = input("Informe seu usuário. ")
    senha = input ("Informe a senha. ")

    if user != "Gisele" or senha != "123":
        i += 1
        print("Usuário ou senha incorretos!")
        print (" ")
    else:
        print (" ")
        print(f"Bem Vindo, {user}!")
        break

else:
    print("Você excedeu todas as tentativas")