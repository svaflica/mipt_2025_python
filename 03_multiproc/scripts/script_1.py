import multiprocessing
import os


def myFunc(i):
    print ('calling myFunc from process %s' %i, "pid: ", str(os.getpid()))
    for j in range (0,i):
        print('output from myFunc is :%s' %j)

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()