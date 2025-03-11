import random
import zmq


context = zmq.Context()


socket = context.socket(zmq.REP)

socket.bind("tcp://*:6001")



tasklist = []
add_str = "Task was successfully added. Here are your unfinished tasks: "
view_str = "Here are your unfinished tasks: "
view_str_err = "You have no unfinished tasks. "

delete_str = "Task was successfully deleted. Here are your unfinished tasks: "
delete_str_err = "Error: task could not be deleted. "
while True:
    
    
    print("The task_to_do microservice is listening and ready for requests...")
    
    
    requestedData = socket.recv()
    
    
        
    
    
    requestedData = requestedData.decode()
    print()
    print("recieved this in the request body: ", requestedData)
    
    input_list = requestedData.split(",")
    
    user_command = input_list[0]
    
    
        
    if user_command == "add":
        
        task = input_list[1]
        tasklist.append(task)
        
        
        add_str += ", ".join(tasklist)
        
        print("sending this in the response : ", add_str)
        socket.send_string(add_str)
        
    
    
    elif user_command == "view":
        
        
        if len(tasklist) == 0:
            print("sending this in the response : ", view_str_err)
            socket.send_string(view_str_err)
            
        else:    
            print(tasklist)
            view_str += ", ".join(tasklist)
            print("sending this in the response : ", view_str)
            socket.send_string(view_str)
     
    if user_command == "delete":
        
        
        if len(tasklist) == 0:
            print("sending this in the response : ", delete_str_err)
            socket.send_string(delete_str_err)
            
        
        else:
            task = input_list[1]
            
            if task in tasklist:
                tasklist.remove(task)
                
                
                
                delete_str += ", ".join(tasklist)
                
                print("sending this in the response : ", delete_str)
        
                socket.send_string(delete_str)
