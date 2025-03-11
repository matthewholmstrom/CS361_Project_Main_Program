# This file will contain the main program/service.


from datetime import datetime
import sys
import copy
import time
import zmq 



def main():

    print()
    print()
    curr_time = datetime.now()
    current_time = curr_time.strftime("%H:%M:%S")
    print("time: " + current_time)

    print()
    print("Greetings Page")
    print()

    command = input("""Welcome to our store’s app. This app manages
    customer info, movie info, and employee info. type 'quit' to exit.
    
    
    A new feature has been added for sorting the store's movies
    by title or price. This can decrease the time the user 
    spends looking for a particular movie. This new feature is
    on the “Search Through Movies Page”.
    
    
    For a tutorial on how to perform operations on the store’s
    current and prospective movies, first enter any digit, then
    press 5, then enter “help”, then enter “help” again. """)


    print()

    quit_help_flag = False

    try:
        int(command)
    except ValueError:
        quit_help_flag = True

    if (quit_help_flag and command == "quit"):
        sys.exit("exiting the program...")

    Home_page()


def Home_page():
    print()
    print()
    print("Movie Store Homepage")
    print()
    print("""Welcome to the Movie Store Homepage.To perform operations on our store’s customer data press “1”. To perform operations on our
    store’s movie data press “5”. To perform operations on our store’s employee data press “9”.
    To quit the app, enter 'quit'. """)

    home_page_command = input()
    print()



    quit_homepage_flag = False

    try:
        int(home_page_command)
    except ValueError:
        quit_homepage_flag = True

    if (quit_homepage_flag and home_page_command == "quit"):
        sys.exit("exiting the program...")

    print()

    movies_array = [["The Godfather Part II", 5.99], ["Forrest Gump ", 4.95
                                                      ], ["Shawshank Redemption", 6.15], ["Indiana Jones", 3.15],
                    ["Cars2", 7.15], ["Alice and Wonderland", 4.15],   ["Office Space", 5.75], ["Fargo", 6.15],
                    ["Wall-E", 4.05],]
    """
    mov_length = len(movies_array)
    for row in movies_array:
        print("Movie: " + row[0] + ", Price: " + str(row[1]
                                                     ))
    """

    # Customer Name: John Smith Customer’s Phone Number: 404-777-4365
    # Customer Name: Jane Gonzales Enter Customer’s Phone
    # Number :
    # 697-4754-9354
    # Customer Name: Michael Lin Customer’s Phone Number
    #:
    # 787-3339-6549

    print()

    customers_array = [["John Smith", "111"
                        ], ["Jane Gonzales", "697-4754-9354"

                            ], ["Michael Lin", "787-3339-6549"], ["John Smith", "222"
                                                                  ]]
    """
    mov_length = len(movies_array)
    for row in customers_array:
        print("Name: " + row[0] + ", Phone Number: " + row[1]
              )
    """
    print()


    #Employee Name: Benjamin Nguyen
    #Employee Name: Carla Michaels
    #Employee Name: Jim Rajeth


    employees_array = [["Benjamin Nguyen", 1, "Job : Clerk, Years worked: 2, Schedule : Mon-Fri 8:00am-5:00pm"
                        ],
                       ["Carla Michaels", 2, "Job : Assitant Manager, Years worked: 4, Schedule : Mon-Sat 8:00am-6:00pm"

                        ], ["Jim Rajeth", 3, "Job : Manager, Years worked: 5, Schedule : Mon-Sat 8:00am-8:00pm"], ]
    """
    mov_length = len(movies_array)
    for row in employees_array:
        print("Name: " + row[0] + ", Employee ID: " + str(row[1])
              )
    """
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

    print("Customers Homepage")
    print()

    customer_page_command = input("""To add a customer to the store’s membership list, enter “add”. To verify that a customer
    is the a member with the store enter “verify”. To sell a movie to a customer enter “sell”.
    To view the store’s membered customers, enter “search”. To cancel a customer
    membership, enter “cancel”. To quit the app, enter “quit”. """)

    print()

    customer_page_command = input()
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
        verify_customer(cus_array)

    elif customer_page_command == "add":
        add_customer(cus_array)

    elif customer_page_command == "sell":
        sell_customer(cus_array)

    elif customer_page_command == "search":
        search_customer(cus_array)

    elif customer_page_command == "cancel":
        cancel_customer(cus_array)


