
from pessoa import Pessoa
import functions
import indices
def main(): 
 pessoas = []
 opcao = False
 while opcao == False:
        
        print(f"[D]igitar dados de nova pessoa")
        print(f"[M]ostar pessoas cadastradas")
        print(f"[S]air")

        opcao = input("")

        if opcao == "D" or opcao == "d":
            functions.digitar_dados_pessoa(pessoas)
            opcao = False
            

        elif opcao == "M" or opcao == "m":
            functions.mostrar_dados_pessoa(Pessoa)
            opcao = False
            #como fazer a entrada ser oq ele espera?
            
        elif opcao == "I" or opcao =="i":
            function.simular_mes_população(pessoas,indices.taxa_mensal_rendimento,indices.gastos)
            opcao = False
    
        elif opcao == "S" or opcao =="s":
            opcao = True
            print("encerrando...")
            break
        
        else:
            opcao = False
            
if __name__ == "__main__":
        main()




    