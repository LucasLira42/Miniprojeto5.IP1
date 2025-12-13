from person import Person
from main import people
from indices import monthly_ratereturn
from indices import monthly_expenses

def add_person(people,name,income,assets):  
    new_person = Person(name,income,assets,0)
    people.append(new_person)
    

def receive_person_data(people):
    name = input("digite aqui seu nome: ")
    income = float(input("digite aqui o seu salário: "))
    assets = float(input("digite aqui o seu patrimônio: "))

    add_person(people,name,income,assets)

def show_person_data(person):
    print(f"{person.name::<20}, salário {person.income:<10.2f}, patrimonio: {person.assets:<13.2f} ")

def show_people_data(person):
    for i in person: print(f"{person.name::<20}, salário {person.income:<10.2f}, patrimonio: {person.assets:<13.2f} ")

def simulate_receipt(person,monthly_ratereturn):
    passive_return = monthly_ratereturn * person.assets
    person.current_account = passive_return + person.income

def simulate_expenses(person,monthly_expenses):
    living_expenses = max({monthly_expenses["moradia"[0]]},{monthly_expenses["moradia"[1]]}*{person.income})

    if person.current_account > 0:
        person.current_account = person.current_account - living_expenses
    else:
        person.current_account = person.current_account - {monthly_expenses["moradia"[0]]}
     
    #eu tenho que colocar para cada chave do dicionário de gastos? 

    person.assests = person.assets + person.current_account
    person.current_account = 0
    

def simulate_month_people(people, monthly_ratereturn,monthly_expenses):
    
    for i in people: 
     simulate_receipt(i,monthly_ratereturn,monthly_expenses) 
     simulate_expenses(i,monthly_expenses) 




    

 




