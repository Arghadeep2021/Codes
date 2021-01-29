import threading
import time

def sleeper(n,name):
    print('Hi, i am {}, going to sleep for 5 mins \n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n '.format(name))

#t = threading.Thread(target= sleeper, name = 'Thread1', args = (5, 'PyQt5'))
#t.start()

Thread_list= []

start = time.time()

for i in range(5):   #Parameter to call thread in the below line
    t = threading.Thread(target= sleeper, name = 'Thread{}'.format(i), args = (5, 'Thread{}'.format(i)))
    Thread_list.append(t)
    t.start()
    print('{} is getting started'.format(t.name))

for t in Thread_list:
    t.join()

end = time.time()

print('Time taken is {} '.format(end-start))
print('Process completed')