import random, sys, time, os
# make vertex with adjacency list
class Vertex:
    def __init__(self, name = None):
        self.next = []
        self.name = name
        self.visited = False
# function to find euler's cycle
def eulerCykl(graph):
    global yeah, find, cycle
    for i in graph:
        # check if vertex has even length of adjacency list
        if len(i.next) % 2 == 1 or len(i.next) == 0:
            print("Oops, Euler's cycle was not found")
            return
    yeah = True
    cycle = []
    # start from random point
    start = random.choice(graph)
    eulerCyklTemp(start)
    print("Found Euler's cycle", cycle)


def eulerCyklTemp(start):
    global cycle
    # return if vertex already exist
    if start.name in cycle:
        return
    for i in start.next:
    # remove from adjacency list of those vertexes and go next recursive
        start.next.remove(i)
        i.next.remove(start)
        eulerCyklTemp(i)
    # at the end add to the list of euler's cycle
    cycle.append(start.name)


def hamiltonCycle(graph):
    global yeah, solution, perm
    perm = 0
    solution = []
    temp = random.choice(graph)
    hamiltonCycleTemp(temp)
    if len(solution) > 0:
        print([j.name for j in solution])
    else:
        print("Graph has no Hamilton's cycle")
    print("Number of permutations that was used to found Hamilton's cycle ", perm)

def hamiltonCycleTemp(start):
    global yeah, perm
    # stop if more then 20 seconds
    if not possible:
        if time.clock() - startTimeHam > 20:
            yeah = True
            return
    perm += 1
    # stop if found
    if yeah:
        return
    global solution
    # mark as visited
    start.visited = True
    solution.append(start)
    # stop if found cycle
    if len(solution) == n:
        if start in solution[0].next:
            print(" Hamilton's cycle was founded ")
            yeah = True
            return
    # if wasn't visited recursive go to the next
    for i in start.next:
        if not i.visited:
            hamiltonCycleTemp(i)
    # if wasn't found clean list from this item
    if not yeah:
        solution.remove(start)
        start.visited = False

def makeList():
    """make list of edges
    In this function we make cycle and later add edges while their num won't equal to required
    :return:
    """
    global adjacencyList, edges
    adjacencyList = []
    for i in range(n):
        adjacencyList.append(Vertex(i))
    edges = 0
    adjacencyList[-1].next.append(adjacencyList[0])
    adjacencyList[0].next.append(adjacencyList[-1])
    edges += 1
    for i in range(len(adjacencyList) - 1):
        adjacencyList[i].next.append(adjacencyList[i + 1])
        adjacencyList[i + 1].next.append(adjacencyList[i])
        edges += 1
    while edges != m:
        temp = random.choice(adjacencyList)
        tempNext = random.choice(adjacencyList)
        if temp is not tempNext and tempNext not in temp.next:
            tempNext.next.append(temp)
            temp.next.append(tempNext)
            edges += 1
    # print("Adjacency list of graph")
    # for i in adjacencyList:
    #     print(i.name, [j.name for j in i.next])


def makeListWithThree():
    """
    In this function we add 3 edges while their num won't equal to required
    Everything is random.
    :return:
    """
    global adjacencyList, edges
    adjacencyList, edges = [], 0
    for i in range(n):
        adjacencyList.append(Vertex(i))
    while edges < m:
        i = random.choice(adjacencyList)
        tempNext = random.choice(adjacencyList)
        tempNext2 = random.choice(adjacencyList)
        if tempNext not in tempNext2.next and tempNext not in i.next and tempNext2 not in i.next and tempNext is not tempNext2 and tempNext is not i and tempNext2 is not i:
            i.next+=[tempNext2, tempNext]
            tempNext.next+=[i, tempNext2]
            tempNext2.next+=[tempNext, i]
            edges += 3
    # print("Adjacency list of graph")
    # for i in adjacencyList:
    #     print(i.name, [j.name for j in i.next])


def makeAcyclic():
    """
    Just isolate one vertex
    :return:
    """
    temp = random.randrange(len(adjacencyList))
    for i in adjacencyList[temp].next:
        i.next.remove(adjacencyList[temp])
    adjacencyList[temp].next = []


