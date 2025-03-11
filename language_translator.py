import asyncio
from googletrans import Translator


import zmq


context = zmq.Context()


socket = context.socket(zmq.REP)

socket.bind("tcp://*:6002")



while True:
    
    
    
  
    
    
    async def text_translate(requestedData):
    
        async with Translator() as translator:
            
            input_list = requestedData.split(",")
            user_command = input_list[0]
            language = input_list[1]
            

            result = await translator.translate(user_command, dest=language)
            ans = result.text
            print("sending this in the response : ", ans)
            socket.send_string(ans)
            
    print("The task_to_do microservice is listening and ready for requests...")
    
    
    requestedData = socket.recv()
    
    
        
    requestedData = requestedData.decode()
    
    print("recieved this in the request body: ", requestedData)


    asyncio.run(text_translate(requestedData))




  
