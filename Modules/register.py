import binascii
def call(username,pasw):
    f = open("Modules/userid.txt",'r')
    for i in f:
        a = i.split()
        yes = binascii.a2b_uu(a[0])
        hmm = yes.decode("utf-8")
        if hmm == username:
            f.close()
            return -1
        v1 = f.readline()
    
    f.close()
    f = open("Modules/userid.txt","ab")
    username = bytes(username, 'utf-8')
    username = binascii.b2a_uu(username)
    pasw = bytes(pasw, 'utf-8')
    pasw = binascii.b2a_uu(pasw)
    f.write(username)
    f.write(pasw)
    f.close()
    return 0


def check(username,pasw):
    f = open("Modules/userid.txt",'r')
    flag = 0
    for inp in f:
        a = inp.split()
        yes = binascii.a2b_uu(a[0])
        hmm = yes.decode("utf-8")
        if hmm == username:
            flag = 1
            break
        v = f.readline()
    
    if flag == 0:
        f.close()
        return -1

    pas = f.readline()
    pa = pas.split()
    yes = binascii.a2b_uu(pa[0])
    hmm = yes.decode("utf-8")
    if hmm == pasw:
        f.close()
        return 0
    else:
        f.close()
        return -1
