class scanThread(threading.Thread): 
def __init__(self): 
threading.Thread.__init__(self)  
def run(self): 
while True: 
c, addr = s.accept()
lists.append({'client': c, 'address': addr}) 
receiveThread(c, addr).start()
print lists
print 'Got connection from', addr
c.send('Thank you for connecting')  






class receiveThread(threading.Thread): 
def __init__(self, client, address): 
threading.Thread.__init__(self) 
self.client = client 
self.address = address  
def run(self): 
while True: 
msg = self.client.recv(1024) 
if msg: 
print msg
                 for receiver in lists:
                     if receiver['address'] != self.address:
                         receiver['client'].sendall(msg)
