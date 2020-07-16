from channels.generic.websocket import AsyncWebsocketConsumer
import json 
x=0
class DashConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.groupname='dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        ) 
        await self.accept()
        global x
        x = x+1 

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
    
        global x
        x = x-1

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val =datapoint['value']

        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'value':val,
                'x':x
            }
        )
 

        # pass

    async def deprocessing(self,event):
        valOther=event['value']
        await self.send(text_data=json.dumps({'value':valOther,'x':x}))
