#archivo-salida.py
i = 33
f = open ('ascii.txt','a')
while(i<128):
    f.write(chr(i) + '\n' )
    i +=1
f.close()

f = open("ascii.txt", "r")
print(f.read())
