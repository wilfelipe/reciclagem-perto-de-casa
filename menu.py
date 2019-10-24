menu = 0

def main():
    print("-------------------------------------------------------------------")

    print("                  Reciclagem Perto de Casa")
    print("\n    Para ver qual o local mais perto para você reciclar, digite '1': ")
    print("\n    Para ver todos os locais que você pode reciclar, digite '2': ")
    print("\n    Para você ver quem criou esse projeto, digite '3': " )

    print("-------------------------------------------------------------------")

    choice = int(input("\n Qual a sua escolha? (1,2 ou 3?): "))

    if choice == 1:
        print("Você escolheu a primeira opção!")
        menu = int(input("Se quiser voltar para o menu, digite '1': "))
        if menu == 1:
            main()
    elif choice == 2:
        print("Você escolheu a segunda opção!")
        menu = int(input("Se quiser voltar para o menu, digite '1': "))
        if menu == 1:
            main()
    elif choice == 3:
        print("Você escolheu a terceira opção!")
        menu = int(input("Se quiser voltar para o menu, digite '1': "))
        if menu == 1:
            main()
    else:
        print("Resposta inválida, tende de novo!")
        main()
main()