def add_customer(cus_array):
    print("")
    print("Add Customer ")

    customer_command = input("""To add a customer to the store’s membership list, enter the
customer’s name and phone number and then press “add” below.
Enter “quit” to quit the program. """)



    customer_name = input("Please enter your first and last name")
    customer_phone = input("Please enter your phone number")
    print()
    new_customer_entry = [customer_name, customer_phone]

    customer_command = input("""Enter "add" to add the customer or "quit" to exit the program.""")
    print()

    if customer_command == "quit":
        sys.exit("exiting from cancel customer page.")

    if customer_command == "add":
        
        verification_message = input("""Warning: are you sure that you want to add this customer to the membered customer list? This
cannot be undone. You must manually delete the customer membership if you want the
membership to be terminated. Please enter “yes” to add the membership or “no” to cancel this
operation.""")

        if verification_message == "yes":

            cus_array.append(new_customer_entry)

            print("The member has been added to the membered customer list. The list is printed below.")
            print()
            for row in cus_array:
                print("Name: " + row[0] + ", Phone Number: " + row[1]
                      )


        elif verification_message == "no":
            main()

    elif customer_command == "quit":
        print()
        sys.exit("exiting in add_customer")

    Home_page()


def sell_customer(cus_array):
    print("Sell movie to Customer")

    customer_name = input("Please enter your first and last name")
    customer_phone = input("Please enter your phone number")

    customer_command = input("enter quit to quit the program.")

    if customer_command == "quit":
        sys.exit("exiting from cancel customer page.")

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
    print()
    print("View the Store’s Member Customer List")
    print()
    print("""The store’s membered customers are displayed below, enter “quit” to quit the program.""")
    print()
    
    for row in cus_array:
        print("Name: " + row[0] + ", Phone Number: " + row[1]
              )

    print()
    customer_command = input("""Enter the name of the customer and their phone number, when prompted, to see if the store finds
                             a membership under those credentials. or enter "quit" to exit the program. """)

    print()
    customer_name = input("Please enter your first and last name ")
    
    customer_name = customer_name.lower()
    print()
    
    if customer_command == "quit":
        sys.exit("exiting from cancel customer page.")
    count = 0
    for index, row in enumerate(cus_array):

        if cus_array[index][0].lower() == customer_name:
            count += 1

    found = False
    for index, row in enumerate(cus_array):

        if cus_array[index][0].lower() == customer_name:

            found = True
            if count > 1:
                print("""There is more than one person with that name in our store's membership list. Please 
                enter your phone number, so that we can determine if you are a member with the store. """ )
                print()
                customer_phone = input("Please enter your phone number")
                print()
                
                if cus_array[index][1] == customer_phone:
                    print("The customer was found the the store's membered customer list ")
                    Home_page()
                    break

                if cus_array[index][1] != customer_phone:
                    print(
                        "There was no match for that customer name belonging to that phone number, in our store's membered customer list")
                    Home_page()
                    break
                         
            elif count == 1:
                print("The customer was found in the store's membered customer list")
                print()

    if found == False:
        print("That customer name was not found the the store's membered customer list")
        print()

    Home_page()

def cancel_customer(cus_array):

    print()
    print("Cancel Customer Membership")
    print()

    print("""The store’s membered customers are displayed below, enter “quit” to quit the program.""")

    for row in cus_array:
        print("Name: " + row[0] + ", Phone Number: " + row[1]
              )

    print()
    try:
        customer_command = input("""To cancel the customer membership, enter the customer’s name and
    phone number and press “cancel” below. To undo the cancellation of the
    customer membership, enter “undo”. To redo the cancellation of the
    membership, enter “redo”. To Enter “quit” to quit the program. 
    """)

        if customer_command == "quit":
            sys.exit("exiting from cancel customer page.")

        print()
        customer_name = input("Please enter your first and last name ")
        customer_phone = input("Please enter your phone number ")

        num = input("enter an integer. ")
        int(num)
        print()

        if customer_command == "quit":
            sys.exit("exiting from cancel customer page.")
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

        print("The customer membership was deleted successfully. The updated membered customer list is;")
        print()

        for row in cus_array:
            print("Name: " + row[0] + ", Phone Number: " + row[1]
                  )
        print()
        undo_command = input("""Would you like to undo the deletion of the customer membership. If yes, enter "undo", if the 
                              answer is no enter "no" """)

        if undo_command == "undo":
            new_customer_entry = [customer_name, customer_phone]

            cus_array.append(new_customer_entry)

            print("""The customer membership was
    once again added to the store’s
    membered customer list. The list is printed below """
                  )
            
            print()
            for row in cus_array:
                print("Name: " + row[0] + ", Phone Number: " + row[1]
                      )
                
            print()

            redo_command = input("""Would you like to redo the deletion of the customer membership. If yes, enter "redo", if the 
                              answer is no enter "no" """)

            if redo_command == "redo":

                print()
                for index, row in enumerate(cus_array):
                    if customer_name in row:
                        cus_array.pop(index)

                    print("""The customer membership was
            once again deleted from the store’s
            membered customer list. The list is printed below """
                          )
                    
                    print()
                    for row in cus_array:
                        print("Name: " + row[0] + ", Phone Number: " + row[1]
                              )
                    print()
                    
    except Exception as e:
        print(f"an {e} error was caught. ")
    Home_page()


