
from person import Person
from functions import receive_person_data
from functions import show_person_data
def main(): 
 people = []
 opcao = False
 while opcao == False:
        
        print(f"[D]igitar dados de nova pessoa")
        print(f"[M]ostar pessoas cadastradas")
        print(f"[S]air")

        opcao = input("")

        if opcao == "D" or opcao == "d":
            receive_person_data()
            opcao = True
            

        elif opcao == "M" or opcao == "m":
            show_person_data(input("digite aqui o nome da pessoa"))
            opcao = True
            print("mostrando pessoas")
        
        elif opcao == "S" or opcao =="s":
            opcao = True
            print("encerrando...")
            break
        
        else:
            opcao = False
            
if __name__ == "__main__":
        main()
#criar um dicionário com os gastos minimos e necessarios(que serão tuplas) associados a chaves que serão as áreas



    