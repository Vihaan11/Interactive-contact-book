print("""_________                __                 __    ___.                  __     ___.           .____    .__      ____   ____                     
\_   ___ \  ____   _____/  |______    _____/  |_  \_ |__   ____   ____ |  | __ \_ |__ ___.__. |    |   |__|__  _\   \ /   /__.__._____    ______
/    \  \/ /  _ \ /    \   __\__  \ _/ ___\   __\  | __ \ /  _ \ /  _ \|  |/ /  | __ <   |  | |    |   |  \  \/ /\   Y   <   |  |\__  \  /  ___/
\     \___(  <_> )   |  \  |  / __ \\  \___|  |    | \_\ (  <_> |  <_> )    <   | \_\ \___  | |    |___|  |\   /  \     / \___  | / __ \_\___ \ 
 \______  /\____/|___|  /__| (____  /\___  >__|    |___  /\____/ \____/|__|_ \  |___  / ____| |_______ \__| \_/    \___/  / ____|(____  /____  >
        \/            \/          \/     \/            \/                   \/      \/\/              \/                  \/          \/     \/ """)

contact=[]
numbers=[]
def add_contact(name, number):
   if number in numbers:
      print("\nSorry! The number for the contact is already used!")
   else:
      contact.append(name)
      numbers.append(number)
      print("\nDone!")


def del_contact(contact_to_del):
   index_no = -1
   if contact_to_del in contact:   
      for i in contact:
         index_no += 1
         
         if i == contact_to_del:
            contact.pop(index_no)
            numbers.pop(index_no)
            print("\nDone!!")
            break
            
         elif (index_no+1) > len(contact):
            print("\nContact not found")
            break
            
         else:
            continue
   else:
      print("\nContact not found")
def search(mycontact):
   
   if mycontact in contact:
      index_no0 = -1
      for v in contact:
         index_no0 += 1
         if v==mycontact:
            print(f"\nContact name: {v}\nContact number: {numbers[index_no0]}")
   else:
      print("Contact not found")


def edit(mycontact):

   # name0=input("New Contact name: ")
   # number0=input("New Contact number: ")
   # try:
   #    contact[index_no1]=name0.upper()
   #    numbers[index_no1]=number0
   #    print("Done!")
   # except:
   #    print("Error!")


   # if number in numbers:
   #    print("\nSorry! The number for the contact is already used!")
   # else:
   #    contact.append(name)
   #    numbers.append(number)
   #    print("\nDone!")
   
   num_of_contact=0
   if mycontact in contact:
      index_no1 = -1
      for v in contact:
         index_no1 += 1
         if v==mycontact:
            print(f"\nContact name: {v}\nContact number: {numbers[index_no1]}")
            num_of_contact += 1
   else:
      print("\nContact not found")
   
   if num_of_contact > 1:
      to_edit = input("\nThere is more than 1 contact(s) here. Please enter the contact number of the one you want to edit: ")
      
      index_no01 = -1
      for v in numbers:
         index_no01 += 1
         if v==to_edit:
            name0=input("\nNew Contact name: ")
            number0=input("New Contact number: ")
            try:
               if number0 in numbers:
                  print("\nSorry! The number for the contact is already used!")
               else:
                  contact[index_no01]=name0.upper()
                  numbers[index_no01]=number0
                  print("\nDone!")
            except:
               print("\nError!")
   else:
      if mycontact in contact:
         index_no01 = -1
         for v in contact:
            index_no01 += 1
            if v==mycontact:
               name0=input("\nNew Contact name: ")
               number0=input("New Contact number: ")
               try:
                  if number0 in numbers:
                     print("\nSorry! The number for the contact is already used!")
                  else:
                     contact[index_no01]=name0.upper()
                     numbers[index_no01]=number0
                     print("\nDone!")
               except:
                  print("\nError!")
      

List_of_cmds="List of commands:\n\t1 : add a contact to contact book\n\t2 : delete an existing contact\n\t3 : search for an existing contact\n\t4 : edit an existing contact\n\t5 : view the contact book\n\tquit : quit the app\n\thelp : get this list of commands"
print(List_of_cmds)

while True:
   cmd=input("\n\n>>")
   if cmd=="1":
      print("\nAdd contact")
      name1=input("\nContact name: ")
      number1=input("Contact number: ")
      add_contact(name1.upper(),number1)
   elif cmd=="2":
      print("\nDelete contact")
      if len(contact)<=0:
         print("The contact book is empty")
      else:
         name2=input("\nContact name: ")
         del_contact(name2.upper())
   elif cmd=="3":
      print("\nSearch")
      if len(contact)<=0:
         print("The contact book is empty")
      else:
         name3=input("\nContact name: ")
         search(name3.upper())
   elif cmd=="4":
      print("\nEdit contact")
      if len(contact)<=0:
         print("The contact book is empty")
      else:
         name4=input("\nContact name: ")
         edit(name4.upper())
   elif cmd=="5":
      print("\nView Contact Book")
      if len(contact)<=0:
         print("The contact book is empty")
      else:
         index_no2=-1
         for v in contact:
            index_no2 += 1
            print(f"\nContact name: {v}\nContact number: {numbers[index_no2]}")
   elif cmd=="quit":
      break
   elif cmd=="help":
      print(List_of_cmds)
   else:
      print("\nCommand not found")
