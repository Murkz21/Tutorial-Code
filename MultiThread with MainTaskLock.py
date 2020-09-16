import threading as th
import time as ti

threadLock = th.Lock()

class mainThread(th.Thread):
    def __init__ (self, threadId, name, count):
        th.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count
    def run(self):
        print('Start {}!\n'.format(self.name))
        threadLock.acquire()
        print_time(self.name, 1, self.count)
        threadLock.release()
        print('{} Ended!\n'.format(self.name))
        
class auxThread(th.Thread):
    def __init__ (self, threadId, name, count):
        th.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count
    def run(self):
        print('Start {}!\n'.format(self.name))
        threadLock.acquire()
        threadLock.release()
        print_time(self.name, 1, self.count)
        print('{} Ended!\n'.format(self.name))

def print_time(name, delay, count):
    while count:
        ti.sleep(delay)
        print('{} {} {}'.format(name, ti.ctime(ti.time()), count))
        count -= 1

payment = mainThread(1, "Payment",6)
email = auxThread(2, 'Sending Email',12)
complete = auxThread(3, 'Loading Complete Page',6)

payment.start()
email.start()
complete.start()

payment.join()
email.join()
complete.join()

print('Done and Exit!')