def test1():
    """
    Function to test for a 10 times euler's and hamilton's cycle
    :return:
    """
    global yeah, m, startTimeHam, n, possible
    possible = False
    minimum = input("Enter start point of test (number of vertexes): ")
    maximum = input("Enter finish point of test: ")
    if maximum.isdigit() and minimum.isdigit() and int(minimum) >= 10:
        for again in range(10):
            hamiltonTime, hamilton, euler, eulerTime = [], [], [], []
            maximum, minimum = int(maximum), int(minimum)
            nList = []
            # to avoid dif == 0
            if maximum - minimum < 10: dif = 1
            else: dif = (maximum - minimum) // 10
            for n in range(minimum, maximum, dif):
                nList.append(n)
                yeah = False
                m = int(n * (n - 1) // 2 * 0.7)
                makeList()
                print(" Number of vertexes is {} , number of edges is  {} ".format(n, edges))
                startTimeHam = time.clock()
                hamiltonCycle(adjacencyList)
                finishTimeHam = time.clock() - startTimeHam
                hamiltonTime.append(finishTimeHam)
                makeListWithThree()
                print(" Number of vertexes is {} , number of edges is  {} ".format(n, edges))
                startTimeEul = time.clock()
                eulerCykl(adjacencyList)
                finishTimeEul = time.clock() - startTimeEul
                eulerTime.append(finishTimeEul)
            file1 = open("hamilton70.txt", "a")
            file1.write("Test from {} to {}\n".format(minimum, maximum) + str(nList) + "\n" + str(hamiltonTime) + "\n")
            file1.close()
            file2 = open("euler70.txt", "a")
            file2.write("Test from {} to {}\n".format(minimum, maximum) +  str(nList) + "\n" + str(eulerTime) + "\n")
            file2.close()
        print("finished")

def test2():
    """
    Function to find hamilton's cycle in graph where it not exist
    :return:
    """
    global possible, yeah, m, n
    possible = True
    hamiltonTime, hamilton, euler, eulerTime = [], [], [], []
    minimum = input("Enter start point of test (number of vertexes): ")
    maximum = input("Enter finish point of test: ")
    if maximum.isdigit() and minimum.isdigit() and int(minimum) >= 10:
        maximum, minimum = int(maximum), int(minimum)
        nList = []
        if maximum - minimum < 10: dif = 1
        else: dif = (maximum - minimum) // 10
        for n in range(minimum, maximum, dif):
            nList.append(n)
            yeah = False
            m = int(n * (n - 1) // 2 * 0.5)
            makeList()
            # isolate vertex
            makeAcyclic()
            print(" Number of vertexes is {} , number of edges is  {} ".format(n, edges))
            startTimeHam = time.clock()
            hamiltonCycle(adjacencyList)
            finishTimeHam = time.clock() - startTimeHam
            hamiltonTime.append(finishTimeHam)
        print(eulerTime)
        print(hamiltonTime)
        file = open("nothamilton.txt", "a")
        file.write("Test from {} to {}\n".format(minimum, maximum) + str(nList) + "\n" + str(hamiltonTime) + "\n")
        file.close()


if __name__ == "__main__":
    # size up recursion limit
    sys.setrecursionlimit(100000000)
    # size up stack
    if os.name == "posix":
        os.system("ulimit -S -s 10000000")
        print("Changed size of stack")
    else: print("{:!^150}".format("I think that you computer won't works with more then 250 vertexes"))
    possible = True
    exit = False
    while not exit:
        opt = input("Choose option:\n"
                "1 \t to find in normal way Euler's cycle and Hamilton\'s cycle in graphs in input range\n"
                "2 \t to try find Hamilton\'s cycle in graph where cycle surely not exist\n"
                "3 \t to exit\n")
        if opt.isdigit():
            if int(opt) == 1: test1()
            elif int(opt) == 2: test2()
            else: exit = True
        if not exit:
            getch = input("Continue? ")
            if getch.lower() == "y" or getch.lower() == "yes": pass
            else: exit = True
