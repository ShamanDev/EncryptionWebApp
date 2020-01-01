import random
k=random.randint(2,9)
class cezar():
    @staticmethod
    def szyfruj(x):
        h = ""
        x=x.lower()
        for i in x:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                z = ord(i) + k
                if (z > ord('z')):
                    z -= 26
            elif i == " ":
                z = 32
            h += chr(z)
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            z = ord(i) + k
            if (z > ord('Z')):
                z -= 26
            h += chr(z)
        h+=str(k)
        return h
    @staticmethod
    def deszyfruj(x):
        c=x.replace("","")
        c=int(x[len(x)-1])
        g = ""
        for i in x:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                z = ord(i)-c 
                if (z < ord('a')):
                    z += 26
                g += chr(z)
            if ord(i) >= ord('A') and ord(i) <= ord('Z'):
                z = ord(i)-c 
                if (z < ord('A')):
                    z += 26
                g += chr(z)
            if i == " ":
                g+=" "
        return g
