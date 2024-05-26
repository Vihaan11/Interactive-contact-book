print("""_________                __                 __    ___.                  __     ___.           .____    .__      ____   ____                     
\_   ___ \  ____   _____/  |______    _____/  |_  \_ |__   ____   ____ |  | __ \_ |__ ___.__. |    |   |__|__  _\   \ /   /__.__._____    ______
/    \  \/ /  _ \ /    \   __\__  \ _/ ___\   __\  | __ \ /  _ \ /  _ \|  |/ /  | __ <   |  | |    |   |  \  \/ /\   Y   <   |  |\__  \  /  ___/
\     \___(  <_> )   |  \  |  / __ \\  \___|  |    | \_\ (  <_> |  <_> )    <   | \_\ \___  | |    |___|  |\   /  \     / \___  | / __ \_\___ \ 
 \______  /\____/|___|  /__| (____  /\___  >__|    |___  /\____/ \____/|__|_ \  |___  / ____| |_______ \__| \_/    \___/  / ____|(____  /____  >
        \/            \/          \/     \/            \/                   \/      \/\/              \/                  \/          \/     \/ """)

contact=[]
numbers=[]
def add_contact(name, number):
   contact.append(name)
   numbers.append(number)
   print("Done!")


def del_contact(contact_to_del):
   index_no = -1
   
   for i in contact:
      index_no += 1
      
      if i == contact_to_del:
         contact.pop(index_no)
         numbers.pop(index_no)
         print("Done!!")
         break
         
      elif (index_no+1) > len(contact):
         print("Contact not found")
         break
         
      else:
         continue

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

   if mycontact in contact:
      index_no1 = -1
      for v in contact:
         index_no1 += 1
         if v==mycontact:
            print(f"\nContact name: {v}\nContact number: {numbers[index_no1]}")
            name0=input("New Contact name: ")
            number0=input("New Contact number: ")
            try:
               contact[index_no1]=name0.upper()
               numbers[index_no1]=number0
               print("Done!")
            except:
               print("Error!")
   else:
      print("Contact not found")

List_of_cmds="List of commands:\n\tadd : add a contact to contact book\n\tdel : delete an existing contact\n\tsearch : search for an existing contact\n\tedit : edit an existing contact\n\tview : view the contact book\n\tquit : quit the app\n\thelp : get this list of commands"
print(List_of_cmds)

while True:
   cmd=input("\n\n>>")
   if cmd=="add":
      name1=input("\nContact name: ")
      number1=input("Contact number: ")
      add_contact(name1.upper(),number1)
   elif cmd=="del":
      name2=input("\nContact name: ")
      del_contact(name2.upper())
   elif cmd=="search":
      name3=input("\nContact name: ")
      search(name3.upper())
   elif cmd=="edit":
      name4=input("\nContact name: ")
      edit(name4.upper())
   elif cmd=="view":
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