def verify_customer(cus_array):

    print()
    print("Verify Customer Membership")
    print()
    print("Here is what that membered customer list looks like.")
    print()
    
    
    for row in cus_array:
        print("Name: " + row[0] + ", Phone Number: " + row[1]
              )

    print()
    
    
    copy_array = cus_array[:]
    customer_name = input("Please enter your first and last name ")
    customer_phone = input("Please enter your phone number ")


    customer_name = customer_name.lower()

    customer_command = input("enter quit if you would like to quit the program ")
    print()
    
    if customer_command == "quit":
        sys.exit("exiting from cancel customer page.")

    found = False
    for index, row in enumerate(cus_array):

        if cus_array[index][0].lower() == customer_name:
            found = True
            print("The customer was found in the store's membered customer list")
            print()
            break

    if found == False:
        print("The customer was not found in the store's membered customer list")
        print()
    """
    for row in cus_array:
        if customer_name not in row:
            return False 

        return True 
    """
    Home_page()

def movie_page(movie_array):
    print()
    print("Movie Page")
    print()

    movie_page_command = input("""To view the store’s movie list, enter “search”. To add a movie to the
store’s movie list, enter “add”. To see the synopsis of a movie, that is
not necessarily already in the store’s movie list, enter “summary”. To
see a tutorial on how to perform data manipulations on the store’s
current and prospective movies, enter “help """)

    movie_page_command = input()
    print()


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

    


def search_movie(movie_array):
    print()
    print("View the Store’s Movie List")


    movie_command = input("""The store’s movie list is displayed below. To sort movies by title alphabetically, enter
“sort1”. To sort movies by increasing price, enter “sort9”. To see the original movie list in its original format (unsorted) enter
 "plain". Enter “quit” to quit the
program """)

    print()

    if movie_command == "quit":
        sys.exit("exiting from cancel customer page.")



    if movie_command == "sort1":
        print("Start of sorting the movie list....")
        start = time.time()

        movies_sorted = sorted(movie_array, key=lambda s: s[0])


        end = time.time()
        total_time = end - start

        print("ended sorting the list. It took " + str(total_time) + "seconds to sort the movies list.")


        print()
        print("The sorted movies are below;")

        for row in movies_sorted:
            print("Movie: " + row[0] + ", Price: " + str(row[1]
                                                         ))

    elif movie_command == "sort9":

        print("Start of sorting the movie list....")
        start = time.time()

        movies_sorted = sorted(movie_array, key=lambda s: s[1])

        end = time.time()
        total_time = end - start

        print("ended sorting the list. It took " + str(total_time) + "seconds to sort the movies list.")

        print("The sorted movies are below;")


        for row in movies_sorted:
            print("Movie: " + row[0] + ", Price: " + str(row[1]
                                                         ))
    elif movie_command == "plain":
        print()
        for row in movie_array:
            print("Movie: " + row[0] + ", Price: " + str(row[1]                                       ))


    Home_page()

