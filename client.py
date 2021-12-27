import websockets
import asyncio

#deze functie zorgt voor verbinding met server
async def listen():
    url = "ws://127.0.0.1:7890"
    # Maakt verbinding met server
    async with websockets.connect(url) as ws:
        # Stuurt een bericht naar server - hier komt de inhoud van het glas en het device die het bericht verstuurd (raspberry)
        await ws.send('{"device": "raspberry", "inhoud": "250ml"}')
        #Deze wacht tot er berichten binnenkomen. Kan evt. weg omdat pi geen berichten hoeft te ontvangen.
        while True:
            msg = await ws.recv()
            print(msg)

# Begint de verbinding met de server
asyncio.get_event_loop().run_until_complete(listen())