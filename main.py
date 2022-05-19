# scripted by Vaimsamay 
# design credits : vaimpier ritik 
# Norification for doing constant work ! 
# Cybok Hackers
# Cybok Wars 


# -----------------------imports 
try:
   from os import system
   from time import sleep
   from gtts import gTTS
   from plyer import notification
   from colorama import Fore
   import os,name
   import sys
except Exception as samay:
    try:
       _ = system('pip install gtts')
       _ = system('pip install plyer')
       _ = system('pip install colorama')
    except:
        print('\n')
        print(r+"└─"+w+"\033[1;37mPlease Check Your Internet Connection !  ")
        print('\n')
        sleep(1.9)
        sys.exit()


#-----------------------------Colors

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"

# ----------------requirements installation ! 


def makemkdir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
makemkdir('Config')


#-------------------------------------banner

logo = """\033[1;37m

\033[1;37m[!] \033[1;31mThis is use for Notification Maker, You can Unlimitedly Edit !!! BYE :_)
\033[1;37m
┌-=============================   -   
=      \033[1;31m . ┌──────── \033[1;37mVaim-Samay    -   
=  \033[1;31m .┌───  \033[1;37mB-Hat Samay            -   \033[34m[✔]     https://github.com/samay825        [✔]
\033[1;37m=    Notificaton-maker - Pro          -   \033[34m[✔]            Version 2.0                 [✔]
\033[1;37m= \033[1;31m . └──── \033[1;37mBY Samay               -   \033[91m[X] Please Don't Use For illegal Activity  [X]
\033[1;37m= \033[1;31m .     └─── \033[1;37mVERSION 2.0         -
\033[1;37m└-=============================   -

\033[1;31m    
Disclaimer: \033[1;32mthis tool is designed for Prank
	    testing in an authorized simulated cyberattack
	    Attacking targets without prior mutual consent
            is illegal!                                                               
\033[1;37m                                    
\033[97m """

#--------------------------About me function ! 
def bye():
	os.system("clear")
	banner()
	string = """ 
	\033[1;37mDeveloper  \033[1;34m: \033[1;31mVAIM-SAMAY

	\033[1;37mGithub     \033[1;34m: \033[1;31msamay825 & vaimpier_ritik

	\033[1;37mInstagram  \033[1;34m: \033[1;31mcyboksamay & vaimpier_ritik

	\033[1;37mE-mail     \033[1;34m: \033[1;31mcybokhackers@gmail.com
	"""
	for letter in string:
	  sleep(0.01) 
	  sys.stdout.write(letter)
	  sys.stdout.flush()
	print("\n")

#-------------------------------------banner and tiny functions 
def funcmain(value):
    with open('Config/vaimsamay.txt','r') as samay:
        data = samay.readlines()
    samay_database = {}
    for i in data:
        cer = i.split('\t')
        samay_database[cer[0]] = cer[1]
    split_keys_database = {x.translate({32:None}) :y
       for x,y in samay_database.items()}
    return split_keys_database[value]
#--------------------------------------Runfile 

def runfile():
    with open('index.txt','r') as f:
        data = f.read()
    return data

# --------------------------------------system clear try for windows exceution ! 
def systemclear():
    if os.name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')



def banner():
    print(logo)

def space():
    print('\n')

def options():
    systemclear()
    banner()
    space()
    print(r+"└─"+w+"\033[1;37m[ 1 ] Notification Maker : ")
    print(r+"└─"+w+"\033[1;37m[ 2 ] Update : ")
    print(r+"└─"+w+"\033[1;37m[ 3 ] About me : ")
    print(r+"└─"+w+"\033[1;37m[ 4 ] Exit : ")
    space()
options()

#-------------------------------- object oriented programming ! 

class Vrushabh:
    def __init__(self,user_input):   
        self.user_input = user_input  
    def Options_Function(self):
        systemclear()
        banner()
        try:
            if self.user_input==1:
                space()
                self.title = input(r+"└─"+w+"\033[1;37mEnter Title of Notification :  "+r)
                space()
                try:
                   self.icon = input(r+"└─"+w+"\033[1;37mEnter Image Path to Set in Notification (optional) :  "+r)  
                except:
                    pass
                space()
                print(r+"└─"+w+"\033[1;37mSaving Configs You Made Almost Ready !  ")
                space()
                sleep(2)
                systemclear()
                banner()
                space()
                print(r+"└─"+w+"\033[1;37m[ 1 ] Hindi Girl : ")
                print(r+"└─"+w+"\033[1;37m[ 2 ] English Girl : ")
                print(r+"└─"+w+"\033[1;37m[ 3 ] Marathi Girl : ")
                space()
                try:
                   self.lund = int(input(r+"└─"+w+"\033[1;37mEnter Available Voice Pack Which You Want :  "+r))
                   if self.lund==1:
                       save = funcmain('hindi')
                   elif self.lund==2:
                       save = funcmain('english')
                   else:
                       save = funcmain('marathi')  

                except Exception as vaimsamay:
                    print('\n')
                    print(r+"└─"+w+"\033[1;37mPlease Enter Number not letters fool !  ")
                    print('\n')
                    sleep(1.9)
                    system('python main.py')
                try:
                    self.timehour = int(input(r+"└─"+w+"\033[1;37mEnter Minutes to Remind  :  "+r))
                except Exception as vaimsamaymandirbichari:
                    print('\n')
                    print(r+"└─"+w+"\033[1;37mPlease Enter Number not letters fool !  ")
                    print('\n')
                    sleep(1.9)
                    system('python main.py')
                sum_count = 1
                while True:
                    notification.notify(
                        title=f'{self.title}',
                        message=f'{runfile()}',
                        app_icon=f'{self.icon}',
                        timeout=15,
                     )
                    os.system('mpg123 Config/v.mp3')
                    text_samay = runfile()
                    language = save
                    samayobject = gTTS(text=text_samay ,lang=language ,slow=False)
                    samayobject.save('Config/play.mp3')
                    os.system('mpg123 Config/play.mp3')
                    system('clear')
                    banner()
                    space()
                    print(r+"└─"+w+"Running"+r+g+f" [ "+r+f"{sum_count}"+g+" ]"+w+" Minutes Over See Notification !")
                    space()
                    secs = (self.timehour * 60)
                    sleep(secs)
                    sum_count += 1
                    
            elif self.user_input==2:
                system('python update.py')
            elif self.user_input==3:
                bye()
            else:
                sys.exit()             
        except Exception as vaimsamaymandirbikhari:
            pass
try:
   samay_user_input = int(input(r+"└─"+w+"\033[1;37mEnter Desire Option :  "+r))  
except Exception as vaimsamaymandirbikhari:
    print('\n')
    print(r+"└─"+w+"\033[1;37mPlease Enter number not letters fool !   ")
    print('\n')
    sleep(1.9)
    system('python main.py')
if __name__ == '__main__':
    samay = Vrushabh(samay_user_input)
    samay.Options_Function()

        
    
    

