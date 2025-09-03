contacts = {}

while True:
    print("\n****** Contact BOOK ******")
    print("1. Add contact")
    print("2. Search number")
    print("3. Show all contacts")
    print("4. Exit") 
    
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
         name = input("Enter your name: ")
         contact = input("Enter your number: ")
         contacts[name] = contact 
         print("Contact Add Successfully!")
     
   
    elif choice == "2":
        name = input("Enter Name to search: ")
        if name in contacts:
            print(f"{name}'s number is {contacts[name]}")
        else:
            print("Contact not found")
            
    elif choice == "3":
        if not contacts:
            print("No contact yet!")
        else:
            print("--- All contacts numbers ---")
            for name, contact in contacts.items():
                print(f"{name}: {contact}")
    
        
    elif choice == "4":
        print("Exit Contact Book, GOODBYE!")
        
        
    else:
        print("Invalid Choice! ")
        print("Please Enter from 1 to 4")
    
            

    


    
        