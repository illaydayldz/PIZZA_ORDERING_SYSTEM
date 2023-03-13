import csv
import datetime


# PİZZA ÜST SINIFI

class Pizza:
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

# PİZZA ALT SINIFLARI  

class KlasikPizza(Pizza):
    def __init__(self, cost, description):
        self.id = 1
        self.cost = cost 
        self.description = description

pizzaKlasik = KlasikPizza(110,"Pizza sosu, Mozerella Peyniri, Sucuk, Sosis, Mısır, Siyah Zeytin")


class MargaritaPizza(Pizza):
     def __init__(self,cost,description):
        self.id = 2
        self.cost = cost
        self.description = description

pizzaMargarita = MargaritaPizza(90,"Pizza sosu, Mozerella Peyniri")


class TurkPizza(Pizza):
    def __init__(self, cost, description):
        self.id = 3
        self.cost = cost
        self.description = description

pizzaTurk = TurkPizza(120,"Pizza sosu, Mozerella Peyniri, Pastırma, Kavurma, Sucuk, Közlenmiş Biber, Soğan")


class SadePizza(Pizza):
     def __init__(self, cost,description):
        self.id = 4
        self.cost = cost
        self.description = description

pizzaSade = SadePizza(100,"Pizza sosu, Mozerella Peyniri, Fesleğen, Beyaz Peynir")

pizzaList = [pizzaKlasik, pizzaMargarita, pizzaTurk, pizzaSade]

# DECARATOR ÜST SINIFI

class Decarator:
    def get_cost(self):
        return self.cost
    
    def get_name(self):
        return self.name
    

    
# DECARATOR ALT SINIFLARI 

class Zeytin(Decarator):
    
    def __init__(self, cost):
        self.id = 11
        self.name = "Zeytin"
        self.cost = cost

dZeytin = Zeytin(14)



class Mantar(Decarator):
    
    def __init__(self, cost):
        self.id = 12
        self.name = "Mantar"
        self.cost = cost
        
dMantar= Mantar(13)


class KeciPeyniri(Decarator):
    
    def __init__(self, cost):
        self.id = 13
        self.name = "Keçi Peyniri"
        self.cost = cost
        
dKeciPeyniri = KeciPeyniri(15)


class Et(Decarator):
    
    def __init__(self, cost):
        self.id = 14
        self.name = "Et"
        self.cost = cost
        
dEt = Et(20)


class Sogan(Decarator):
    
    def __init__(self, cost):
        self.id = 15
        self.name = "Soğan"
        self.cost = cost
        
dSogan = Sogan(10)


class Misir(Decarator):
    
    def __init__(self, cost):
        self.id = 16
        self.name = "Mısır"
        self.cost = cost
        
dMisir = Misir(14)

toppingList = [dZeytin, dMantar, dKeciPeyniri, dEt, dSogan, dMisir]
toppingMenu = []

# MENÜ 

with open("Menu.txt", encoding="utf-8") as menu:
    for row in menu:
        rowid = row.split(":")[0]
        pizza = None

        for piz in pizzaList:
            if piz.id == int(rowid):
                pizza = piz
                break
            else:
                pizza = None

        if pizza != None:
            pizzaRow = f"{row.strip()} | {pizza.get_cost()} TL | {pizza.get_description()}"
            print(pizzaRow)
        else:
            toppingMenu.append(row.strip())
            

secim = int(input("Pizza alt tabanı için tuşlama yapınız\n"))

selectedPizza = [piz for piz in pizzaList if piz.id == secim]
selectedTopping = None
if selectedPizza:
    for topping in toppingMenu:
        print(topping)

    secim = int(input("Eklemek istediğiniz sos var ise tekrar tuşlama yapınız\n"))
    selectedTopping = [top for top in toppingList if top.id == secim]
    
# SİPARİŞ TUTARI HESAPLAMA
 
    pizza_cost_calculate = (selectedPizza[0].get_cost())
    topping_cost_calculate = (selectedTopping[0].get_cost())
    Calculate = (pizza_cost_calculate + topping_cost_calculate)


    print("---------------------------------SİPARİŞ BİLGİLERİ---------------------------------------")
    name = input("AD : ")
    surname = input("SOYAD : ")
    TCID = input("TC : ")
    k_no = input("Kredi Kartı Numarası : ")
    k_password = input("Kredi Kartı Şifresi : ")
    time_of_order = datetime.datetime.now()
    with open('orders.csv', mode='a', encoding="utf-8") as orders_writer:
        writer = csv.writer(orders_writer, delimiter= ",")
        writer.writerow([time_of_order, name,surname,TCID,k_no,k_password, selectedPizza[0].id, selectedPizza[0].get_description(), selectedPizza[0].get_cost(), selectedTopping[0].id, selectedTopping[0].get_name()])
    print("SİPARİŞ TUTARI : " , Calculate)
    print("SİPARİŞİNİZ TAMAMLANDI" )
    
else:
    print("\nYanlış tuşlama yaptınız lütfen tekrar deneyiniz")

