import functions

def main():
  

    pessoas = []


    laco = 0
    while laco == 0:

        print("[SIMULADOR DE RELAÇÕES DO MERCADO]\n - [d]igitar dados de nova pessoa\n - [m]ostrar pessoas cadastradas\n - [s]air")
        opcao = input("digite aqui: ")

        if opcao == "d":
            print("digitar dados de uma nova pessoa")
            functions.receive_person_data(pessoas)
            laco= 1

        elif opcao == "m":
            print("mostrar pessoas casdastradas")
            laco=1

        elif opcao == "s":
            print("Saindo")
            quit()
            laco = 1

        else:
            print("opção inválida")
            laco = 0
        
#criar um dicionário com os gastos minimos e necessarios(que serão tuplas) associados a chaves que serão as áreas











if __name__ == "__main__":
    main()
    