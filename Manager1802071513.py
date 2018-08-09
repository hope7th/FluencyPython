import multiprocessing,time
def fun1(a,q):
    q.put(a)

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    q = manager.Queue()
    p = multiprocessing.Pool()
    x = [a for a in range(1,5)]
    print(x)
    while True:
        for each in x:
            p.apply_async(fun1,(each,q))
        # p.close()
        # p.join()
        print q.qsize()
        for i in range(q.qsize()):
            print "q.get()"
            print(q.get())
        time.sleep(3)