#Deze code niet nodig, wordt vervangen door arduino code
import websockets
import asyncio

PORT = 7890

print("Server listening on Port " + str(PORT))

#Deze functie handelt berichten af
async def echo(websocket, path):
    #stuurt bericht wanneer iemand connect
    print("A client just connected")
    try:
        async for message in websocket:
            #print inkomende berichten
            print("Received message from client: " + message)
            await websocket.send("Bericht ontvangen door server")
    except websockets.exceptions.ConnectionClosed as e:
        #print wanneer iemand disconnect
        print("A client just disconnected")

#variabele die de server start
start_server = websockets.serve(echo, "localhost", PORT)

#server wordt gestart en code runt totdat je deze handmatig onderbreekt
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()