def add_delete_movie(movie_array):
    print()
    print("Add or Delete Movie")

    print()
    movie_command = input("""To add a movie to the store’s movie list, enter "add", then enter the movie title and movie price
To delete a movie from the store’s movie list, enter "delete", the enter the movie title and movie price. Enter “quit” to quit the program. """)
    
    print()
    if movie_command == "quit":
        sys.exit("exiting from cancel customer page.")

    if movie_command == "add":
        movie_name = input("Please enter the movie name ")
        movie_price = input("Please enter the movie price ")
        print()

        float_price = float(movie_price)


        new_movie_entry = [movie_name, float_price]


        movie_array.append(new_movie_entry)
        print("The movie was added to the movie list.")
        print()
        print("Here is the updated movie list.")
        for row in movie_array:

            print("Movie: " + row[0] + ", Price: " + str(row[1]
                                                         ))



    elif movie_command == "delete":
        movie_name = input("Please enter the movie name ")
        movie_price = input("Please enter the movie price ")

        for index, row in enumerate(movie_array):
            if movie_name in row:
                print()
                validation = input("""Do you really want to delete this
movie? This is permanent. You
will have to manually add the
movie, if you want it
in there again.
Enter “yes” or “no” """)
                if validation == "yes":
                    movie_array.pop(index)
                    print()
                    for row in movie_array:
                        print("Movie name: " + row[0] + ", Price: " + str(row[1])
                              )

                if validation == "no":
                    print()
                    print("The movie was not deleted.")
                    print("Here is the movies list below;")
                    for row in movie_array:
                        print("Movie name: " + row[0] + ", Price: " + str(row[1])
                              )

    Home_page()

def summary_movie(movie_array):
    print()
    print("Movie Wishlist Synopsis")

    print()
    movie_command = input("""If you want to see the plot of a movie, then enter "plot". If you want to
                          see the actors list for a movie, then enter "actors". If you want to see the rating
                          of a movie, enter "rating". Enter “quit” to quit the program. """)

    if movie_command == "quit":
        sys.exit("exiting from cancel customer page.")
        
        
    context = zmq.Context()

    socket = context.socket(zmq.REQ)

    socket.connect("tcp://localhost:5558")

    print("Sending a request to the server...")


    print()
    if movie_command == "plot":
        
        print()
        
        movie_title = input("Please enter the movie name ")
        release_date = input("Please enter the movie's release date ")
        print()
        
        movie_command = movie_command.strip()
        movie_title = movie_title.strip()
        release_date = release_date.strip()
        string_list = [movie_title, release_date, movie_command]
        final_string = ','.join(string_list)
        
        print("Sending this to the server: ", final_string)
        socket.send_string(final_string)

        response = socket.recv()
        print()
        print("The plot is : ", (response.decode()))
        
        
    elif movie_command == "actors":
         
        print()
        
        movie_title = input("Please enter the movie name ")
        release_date = input("Please enter the movie's release date ")
        print()
        
        movie_command = movie_command.strip()
        movie_title = movie_title.strip()
        release_date = release_date.strip()
        string_list = [movie_title, release_date, movie_command]
        final_string = ','.join(string_list)
        
        print("Sending this to the server: ", final_string)
        socket.send_string(final_string)

        response = socket.recv()
        print()
        print("The actors are : ", (response.decode()))


    elif movie_command == "rating":
        
        print()
        
        movie_title = input("Please enter the movie name ")
        release_date = input("Please enter the movie's release date ")
        print()
        movie_command = movie_command.strip()
        movie_title = movie_title.strip()
        release_date = release_date.strip()
        string_list = [movie_title, release_date, movie_command]
        final_string = ','.join(string_list)
        print("Sending this to the server: ", final_string)
        
        socket.send_string(final_string)
        

        response = socket.recv()
        print()
        print("The rating is : ", (response.decode()))
        
   

    print()
    Home_page()

def help_movie(movie_array):
    print()
    print("Movie Help")
    print()
    movie_command = input("""To go back to the Movies page, enter “movies”. To see the
tutorial on how to perform manipulations on current and
prospective movies, enter “help”. To exit the program,
“enter quit”. """)

    if movie_command == "quit":
        sys.exit("exiting from cancel customer page.")

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

    Home_page()
    
    
def employees_page(employee_array):
    print()
    print("Employees")
    print()
    customer_page_command = input("""To view the store’s current employees, enter “search”. To get an
employee’s information, enter “info”. To see inspirational quotes, enter "quote". To manipulate the store's unfinished tasks, enter "task". To translate text from one language to another enter "translate"
To quit the app, enter “quit”. """)

    print()

    employee_page_command = input()
    print()

    if employee_page_command == "quit":
        sys.exit("exiting from cancel customer page.")



    if employee_page_command == "search":
        search_employee(employee_array)

    elif employee_page_command == "info":

        get_employee_info(employee_array)
        
        
    elif employee_page_command == "quote":

        get_quote(employee_array)
        
    elif employee_page_command == "task":

        employee_tasks(employee_array)
        
          
    elif employee_page_command == "translate":

        translated_text(employee_array)


    elif customer_page_command == "quit":
        sys.exit("exiting from the employees_page.")


