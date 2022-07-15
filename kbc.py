############################ Kon Banega Crorepati ##########################################
import random
print('\033[1m',"WELCOME TO KON BANEGA CROREPATI",'\033[0m')
Q=["The shape of our milky way galaxy is:",
   "Instrument used to measure the force and velocity of the wind is:",
   "which one of these animals is jawless?",
   "outside the nucleus DNA is found in:",
   "In which year salt satyagraha took place?",
   "In which river has the Hirakund Dam been built?",
   "'POSHAN Maah' is celebrated in which month in India?",
   "Name of the first Atomic Submariene of India?",
   "Name of the first University of India"] 
A=[["1.circular","2.eliptical","3.spiral","4.non of the above","5.life line"],
   ["1.Ameter","2.Anemometer","3.Altimeter","4.Audiometer","5.life line"],
   ["1.shark","2.myxine","3.trygon","4.sphyrna","5.life line"],
   ["1.golgi body","2.Ribosome","3.endoplasmic reticulam","4.Mitochondria","5.life line"],
   ["1.1929","2.1930","3.1931","4.1932","5.life line"],
   ["1.mahanadi","2.Godavari","3.cauvery","4.Periyar","5.life line"],
   ["1.August","2.September","3.October","4.November","5.life line"],
   ["1.I.N.S.Chakra","R.N.Sukla","3.V.R.Gill","4.D.B.Mahawar","5.life line"],
   ["1.Nalanda","2.Taxshila","3.Jawahar","4.Dronacharya","5.life line"]] 
choice=["3","2","2","4","2","1","2","1","1"]
life=["1.50-50","2.switch the question","3.audiance pole","4.phone a friend"] 
fifty=[["1.circular","3.spiral"],
       ["4.Audiometer","2.Anemometer"],
       ["4.sphyrna","2.myxine"],
       ["4.mitochondria","2.ribosome"],
       ["1.1929","2.1930"],
       ["4.periyar","1.mahanadi"],
       ["2.September","4.November"],
       ["1.I.N.S.Chakra","4.D.B.Mahawar"],
       ["1.Nalanda","2.Taxshila"]]
l1=0
l2=0
l3=0
l4=0

a=1
while a>0:
    w=random.randint(1,101)
    y=random.randint(1,101)
    x=random.randint(1,101)
    z=random.randint(1,101)
    if w+y+x+z==100:
        break
    else:
        a+=1
R=0
T=0
len=len(Q)
for i in range (len-1):
    R=R+10000
    
    print('\033[32m',"your",i+1,")",f"question for {R} rupees please give answer carefully.",'\033[0m')
    print('\033[33m', Q[i] ,'\033[0m')
    for j in A[i]:
        print('\033[3m', j ,'\033[0m')
    n=input("enter your choice:")
    if (n)==choice[i]:
        print('\033[32m',"CONGRATULATIONS YOU WIN.your answer is right.",'\033[0m')
        print('\033[32m',f"you win {R} rupees.",'\033[0m')
        T=R+T
        print('\033[32m',f"Your total win amount now {T} rupees.",'\033[0m')
        
        
    elif n=="5":
        if l1==1:
            print('\033[35m',"you have already used 50-50 life line.",'\033[0m')
        if l2==1:
            print('\033[35m',"you have already used switch the queston life line.",'\033[0m')
        if l4==1:
            print('\033[35m',"you have already used phone a friend life line.",'\033[0m')
        if l3==1:
            print('\033[35m',"you have already used audience pole life line.",'\033[0m')
        print('\033[31m',"you have given bellow life line. ",'\033[0m')
        for j in life:
            print('\033[36m',j,'\033[0m')
        life_line=int(input("Enter which life line you have choose:"))
        if life_line==1:
            l1+=1
            life.remove("1.50-50")
            for x in fifty[i]:
                print('\033[33m',x,'\033[0m')
            choose=input("Enter your option:")
            if choose==choice[i]:
                print('\033[32m',"CONGRATULATION YOU WIN.your answer is right.",'\033[0m')
                print('\033[32m',f"you win {R} rupees.",'\033[0m')
                T=R+T
                print('\033[32m',f"Your total win amount now {T} rupees.",'\033[0m')
            else:
                print('\033[31m',"YOU LOSE. your answer is wrong.",'\033[0m')   
                if choose!=choice[i]:
                    n=input("you want to game continue yes or no:")
                    if n=="yes":
                        continue
                    else:
                        break
        elif life_line==2:
            l2+=1
            len+=1
            life.remove("2.switch the question")
            print('\033[36m',"you choose switch question so \n your next question is:",'\033[0m')
            print('\033[33m',Q[i+1],'\033[0m')
            del(Q[i+1])
            for y in (A[i+1]):
                print('\033[37m',y,'\033[0m')
            choose=input("enter your option:")
            del(A[i+1])
            if choose==choice[i+1]:
                del(choice[i+1])
                print('\033[32m',"CONGRATULATION YOU WIN.your answer is right.",'\033[0m')
                print('\033[32m',f"you win {R} ruppes.",'\033[0m')
                T=R+T
                print('\033[32m',f"Your total win amount now {T} rupees.",'\033[0m')               
                del(fifty[i+1])
            else:
                print('\033[31m',"YOU LOSE. your answer is wrong.",'\033[0m')
                if choose!=choice[i]:
                    n=input("you want to game continue yes or no:")
                    if n=="yes":
                        continue
                    else:
                        break
        elif life_line==4:
            l4+=1
            life.remove("4.phone a friend")
            print('\033[36m',"your friend tell you option: \n",'\033[0m',A[i][int(choice[i])-1])
            
            choose=input("enter the your option: ")
            if choose==choice[i]:
                
                print('\033[32m',"CONGRATULATION YOU WIN.your answer is right.",'\033[0m')
                print('\033[32m',f"you win {R} ruppes.",'\033[0m')
                T=R+T
                print('\033[32m',f"Your total win amount now {T} rupees.",'\033[0m') 
            else:
                print('\033[31m',"YOU LOSE. your answer is wrong.",'\033[0m')
                if choose!=choice[i]:
                    n=input("you want to game continue yes or no:")
                    if n=="yes":
                        continue
                    else:
                        break
        elif life_line==3:
            l3+=1
            life.remove("3.audiance pole")
            if w+y+x+z==100:
                print('\033[37m',"1.audience call",w,"%",'\033[0m')
                print('\033[37m',"2.audience call",y,"%",'\033[0m')
                print('\033[37m',"3.audience call",x,"%",'\033[0m')
                print('\033[37m',"4.audience call",z,"%",'\033[0m')
            n=input("enter your option:")
            if n==choice[i]:
                print('\033[32m',"CONGRATULATION YOU WIN. your answer is right.",'\033[0m')
                print('\033[32m',f"you win {R} rupees.",'\033[0m')
                T=R+T
                print('\033[32m',f"Your total win amount now {T} rupees.",'\033[0m') 
            else:
                print('\033[31m'," YOU LOSE. your answer is wrong.",'\033[0m')
                if n!=choice[i]:
                    n=input("you want to game continue yes or no:")
                    if n=="yes":
                        continue
                    else:
                        break
    else:
        print('\033[31m',"YOU LOSE.your answer is wrong.",'\033[0m')
        n=input("you want to game continue yes or no:")
        if n=="yes":
            continue
        else:
            break
print('\033[4m',"Congratulations you win",T,"rupees \nThank you for playing  KBC.",'\033[0m')
# 
# 