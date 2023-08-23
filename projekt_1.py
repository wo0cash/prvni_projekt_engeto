"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lukasz Orszulik
email: luki93@seznam.cz
discord: Lukasz Orszulik, wo0cash
"""
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
user_list = ["bob", "ann", "mike", "liz"]
passw_list = ["123", "pass123", "password123", "pass123"]
sep_line = "-" * 40

user = "bob" #input("Zadej přihlašovací jméno: ")
passw = "123" #input("Zadej heslo: ")
print(sep_line)

#smyčka - kontrola údajů která nás pustí dál
#!!! upravit jméno a heslo musí patřit k sobě
if user in user_list and passw in passw_list:
    print("Welcome to the app,", user.capitalize(), "\nWe have 3 texts to be analyzed.")   
    print(sep_line)
    text_number = input("Enter a number btw. 1 and 3 to select: ") #vložení čísla textu
    print(sep_line)
    if not text_number.isdigit():
        print("Must type digits only! Terminating the program..")
    elif int(text_number) > 3 and int(text_number) == 0:
        print("Number must be between 1 and 3! Terminating the program..")
    else:
        ch_text = texts[int(text_number) - 1]
        text_list = ch_text.split() #vytvoří seznam
        #print(text_list) - jenom ať vím že utvořil list
        x_words = 0 
        #Počet slov
        for word in text_list:  #pro každé slovo spočítej slovo = slovo + 1
            x_words += 1
        print("There are", x_words, "words in selected text.")
        #Počet slov začínajících velkým písmenem
        x_title = 0
        for title_word in text_list:
            if title_word.istitle():
                x_title += 1
        print("There is", x_title, "titlecase word.") if x_title == 1 else print("There are", x_title, "titlecase words.") #ternární operátor pro jednoduchost
        #Počet slov kapitálkami
        x_up = 0
        for up_word in text_list:
            if up_word.isupper() and up_word.isalpha():
                x_up += 1
        print("There is", x_up, "uppercase word.") if x_up == 1 else print("There are", x_up, "uppercase words.") #ternární operátor pro jednoduchost
        #Počet slov z malého písmena
        x_low = 0
        for low_word in text_list:
            if low_word.islower():
                x_low += 1
        print("There is", x_low, "lowercase word.") if x_low == 1 else print("There are", x_low, "lowercase words.") #ternární operátor pro jednoduchost
        #Počet numerických hodnot
        #spočítat všechny čísla v textu
        x_num = 0
        x_sum = 0
        for number in text_list:
            if number.isdigit():
                x_num += 1
                x_sum += int(number)  
        
        print("There is", x_num, "numeric string") if x_num == 1 else print("There are", x_num, "numeric strings.") #ternární operátor pro jednoduchost
        print("The sum of all the numbers is", x_sum) if x_sum > 0 else print("There are no numbers") #ternární operátor pro jednoduchost
        print(sep_line)
        #graf na četnost různých delek slov v textu
        #TODO spočítat stejně dlouhá písma
        #TODO asi while? tzn.-> smyčka kdy bude vyhledávat prvně slova s jedním znakem a sečte je pak se vráti a bude sčítat slova o dvou znacích
        print("LEN | OCCURENCES | NR.")
        print(sep_line)
        len_list = []
        for word in text_list:
            if word in text_list:
            len_list.append(len(word))
        len_list.sort()    
        pocet = 0

        for lenword in len_list:
            if pocet + 1 in len_list:
                print(pocet + 1, "|", "*" * (len_list.count(pocet + 1) + 1), "|", len_list.count(pocet + 1))
            pocet += 1    
                
               
       
        

            
            
            
        





        

        

                   
        

else:
    print("unregistered user, terminating the program..")