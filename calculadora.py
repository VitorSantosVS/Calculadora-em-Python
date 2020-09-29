def soma(n1,n2):
    resultado= n1+n2
    return resultado

def multiplicacao(n1,n2):
    resultado= n1*n2
    return resultado

def divisao(n1,n2):
    resultado=n1/n2
    return resultado

def subtracao(n1,n2):
    resultado= n1-n2
    return resultado
def inicio():
    print("------- Calculadora -------")
    x= int(input("Qual opção deseja realizar?\n1. soma \n2. multiplicação \n3. divisão \n4. subtração \nopção: "))
    n1=float(input("Adicione o primeiro numero: "))
    n2=float(input("Adicione o segundo numero: "))

    if(x==1):
        print("O valor da sua soma é: ",soma(n1,n2))
    elif(x==2):
        print("O valor da sua multiplicação é: ",multiplicacao(n1,n2))
    elif(x==3):
        print("O valor da sua divisao é: ",divisao(n1,n2))
    elif(x==4):
        print("O valor da sua subtração é: ",subtracao(n1,n2))
    else:
        print("Opção inválida.")
    z=input("Deseja tentar novamente? [S/N]")
    while(z.upper()=="S"):
        inicio()
    
inicio()
