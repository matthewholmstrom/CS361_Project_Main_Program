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
    ], ["Shawshank Redemption", 6.15], ]

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

    employees_array = [["Benjamin Nguyen", 1, "Job : Clerk, Years worked: 2, Schedule : Mon-Fri 8:00am-5:00pm"
    ], ["Carla Michaels", 2, "Job : Assitant Manager, Years worked: 4, Schedule : Mon-Sat 8:00am-6:00pm"

    ], ["Jim Rajeth", 3, "Job : Manager, Years worked: 5, Schedule : Mon-Sat 8:00am-8:00pm"], ]

    mov_length = len(movies_array)
    for row in employees_array :
        print("Name: " + row[0] + ", Employee ID: " + str(row[1])
                                                )
        
    print()

    if home_page_command == "1":
        customers_page(customers_array)
        
    elif home_page_command == "5":
        movie_page(movies_array)
        
    elif home_page_command == "9":
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
    
    print()
    
    customer_command = input("""To cancel the customer membership, enter the customer’s name and
phone number and press “cancel” below. To undo the cancellation of the
customer membership, enter “undo”. To redo the cancellation of the
membership, enter “redo”. To Enter “quit” to quit the program.
""")
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
    for index, row in enumerate(cus_array):
        if customer_name in row:
            cus_array.pop(index)
            
    
    print()
    print("The customer membership was deleted successfully. The updated membered customer list is;")
    
    
            
    
    for row in cus_array :
        print("Name: " + row[0] + ", Phone Number: " + row[1]
                                                )
    print()
    undo_command = input ("""Would you like to undo the deletion of the customer membership. If yes, enter "undo", if the 
                          answer is no enter "no" """)
        
    if undo_command == "undo":
        new_customer_entry = [customer_name, customer_phone]
    
        cus_array.append(new_customer_entry)
    
        print("""The customer membership was
once again added to the store’s
membered customer list. The list is printed below"""
)
        for row in cus_array :
            print("Name: " + row[0] + ", Phone Number: " + row[1]
                                                )
        
        
        redo_command = input ("""Would you like to redo the deletion of the customer membership. If yes, enter "redo", if the 
                          answer is no enter "no" """)
        
        if redo_command == "redo":
        
        
                    
            print()
            for index, row in enumerate(cus_array):
                if customer_name in row:
                    cus_array.pop(index)
                
                
                print("""The customer membership was
        once again deleted from the store’s
        membered customer list. The list is printed below"""
        )
                for row in cus_array :
                    print("Name: " + row[0] + ", Phone Number: " + row[1]
                                                        )
                
            
        
            
        
    

    
    sys.exit("exiting in cancel_customer")




def verify_customer(cus_array):
    customer_name = input("Please enter your first and last name")
    customer_phone = input("Please enter your phone number")
    
    for row in cus_array:
        if customer_name not in row:
            return False 
       
        return True 
    
    
    
    
    
    
    
    
def movie_page(movie_array):
    
    print("Movie Page")
    movie_page_command = input("""To view the store’s movie list, enter “search”. To add a movie to the
store’s movie list, enter “add”. To see the synopsis of a movie, that is
not necessarily already in the store’s movie list, enter “summary”. To
see a tutorial on how to perform data manipulations on the store’s
current and prospective movies, enter “help""")

   


    movie_page_command = input()
    print()


    print("you entered", movie_page_command)
    print()

    quit_movie_flag = False

    try:
        int(movie_page_command)
    except ValueError:
        quit_movie_flag = True
    
    
    if (quit_movie_flag and movie_page_command == "quit"):
        sys.exit("exiting the program...")
    
    
    
    print()
    found = False
    
    if movie_page_command == "search":
        found = search_movie(movie_array)
        
    elif movie_page_command == "add":
        add_delete_movie(movie_array)
        
    elif movie_page_command == "summary":
        summary_movie(movie_array)

    elif movie_page_command == "help":
        help_movie(movie_array)
        
        
    
    
    if found == True:
        print("customer's name was found")
    else:
         print("customer's name was not found in the membered customer list.")
    



def search_movie(movie_array):
    print("View the Store’s Movie List")
    
    print()
    movie_command = input("""The store’s movie list is displayed below. To sort movies by title alphabetically, enter
“sort1”. To sort movies by increasing price, enter “sort9”. enter “quit” to quit the
program""")
    
    
    for row in movie_array :
        print("Movie: " + row[0] + ", Price: " + str(row[1]
                                                ))
        
    print()
    
    
    if movie_command == "sort1":
        movies_sorted = sorted(movie_array, key=lambda s:s[0])
        
    elif movie_command == "sort9":
        movies_sorted = sorted(movie_array, key=lambda s:s[1])
    
    print("The sorted movies are below;")
    
    for row in movies_sorted:
        print("Movie: " + row[0] + ", Price: " + str(row[1]
                                                ))
        
    
    
    

