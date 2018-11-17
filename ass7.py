# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mohak Chavan"
__date__ = "$14 Nov, 2018 4:32:41 PM$"

data0 = []
data1 = []
data2 = []
i = 0
FILEPATH = "E:\\Google Drive\\PICT\\LP - 1\\Assignment 7\\New folder\\"


# equal-frequency
def equal_freq():
    print("\n\nEnter frequency for each Bin:")
    freq = int(input())
    f = open(FILEPATH + "equal_freq.csv", "w")
    f.write("Equal-Frequency Partitioning for Dataset0\nBin-1")
    x = 0
    bin = 1
    for j in range(0, len(data0)):
        if (x < freq):
            f.write("," + str(data0[j]))
            x += 1
        else:
            bin += 1
            x = 0
            f.write("\nBin-" + str(bin) + "," + str(data0[j]))
            x += 1
    f.write("\n\nEqual-Frequency Partitioning for Dataset1\nBin-1")
    x = 0
    bin = 1
    for j in range(0, len(data1)):
        if (x < freq):
            f.write("," + str(data1[j]))
            x += 1
        else:
            bin += 1
            x = 0
            f.write("\nBin-" + str(bin) + "," + str(data1[j]))
            x += 1
    f.write("\n\nEqual-Frequency Partitioning for Dataset2\nBin-1")
    x = 0
    bin = 1
    for j in range(0, len(data2)):
        if (x < freq):
            f.write("," + str(data2[j]))
            x += 1
        else:
            bin += 1
            x = 0
            f.write("\nBin-" + str(bin) + "," + str(data2[j]))
            x += 1
    f.close()
    print("\nEqual-Frequency Partitioning written in \"" + f.name + "\" file.")


# equal-width
def equal_width():
    print("\n\nEnter width of each Bin:")
    width = int(input())
    f = open(FILEPATH + "equal_width.csv", "w")
    sdata0 = data0[:]
    sdata1 = data1[:]
    sdata2 = data2[:]
    sdata0.sort()
    sdata1.sort()
    sdata2.sort()
    f.write("Equal-Width Partitioning for Dataset0\nBin-1")
    bin = 1
    # wri = 0
    last = sdata0[0] + width
    for j in range(0, len(sdata0)):
        if sdata0[j] <= last:
            f.write("," + str(sdata0[j]))
            # wri += 1
        else:
            bin += 1
            f.write("\nBin-" + str(bin) + "," + str(sdata0[j]))
            # wri += 1
            last = sdata0[j] + width
    # print(str(i) + "\t" + str(wri))
    f.write("\n\nEqual-Width Partitioning for Dataset1\nBin-1")
    bin = 1
    # wri = 0
    last = sdata1[0] + width
    for j in range(0, len(sdata1)):
        if sdata1[j] <= last:
            f.write("," + str(sdata1[j]))
            # wri += 1
        else:
            bin += 1
            f.write("\nBin-" + str(bin) + "," + str(sdata1[j]))
            # wri += 1
            last = sdata1[j] + width
    # print(str(i) + "\t" + str(wri))
    f.write("\n\nEqual-Width Partitioning for Dataset2\nBin-1")
    bin = 1
    # wri = 0
    last = sdata2[0] + width
    for j in range(0, len(sdata2)):
        if sdata2[j] <= last:
            f.write("," + str(sdata2[j]))
            # wri += 1
        else:
            bin += 1
            f.write("\nBin-" + str(bin) + "," + str(sdata2[j]))
            # wri += 1
            last = sdata2[j] + width
    # print(str(i) + "\t" + str(wri))
    f.close()
    print("\nEqual-Width Partitioning written in \"" + f.name + "\" file.")


