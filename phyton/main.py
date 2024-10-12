





from random import randint
import os

status_menu = True 

def main_menu ():
    global status_oposts
    status_opts = True
    print(":::MAIN MENU:::")
    print("[1]. Start game") 
    print("[2]. help")
    print("[3]. Exit")
    
    while status_opts:
         opt = int (input("Press any option: ")) 
         if opt < 1 or opt >3:
             print ("error.press any option between 1 and 3")
         else:
             status_opts = False
    
    return opt
    
while status_menu:
    os.system('clear')
    op = main_menu()
    if op == 1:
        os.system('clear')
        print ("welcome to number race")
        
        players = int(input("press number of players [1:4]"))
        print("level menu ")
        print("[1] Basic")
        print("[2] Intermediante")
        print("[3] Adnance")
        print("[4] Expert")
        opt = int(input("press any option"))
        
        if opt ==1:
            pos=20
        elif opt ==3:
            pos=30  
        elif opt ==3:
            pos=50 
        else:
            pos=100 
            
        #start game 
        status_game =True
        roll_count=0
        roll_acum=0
        while status_game: 
            key = input("Presione una tecla para tirar dados")
        
            dice1 = randint (1,6)
            dice2 = randint (1,6)

            print(f"dice 1:{dice1}")
            print(f"dice 2:{dice2}")
            total = dice1 + dice2
            print(f"Total: {total}")
        
        
        
            roll_count += 1 
            roll_acum += total
            print(f"total roll:{total}")
        
            if roll_count >= pos:
              print("GANASTE")
              status_game=False
            os.system('pause')
        print("INFO")
        print(f"TOTAL ROLLS: {roll_count}")
        print(f"TOTAL DICES: {roll_acum}")

        
        key =input ("press any key to go to the main menu")
    if op == 2:
        print ("Game under construction")
        key =input ("press any key to go to the main menu")  
    else:
        print("See 'u leter")   
        key=input("Press any key to exit")  
        break
