import matplotlib.pyplot as plt

for ls in [["euler", "euler70"], ["hamilton", "hamilton70"], ["nothamilton"]]:
    for name in ls:
        data = open("{}.txt".format(name), "r").read().split("\n")
        x = []
        y = []
        temp = []
        tempY= []
        for i in range(2, len(data), 3):
            temp.append(eval(data[i]))
        for k in range(len(temp[0])):
            tempSum, n = 0, 0
            for j in temp:
                tempSum += float(j[k])
                n += 1
            tempSum = tempSum / n
            x.append(tempSum)
        tempSum = 0
        n = 0
        y = eval(data[1])
        print(x, y)
        plt.plot(y, x)
    if len(ls) == 2 : plt.legend(["30%", "70%"])
    plt.title(ls[0])
    plt.xlabel("n (num of edges)")
    plt.ylabel("time (seconds)")
    plt.savefig(ls[0]+".jpg")
    plt.show()