# Normalization
def normalization(m0, m1, m2, s0, s1, s2):
    mini0 = data0[0]
    mini1 = data1[0]
    mini2 = data2[0]
    maxi0 = data0[0]
    maxi1 = data1[0]
    maxi2 = data2[0]
    # Finding Maximum Value
    for x in data0:
        if (x < mini0):
            mini0 = x
        if (x > maxi0):
            maxi0 = x
    for x in data1:
        if (x < mini1):
            mini1 = x
        if (x > maxi1):
            maxi1 = x
    for x in data2:
        if (x < mini2):
            mini2 = x
        if (x > maxi2):
            maxi2 = x

    # Finding Minimum Value
    for x in range(0, i):
        if (data0[x] < mini0):
            mini0 = data0[x]
        if (data0[x] > maxi0):
            maxi0 = data0[x]
        if (data1[x] < mini1):
            mini1 = data1[x]
        if (data1[x] > maxi1):
            maxi1 = data1[x]
        if (data2[x] < mini2):
            mini2 = data2[x]
        if (data2[x] > maxi2):
            maxi2 = data2[x]

    #    print("\nmini0: "+str(mini0)+"\tmaxi0:"+str(maxi0))
    #    print("\nmini1: "+str(mini1)+"\tmaxi1:"+str(maxi1))
    #    print("\nmini2: "+str(mini2)+"\tmaxi2:"+str(maxi2))

    #    print("For Dataset0\n\tEnter new_min:")
    #    nmin0 = int(input())
    #    print("\n\tEnter new_max:")
    #    nmax0 = int(input())
    #    print("\nFor Dataset1\n\tEnter new_min:")
    #    nmin1 = int(input())
    #    print("\n\tEnter new_max:")
    #    nmax1 = int(input())
    #    print("\nFor Dataset2\n\tEnter new_min:")
    #    nmin2 = int(input())
    #    print("\n\tEnter new_max:")
    #    nmax2 = int(input())

    nmax0 = 1
    nmin0 = 0
    nmax1 = nmax0
    nmax2 = nmax0
    nmin1 = nmin0
    nmin2 = nmin0

    f = open(FILEPATH + "normalized_dataset.csv", "w")
    # f = open("normalized_dataset.csv", "w")
    f.write(
        "Normalized0,Normalized1,Normalized2,Z-Score0,Z-Score1,Z-Score2,Decimal_Scaling0,Decimal_Scaling1,Decimal_Scaling2\n")
    c0 = data0.count(maxi0)
    c1 = data1.count(maxi1)
    c2 = data2.count(maxi2)
    for x in range(0, i):
        nval0 = (((data0[x] - mini0) / (maxi0 - mini0)) * (nmax0 - nmin0)) + nmin0
        nval1 = (((data1[x] - mini1) / (maxi1 - mini1)) * (nmax1 - nmin1)) + nmin1
        nval2 = (((data2[x] - mini2) / (maxi2 - mini2)) * (nmax2 - nmin2)) + nmin2
        z0 = (data0[x] - m0) / s0
        z1 = (data1[x] - m1) / s1
        z2 = (data2[x] - m2) / s2
        ds0 = data0[x] / (10 ** c0)
        ds1 = data1[x] / (10 ** c1)
        ds2 = data2[x] / (10 ** c2)
        f.write(str(nval0) + "," + str(nval1) + "," + str(nval2) + "," + str(z0) + "," + str(z1) + "," + str(
            z2) + "," + str(ds0) + "," + str(ds1) + "," + str(ds2) + "\n")
    f.close()
    print("\n\nNormalized values are stored in \"" + f.name + "\" file.")


# Standard Deviation
def standard_deviation(data, mean):
    sd = 0
    for x in data:
        sd += ((x - mean) ** 2)
    sd = (sd / len(data)) ** (0.5)
    # print "Standard Deviation first dataset = "+str(sd)
    return sd


#
#
#
# Main Function Starting from here
#
#
#
# reading dataset from file
fr = open(FILEPATH + "dataset.csv", "r")
fr.readline()
sum0 = 0
sum1 = 0
sum2 = 0

for line in fr:
    data0.append(round(float(line.split(",")[0]), 3))
    data1.append(round(float(line.split(",")[1]), 3))
    data2.append(round(float(line.split(",")[2]), 3))
    sum0 += float(line.split(",")[0])
    sum1 += float(line.split(",")[1])
    sum2 += float(line.split(",")[2])
    i += 1
fr.close()

# calculating mean
mean0 = sum0 / i
mean1 = sum1 / i
mean2 = sum2 / i

# calculating median
length = int(i / 2)
sdata0 = data0[:]
sdata1 = data1[:]
sdata2 = data2[:]
sdata0.sort()
sdata1.sort()
sdata2.sort()
if ((i % 2) == 0):
    median0 = (sdata0[length] + sdata0[length + 1]) / 2
    median1 = (sdata1[length] + sdata1[length + 1]) / 2
    median2 = (sdata2[length] + sdata2[length + 1]) / 2
else:
    median0 = sdata0[length + 1]
    median1 = sdata1[length + 1]
    median2 = sdata1[length + 1]

# calculating SD
sd0 = standard_deviation(data0, mean0)
sd1 = standard_deviation(data1, mean1)
sd2 = standard_deviation(data2, mean2)

# Printing information
print("\nTotal Records: " + str(i))
print("\nFirst Dataset:\n\t\tMean:   \t\t" + str(mean0) + "\n\t\tMedian: \t\t" + str(
    median0) + "\n\t\tStandard Deviation: \t" + str(round(sd0, 2)))
print("\nSecond Dataset:\n\t\tMean:   \t\t" + str(mean1) + "\n\t\tMedian: \t\t" + str(
    median1) + "\n\t\tStandard Deviation: \t" + str(round(sd1, 2)))
print("\nThird Dataset:\n\t\tMean:   \t\t" + str(mean2) + "\n\t\tMedian: \t\t" + str(
    median2) + "\n\t\tStandard Deviation: \t" + str(round(sd2, 2)))

normalization(mean0, mean1, mean2, sd0, sd1, sd2)
equal_width()
equal_freq()
