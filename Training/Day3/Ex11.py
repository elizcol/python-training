'''
Created on 26 Nov 2014

@author: b8605521
'''
import asyncio

class Server(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        transport.write(b"time is")
        
class Client:
    pass
#mock stuff!    
loop = asyncio.get_event_loop()
server = loop.run_until_complete(loop.create_server(Server, '', 65530))
if __name__ == '__main__':
    pass