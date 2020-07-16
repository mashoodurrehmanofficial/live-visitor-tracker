import json,requests,random,time ,websocket
ws = websocket.WebSocket()
ws.connect("ws://localhost:8000/ws/polData/", )
while True:
    time.sleep(1)
    import psutil  
    ws.send(json.dumps({'value':int(psutil.virtual_memory().percent)}))