def add_delete_movie(movie_array):
    print()
    print("Add or Delete Movie")
    
    print()
    movie_command = input("""To add a movie to the store’s movie list, enter "add", then enter the movie title and movie price
To delete a movie from the store’s movie list, enter "delete", the enter the movie title and movie price. Enter “quit” to quit the program.""")

    if movie_command == "add":
         movie_name = input("Please enter the movie name")
         movie_price = input("Please enter the movie price")
        
        
    elif movie_command == "delete":
        movie_name = input("Please enter the movie name")
        movie_price = input("Please enter the movie price")
        
        for index, row in enumerate(movie_array):
            if movie_name in row:
                print()
                validation = input("""Do you really want to delete this
movie? This is permanent. You
will have to manually add the
movie again, if you want the
movie in the store’s inventory.
Enter “yes” or “no”""")
                if validation == "yes":
                    movie_array.pop(index)
                    print()
                    for row in movie_array :
                        print("Movie name: " + row[0] + ", Price: " + str(row[1])
                                                )
            
                if validation == "no":
                    print()
                    print("The movie was not deleted.")
                    print("Here is the movies list below;")
                    for row in movie_array :
                        print("Movie name: " + row[0] + ", Price: " + str(row[1])
                                                )
                    
    
    
    



def summary_movie(movie_array):
    print()
    print("Movie Wishlist Synopsis")
    
    print()
    movie_command = input("""If you want to see the synopsis of a movie, for prospective movies that
could be added to the movie store’s inventory. Enter the Movie title and
movie director and then enter “summary”. Enter “quit” to quit the program.""")
    
    #Back to the Future 
    movie_title = input("Please enter the movie name")
    
    # Robert Zemeckis
    movie_director = input("Please enter the movie director")
    print()
    if movie_command == "summary":
        print()
        print("""Synopsis: “In this 1980s sci-fi classic, small-town
California teen Marty McFly (Michael J. Fox) is thrown
back into the '50s when an experiment by his eccentric2
scientist friend Doc Brown (Christopher Lloyd) goes awry.
Traveling through time in a modified DeLorean car, Marty
encounters young versions of his parents (Crispin Glover, Lea
Thompson), and must make sure that they fall in love, or he'll
cease to exist. Even more dauntingly, Marty must return to his
own time and save the life of Doc Brown.” """)
    

    
    
    
    
    
    
    
    

def help_movie(movie_array):
    
    print()
    print("Movie Help")
    print()
    movie_command = input("""To go back to the Movies page, enter “movies”. To see the
tutorial on how to perform manipulations on current and
prospective movies, enter “help”. To exit the program,
“enter quit”.""")
    
    if movie_command == "movies":
        movie_page(movie_array)
        
    elif movie_command == "quit":
        sys.exit("exiting from help_movie page.")
        
    elif movie_command == "help":
        print()
        print("""From the store’s Movies page, we have the option of viewing the store’s movie inventory. We can do this by entering the command
“search”. Upon the store’s movies we have the option of sorting the movies in alphabetical order by title (using the sort1 command), or by
increasing price (using the sort9 command). Also, from the store’s Movies page, we have the option of adding or deleting one of the
store’s movies. We can add a movie to the stores inventory by typing “add” followed by “add” again. We can delete a movie from the
stores inventory by typing “add” followed by “delete”. Also, from the store’s Movies page, we have the option to see the synopsis of a
movie (even if the store doesn’t have it in its inventory). We can see the synopsis of a movie by entering “summary”, then entering the title
and director of the movie, followed by entering the command “summary” again.""")







    
def employees_page(employee_array):
    
    print()
    print("Employees")
    customer_page_command = input("""To view the store’s current employees, enter “search”. To get an
employee’s information, enter “info”. To quit the app, enter “quit”.""")

    print()


    employee_page_command = input()
    print()
    
    
    for row in employee_array :
        print("Name: " + row[0] + ", Employee ID: " + str(row[1])
                                                )
        

    
    if employee_page_command == "search":
        search_employee(employee_array)
        
    elif employee_page_command == "info":
        
        get_employee_info(employee_array)
        
    elif customer_page_command == "quit":
        sys.exit("exiting from the employees_page.")

    




def get_employee_info(employee_array):
    
    print()
    print("Get Employee Information")
    
    
    for row in employee_array :
        print("Name: " + row[0] + ", Employee ID: " + str(row[1])
                                                )
        
    
    print("""To get an employee’s information enter the employee’s name or their employee
ID number, and then press “get” below. Enter “quit” to quit the program.
""")
    employee_name = input("Please enter the employee's name.")
    employee_ID = input("Please enter the employee ID number")
    
    print()
    employee_command = input("""Enter "get" to get the employee information or "quit" to exit the program.""")
    print()
    
    if employee_command == "get":
        
        for index, row in enumerate(employee_array):
            print("hi")
            if employee_name in row:
                print(employee_array[index][2])
            
            elif int(employee_ID) in row:
                print(employee_array[index][2])

          
    elif employee_command == "quit":
        sys.exit("exiting from get_employee_info page.")





