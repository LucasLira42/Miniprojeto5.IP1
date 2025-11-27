from person import Person

def add_person(people,name,income,assets):  
    new_person = Person(name,income,assets,0)
    people.append(new_person)
    

def receive_person_data(people):
    name = input("digite aqui seu nome: ")
    income = float(input("digite aqui o seu salário: "))
    assets = float(input("digite aqui o seu patrimônio: "))

    add_person(people,name,income,assets)



 




