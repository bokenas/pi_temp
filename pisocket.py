import time
from threading import Thread, sleep 
I=0
def incr():
    global I
    while True:
        I+=1
        sleep(1)

t=Thread(target=incr)

t.run()
print("thread running")
time.sleep(10)

print(I)


