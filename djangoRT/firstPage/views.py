from django.shortcuts import render 
from django.http import JsonResponse
import json,requests,random,time ,websocket,asyncio
from django.views.decorators.csrf import csrf_exempt
def index(request):   
    return   render(request,'index.html')

x=1
def fetch(request): 
    
    try: 
        ws = websocket.WebSocket()
        ws.connect("ws://localhost:8000/ws/polData/", ) 
        while x==1:
            time.sleep(1)
            import psutil  
            ws.send(json.dumps({'value':random.randint(1,100)}))
    except ValueError as e:
        print(e.message)
        pass
 
    
    

@csrf_exempt
def deactivate(request):
    print('________')
    global x 
    x=0  
    time.sleep(1)
    x=1
    return JsonResponse({})