def get_employee_info(employee_array):
    print()
    print("Get Employee Information")

    for row in employee_array:
        print("Name: " + row[0] + ", Employee ID: " + str(row[1])
              )

    print("""To get an employee’s information enter the employee’s name or their employee
ID number, and then press “get” below. To Enter “quit” to quit the program.
""")
    employee_name = input("Please enter the employee's name. ")
    employee_ID = input("Please enter the employee ID number. ")

    print()
    employee_command = input("""Enter "get" to get the employee information or "quit" to exit the program.""")
    print()

    if employee_command == "get":

        for index, row in enumerate(employee_array):

            if employee_name in row:
                print(employee_array[index][2])

            elif int(employee_ID) in row:
                print(employee_array[index][2])
                
    if employee_command == "get":

        for index, row in enumerate(employee_array):

            if employee_name in row:
                print(employee_array[index][2])

            elif int(employee_ID) in row:
                print(employee_array[index][2])



    elif employee_command == "quit":
        sys.exit("exiting from get_employee_info page.")

    Home_page()
    
    
def get_quote(employee_array):
    print()
    print("Get Quote Page")
    print()

   

    quote_type = input ("""Enter "inspirational" if you want to see a random inspirational quote. 
                        Enter "movie" if you want to see a random movie quote.
                        To Enter “quit” to quit the program. """)
    
    
    
        
    context = zmq.Context()


    socket = context.socket(zmq.REQ)

    socket.connect("tcp://localhost:5559")

    print()
    
    print("Sending a request to the server...")
    


    print()
    if quote_type == "inspirational":
        
 
        print("sending this to the server : ", quote_type)
        socket.send_string(quote_type)

        response = socket.recv()
        print()
        print("The random inspirational quote is: ", response.decode())
        

                
    elif quote_type == "movie": 
        
        print("sending this to the server : ", quote_type)
        socket.send_string(quote_type)

        response = socket.recv()
        print()
        print("The random movie quote is: ", response.decode())


    if quote_type == "quit":
        sys.exit("exiting from tasks to-do page.")

    Home_page()
    
    
def employee_tasks(employee_array):
    print()
    print("Employee Tasks To-do")
    print()
    
    context = zmq.Context()


    socket = context.socket(zmq.REQ)

    socket.connect("tcp://localhost:6001")

    print()
    print("Sending a request to the server...")


    input_type = input("""Enter "add" if you want to add a task. 
                  Enter "view" if you want to view the stores unfinished taks.
                  Enter "delete" if you want to delete a task.
                  Enter “quit” to quit the program. """)
    
    input_type = input_type.strip()
    
    if input_type == "add":
        
        
        print()
        command = input("Enter the unfinished task that you want to save. ")
        print()
        command.strip()
        
        final_string = input_type + "," + command
        
        print("sending this to the server : ", final_string)
        socket.send_string(final_string)
        print()
        response = socket.recv()

        print(response.decode())

        
        
    elif input_type == "delete":
        
        print()
        command = input("Enter the task that you want to delete. ")
        print()
        command.strip()
        
        final_string = input_type + "," + command
        
        print("sending this to the server : ", final_string)
        socket.send_string(final_string)
        
        print()
        response = socket.recv()

        print(response.decode())
    
    
    elif input_type == "view":
        
        print("sending this to the server : ", input_type)
        socket.send_string(input_type)
        
        response = socket.recv()
        print()
        print(response.decode())
        
    
    if input_type == "quit":
        sys.exit("exiting from move_quote page.")

    Home_page()
    
    
def translated_text(employee_array):
    print()
    print("Get Translated Text")
    print()

   
    language_type = input ("""Enter the text that you want translated.
                   Enter “quit” to quit the program. """)
    
    language_type = language_type.strip()
    print()
    command = input("Enter the language that you want the text translated to.")
    print()
    command = command.strip()
    
    final_string = language_type + ',' + command
        
    context = zmq.Context()


    socket = context.socket(zmq.REQ)

    socket.connect("tcp://localhost:6002")


    print("Sending a request to the server...")
    print()
    socket.send_string(final_string)
    print()
    
    response = socket.recv()

    print("The translated string is : ", response.decode())
        

    if language_type == "quit":
        sys.exit("exiting from tasks to-do page.")

    Home_page()
    

if __name__ == "__main__":
    main()
