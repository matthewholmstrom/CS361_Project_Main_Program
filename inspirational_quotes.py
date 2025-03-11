import random
import zmq


context = zmq.Context()


socket = context.socket(zmq.REP)

socket.bind("tcp://*:5559")




while True:
    
    
        print("The inspirational_quotes microservice is listening and ready for requests...")
    
        quote_list1 = ["If I cannot do great things, I can do small things in a great way. — Martin Luther King, Jr",

        "Act as if what you do makes a difference. It does. — William James, American philosopher and psychologist",

        "Be the change that you wish to see in the world. — Mahatma Ghandi",

        "Don't sit down and wait for the opportunities to come. Get up and make them. — Madam C.J. Walker ", 

        "Opportunity is missed by most people because it is dressed in overalls and looks like work. —Thomas Edison ",

        "The most difficult thing is the decision to act; the rest is merely tenacity. — Amelia Earhart",

        "The bad news is time flies. The good news is you're the pilot. — Michael Altshuler",

        "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. — Jimmy Dean",

        "You get what you give. — Jennifer Lopez",

        "It is often the small steps, not the giant leaps, that bring about the most lasting change.  - Queen Elizabeth II"]




        quote_list2 = ["Frankly, my dear, I don't give a damn - Gone with the Wind 1939",

        " Im gonna make him an offer he can't refuse. The Godfather (1972)",

        "“You don’t understand! I coulda had class. I coulda been a contender. I could’ve been somebody, instead of a bum, which is what I am. — On the Waterfront",

        "Toto, Ive got a feeling we're not in Kansas anymore. - The Wizard of Oz", 

        "Here’s looking at you, kid -- Casablanca",

        "Go ahead, make my day  - Sudden Impact",

        "May the Force be with you — Star Wars",

        "Fasten your seatbelts. It’s going to be a bumpy night. - All About Eve",

        "You talkin’ to me? - Taxi Driver",

        "What we’ve got here is (a) failure to communicate. - Cool Hand Luke",
        
        "I love the smell of napalm in the morning! - Apocalypse Now",
        
        "The stuff that dreams are made of. - The Maltese Falcon"]
        
        quote1 = random.choice(quote_list1)
        
        quote2 = random.choice(quote_list2)
        
        print("The inspirational_quotes microservice is listening and ready for requests...")
        print()
        requestedData = socket.recv()
        requestedData = requestedData.decode()
        
        print("recieved this in the request body: ", requestedData)
        print()
        if requestedData == "inspirational":
                
                print("sending this in the response : ", quote1)
                socket.send_string(quote1)
                
                
        elif requestedData == "movie":
                
                print("sending this in the response : ", quote2)
                socket.send_string(quote2)
