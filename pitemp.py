import dateparser
import matplotlib.pyplot as plt

def parse_time(line):
    d = " ".join(line.split(" ")[2:-1])
    return dateparser.parse(d)

def parse_temp(line):
    d = line.split(" ")[0]
    return int(d)/1000

t=[]
w=[]

for i,line in enumerate(open("CpuTempLog.txt").readlines()):
    if i==0:
        continue
    t.append(parse_time(line))
    w.append(parse_temp(line))

plt.plot(t, w)
plt.show()
