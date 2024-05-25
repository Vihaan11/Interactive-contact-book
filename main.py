contact=[]
numbers=[]
def add_contact(name, number):
  contact.append(name)
  numbers.append(number)


def del_contact():
   contact_to_del=input("Which contact do you want to delete (Enter name of contact : case sensitive): ")
   index_no = -1
   
   for i in contact:
      index_no += 1
      
      if i == contact_to_del:
         contact.pop(index_no)
         numbers.pop(index_no)
         break
         
      elif (index_no+1) > len(contact):
         print("Contact not found")
         break
         
      else:
         continue
