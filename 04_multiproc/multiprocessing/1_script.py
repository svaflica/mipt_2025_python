import multiprocessing as mp

def demoFunction(targetList,newElem,comment):
    targetList.append(newElem)
    print(comment, 'Inside demoFunction: ', targetList)


if __name__ == '__main__':
    myList = [1,2,3]
    demoFunction(myList, 4, 'Plain.')
    print('After "demoFunction" without multiprocessing', myList)

    p = mp.Process(target=demoFunction, args=[myList,5,'Multiprocessing.']) 
   

    p.start()
    p.join()

    print('After "demoFunction" with multiprocessing', myList)