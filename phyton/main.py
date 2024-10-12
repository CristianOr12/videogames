from random import randint
import os


status_game = True 


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
    
while status_game:
    os.system('clear')
    op = main_menu()
    if op == 1:
        os.system('clear')
        print ("welcome to number race")
        
        key =input ("press any key to go to the main menu")
    if op == 2:
        print ("Game under construction")
        key =input ("press any key to go to the main menu")  
    else:
        print("See 'u leter")   
        key=input("Press any key to exit")  
        break
'''''
dice1 = randint (1,6)
dice2 = randint (1,6)

print(f"dice 1:{dice1}")
print(f"dice 2:{dice2}") 

'''''