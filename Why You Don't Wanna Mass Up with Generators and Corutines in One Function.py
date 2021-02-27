def gen_num():
    i = 0
    while i < 10:
        i += 1
        rec_msg = yield i
        print(f'Received Message: {rec_msg}')
        
g = gen_num()
g.send(None)

send_value = None

for num in gen_num(): # The for-loop will next()/send(None) to the coroutine but not change the yield value for coroutine...
    try:
        g.__next__() # Every __next__()/send(None) and send() will increase Coroutine Yield Number by 1
        next(g) # Same as g.__next__() and send(None)
        print(f'Coroutine Yield Number: {send_value}')
        send_value = g.send(1000*num) # Send back the yield number of the coroutine to 'send_value'.
        print(f'Coroutine Yield Number: {send_value}')
        print(f'For Loop Yield Number: {num}')
    except StopIteration:
        break

'''
Output as follow:

Received Message: None
Received Message: None
Coroutine Yield Number: None
Received Message: 1000
Coroutine Yield Number: 4
For Loop Yield Number: 1
Received Message: None
Received Message: None
Received Message: None
Coroutine Yield Number: 4
Received Message: 2000
Coroutine Yield Number: 7
For Loop Yield Number: 2
Received Message: None
Received Message: None
Received Message: None
Coroutine Yield Number: 7
Received Message: 3000
Coroutine Yield Number: 10
For Loop Yield Number: 3
Received Message: None
Received Message: None
'''
