print( """ 
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝""")

print("""
░██████╗██╗░░░██╗██████╗░████████╗██████╗░░█████╗░░█████╗░░█████╗░░█████╗░
██╔════╝██║░░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░██║░░░██║██████╦╝░░░██║░░░██████╔╝███████║██║░░╚═╝███████║██║░░██║
░╚═══██╗██║░░░██║██╔══██╗░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔══██║██║░░██║
██████╔╝╚██████╔╝██████╦╝░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░░██║╚█████╔╝
╚═════╝░░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░ """)

x = (int(input("Digite o primeiro número: ")))
y = (int(input("Digite o segundo número: ")))

resultado = x-y
numero_impar = resultado % 2

print('O resultado da sua subtração é: ', resultado)

# função para definir se o número resultante é ímpar ou não. 
if numero_impar == 1:
    print("O valor resultante é um número ímpar")
else:
    print("O valor resultante não é um número ímpar")