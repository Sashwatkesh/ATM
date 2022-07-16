#ATM machine made by Shashwat Kesharwani

print(" Welcome to our Bank")
f=1
bal=1000
chance=3
restart= 'y'
while chance != 0:
   p_n= int(input("Enter your pin \n "))
   if p_n ==1234:
       #a=input ('''Enter your choice
       # :- Balance inquary
      # 3 :- Deposite amount
       #4 :- Exit ''')
       while restart not in ('no','NO','n', 'N'):
           print("Enter your choice")
           print("1 :- withdeawl ")
           print ("2 :- Balance inquary")
           print("3 :- Deposite amount")
           print ("4 :- Exit ")
           a=int(input("Enter you choice :- "))
           if a==1:
               amt=int(input("enter the amount you want to withdrawl\n"))
               if amt>bal:
                   print("Insufficent balance")  
                   continue
               else:
                   bal=bal-amt
                   print("your balance is:-\n", bal)
                   continue
           elif a==2:
              print("your balance is\n", bal)
              continue
           elif a==3:
            amt2=int(input("enter the amount you want to diposite\n"))
            bal=bal+amt2
            print("your balance is:-\n", bal)
            continue


           elif a==4:
                print ('Thankyou for banking with us ')
                chance = 0
                break

        
   else:
         print("Wrong password!")
         chance=chance-1

