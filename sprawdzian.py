napisy = open("napisy.txt")

zawartosc = napisy.read().split("\n")

liczba=0
konczySie1=0
palindrom=0
tylko1=0
tylko0=0
takaSamaLiczba=0
k1=0
k2=0
k3=0
k4=0
k5=0
k6=0
k7=0
k8=0
k9=0
k10=0
k11=0
k12=0
k13=0
k14=0
k15=0
k16=0

for znak in zawartosc:
    if len(znak)%2==0:
        liczba+=1
    if znak.endswith("1"):
        konczySie1+=1
    if znak == znak[::-1]:
        palindrom+=1
    if len(znak) == sum(map(int, str(znak))):
        if sum(map(int, str(znak))) > 0:
            tylko1+=1
        else:
            tylko0+=1
    if(len(znak)==2):
        k2+=1
    if (len(znak)==3):
        k3+=1
    if (len(znak)==4):
        k4+=1
    if (len(znak)==5):
        k5+=1
    if (len(znak)==6):
        k6+=1
    if (len(znak)==7):
        k7+=1
    if (len(znak)==8):
        k8+=1
    if (len(znak)==9):
        k9+=1
    if (len(znak)==10):
        k10+=1
    if (len(znak)==11):
        k11+=1
    if (len(znak)==12):
        k12+=1
    if (len(znak)==13):
        k13+=1
    if (len(znak)==14):
        k14+=1
    if (len(znak)==15):
        k15+=1
    if (len(znak)==16):
        k16+=1
    if znak.count("1") == znak.count("0"):
        takaSamaLiczba+=1

print("Liczba parzystych:", liczba)
print("Ile konczy sie na 1:", konczySie1)
print("Liczba palindromow:", palindrom)
print("Ile sklada sie tylko z 1:", tylko1)
print("Ile sklada sie tylko z 0:", tylko0)
print("Napisow z taka sama liczba 0 i 1:", takaSamaLiczba)
print("dlugosc 2:", k2, "\ndlugosc 3:", k3, "\ndlugosc 4:",k4,"\ndlugosc 5:",k5,"\ndlugosc 6:",k6,"\ndlugosc 7:",k7,"\ndlugosc 8:",k8,"\ndlugosc 9:",k9,"\ndlugosc 10:",k10,"\ndlugosc 11:",k11,"\ndlugosc 12:",k12,"\ndlugosc 13:",k13,"\ndlugosc 14:",k14,"\ndlugosc 15:",k15,"\ndlugosc 16:",k16)