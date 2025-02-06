# This file will contain the main program/service. 


from datetime import datetime
import sys



def main():

    curr_time = datetime.now()
    current_time = curr_time.strftime("%H:%M:%S")
    print("time: " + current_time)


    print()

    command = input("""Welcome to our store’s app, used by our employees for the
    store’s daily operations. This app allows you to manage our
    store’s customer info, movie info, and employee info. To start
    the app, enter any digit. If you don’t want to use the app, then
    type ‘quit’. If you use the app, additional instructions will be
    provided in the app, for performing the operations on the
    customer, movie, and employee data.
    A new feature has been added to the app, that allows the
    user to sort the store’s movies in alphabetical order by title,
    or by price. This can greatly decrease the time the user of the
    app spends looking for a particular movie. This feature is
    available on the “Search Through Movies Page”.
    For a tutorial on how to perform operations on the store’s
    current and prospective movies, first enter any digit, then
    press 5, then enter “help”, then enter “help” again.""")

    print("you entered", command)
    print()

    quit_help_flag = False

    try:
        int(command)
    except ValueError:
        quit_help_flag = True
        
        
    if (quit_help_flag and command == "quit"):
        sys.exit("exiting the program...")
        
        
        
    print()
    print("Movie Store Homepage")
    print()
    print("""Welcome to the Movie Store Homepage.To perform operations on our store’s customer data press “1”. To perform operations on our
    store’s movie data press “5”. To perform operations on our store’s employee data press “9”.
    To quit the app, enter 'quit'.""")

    home_page_command = input()
    print()


    print("you entered", home_page_command)
    print()

    quit_homepage_flag = False

    try:
        int(home_page_command)
    except ValueError:
        quit_homepage_flag = True
        
        
    if (quit_homepage_flag and home_page_command == "quit"):
        sys.exit("exiting the program...")
        
        
        
    print()


    movies_array = [["The Godfather Part II", 5.99 ], ["Forrest Gump ", 4.95
    ], ["Shawshank Redemption", 4.99], ]

    mov_length = len(movies_array)
    for row in movies_array :
        print("Movie: " + row[0] + ", Price: " + str(row[1]
                                                ))
        
        
    #Customer Name: John Smith Customer’s Phone Number: 404-777-4365
    #Customer Name: Jane Gonzales Enter Customer’s Phone
    #Number :
    #697-4754-9354
    #Customer Name: Michael Lin Customer’s Phone Number
    #:
    #787-3339-6549"""

    print()

    customers_array = [["John Smith", "404-777-4365"
    ], ["Jane Gonzales", "697-4754-9354"

    ], ["Michael Lin", "787-3339-6549"], ]

    mov_length = len(movies_array)
    for row in customers_array :
        print("Name: " + row[0] + ", Phone Number: " + row[1]
                                                )
        
    print()
        
    '''
    Employee Name: Benjamin Nguyen
    Employee Name: Carla Michaels
    Employee Name: Jim Rajeth
    '''

    employees_array = [["Benjamin Nguyen ", 1, "Job : Clerk, Years worked: 2, Schedule : Mon-Fri 8:00am-5:00pm"
    ], ["Carla Michaels ", 2, "Job : Assitant Manager, Years worked: 4, Schedule : Mon-Sat 8:00am-6:00pm"

    ], ["Jim Rajeth ", 3, "Job : Manager, Years worked: 5, Schedule : Mon-Sat 8:00am-8:00pm"], ]

    mov_length = len(movies_array)
    for row in employees_array :
        print("Name: " + row[0] + ", Employee ID: " + str(row[1])
                                                )
        
    print()

    if home_page_command == "1":
        customers_page(customers_array)
        
    elif home_page_command == 5:
        movies_page(movies_array)
        
    elif home_page_command == 9:
        employees_page(employees_array)

    else:
        sys.exit()
        
        





