contact=[]
numbers=[]
def add_contact(name, number):
  contact.append(name)
  numbers.append(number)


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
            print(f"Contact name: {v}\nContact number: {numbers[index_no0]}")
   else:
      print("Contact not found")

