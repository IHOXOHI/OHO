import os

def view(ori,L1=1,L2=1):
    fil_ori = open(ori, "r")
    if L2 == 1:
        l = fil_ori.readline()
        while l != "":
            L2 += 1
            l = fil_ori.readline()
    fil_ori.close()
    fil_ori = open(ori, "r")
    if L1 != 1:
        l = fil_ori.readline()
        n = 1
        while n != L1:
            n += 1
            l = fil_ori.readline()
    text = ""
    n = 0
    while L1 <= L2:
        n+=1
        ligne = fil_ori.readline()
        text =  text + str(n) + " " + ligne + "\n"
        L1 += 1
    fil_ori.close()
    print(text)

def cp(ori, des,ch_lg=0, ch_txt=""):
    fil_ori = open(ori, "r")
    fil_des = open(des, "w")
    l = fil_ori.readline()
    n = 1
    while l != "":
        if n == int(ch_lg):
            text = str(ch_txt)
        else:
            text = str(l)
        fil_des.write(text)
        l = fil_ori.readline()
        n += 1
    fil_ori.close()
    fil_des.close()

def count(ori):
    fil_ori = open(ori, "r")
    n = 0
    l = fil_ori.readline()
    while l != "":
        n += 1
        l = fil_ori.readline()
    fil_ori.close()
    return n

def md(ori,ch_lg=0, ch_txt=""):
    fil_ori = open(ori, "r")
    fil_des = open('tempo.py', "w")
    l = fil_ori.readline()
    n = 1
    while l != "":
        if n == int(ch_lg):
            text = str(ch_txt)
        else:
            text = str(l)
        fil_des.write(text)
        l = fil_ori.readline()
        n += 1
    fil_ori.close()
    fil_des.close()

    fil_ori = open('tempo.py', "r")
    fil_des = open(ori, "w")
    l = fil_ori.readline()
    n = 1
    while l != "":
        if n == int(ch_lg):
            text = str(ch_txt)
        else:
            text = str(l)
        fil_des.write(text)
        l = fil_ori.readline()
        n += 1
    fil_ori.close()
    fil_des.close()

    os.remove('tempo.py')