def customers_page(cus_array):
    
    print()
    print("""To add a customer to the store’s membership list, enter “add”. To verify that a customer
    isa member with the store enter “verify”. To sell a movie to a customer enter “sell”.
    To view the store’s membered customers, enter “search”. To cancel a customer
    membership, enter “cancel”. To quit the app, enter “quit”.""")

    print()


    customer_page_command = input()
    print()


    print("you entered", customer_page_command)
    print()

    quit_customer_flag = False

    try:
        int(customer_page_command)
    except ValueError:
        quit_customer_flag = True
    
    
    if (quit_customer_flag and customer_page_command == "quit"):
        sys.exit("exiting the program...")
    
    
    
    print()
    
    
    
    
def customers_page(cus_array):
    
    print()
    customer_page_command = input("""To add a customer to the store’s membership list, enter “add”. To verify that a customer
    is the a member with the store enter “verify”. To sell a movie to a customer enter “sell”.
    To view the store’s membered customers, enter “search”. To cancel a customer
    membership, enter “cancel”. To quit the app, enter “quit”.""")

    print()


    customer_page_command = input()
    print()


    print("you entered", customer_page_command)
    print()

    quit_customer_flag = False

    try:
        int(customer_page_command)
    except ValueError:
        quit_customer_flag = True
    
    
    if (quit_customer_flag and customer_page_command == "quit"):
        sys.exit("exiting the program...")
    
    
    
    print()
    found = False
    
    if customer_page_command == "verify":
        found = verify_customer(cus_array)
        
    elif customer_page_command == "add":
        add_customer(cus_array)
        
    elif customer_page_command == "sell":
        sell_customer(cus_array)

    elif customer_page_command == "search":
        search_customer(cus_array)
        
    elif customer_page_command == "cancel":
        cancel_customer(cus_array)
        
    
    
    if found == True:
        print("customer's name was found")
    else:
         print("customer's name was not found in the membered customer list.")
    










def add_customer(cus_array):
    customer_name = input("Please enter your first and last name")
    customer_phone = input("Please enter your phone number")
    
    new_customer_entry = [customer_name, customer_phone]
    
    cus_array.append(new_customer_entry)
    
    
    for row in cus_array :
        print("Name: " + row[0] + ", Phone Number: " + row[1]
                                                )
        
    print()
    sys.exit("exiting in add_customer")



def sell_customer(cus_array):
    customer_name = input("Please enter your first and last name")
    customer_phone = input("Please enter your phone number")
    
    
    found = False
    for row in cus_array:
        if customer_name not in row:
            pass
        else:
            found = True
            print("The name is valid")
            
        
    if found == True:
        print("The name is valid")
    if found != True:
        print("Sorry, we don't see that name in our membered customer list. blah blah blah.")

    
    sys.exit("exiting in sell_customer")
    """
    
    valid_customer = verify_customer(cus_array)
    if valid_customer == False:
        print("Sorry, we don't see your name in our membered customer list")
        
    return
    """



def search_customer(cus_array):
    pass



def cancel_customer(cus_array):
    customer_name = input("Please enter your first and last name")
    customer_phone = input("Please enter your phone number")
    print()
    
    
    found = False
    for row in cus_array:
        if customer_name not in row:
            pass
        else:
            found = True
            print("The name is valid")
            
            
    print()
    print()
    print("The customer membership was deleted successfully. The updated membered customer list is;")
    
    for index, row in enumerate(cus_array):
        if customer_name in row:
            cus_array.pop(index)
            
    
    for row in cus_array :
        print("Name: " + row[0] + ", Phone Number: " + row[1]
                                                )
        
    print()
        
      
            
        
    

    
    sys.exit("exiting in cancel_customer")




def verify_customer(cus_array):
    customer_name = input("Please enter your first and last name")
    customer_phone = input("Please enter your phone number")
    
    for row in cus_array:
        if customer_name not in row:
            return False 
       
        return True 


if __name__ == "__main__":
     main()
    