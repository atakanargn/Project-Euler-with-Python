import numpy as np
sayi="75*"
sayi+="95 64*"
sayi+="17 47 82*"
sayi+="18 35 87 10*"
sayi+="20 04 82 47 65*"
sayi+="19 01 23 75 03 34*"
sayi+="88 02 77 73 07 63 67*"
sayi+="99 65 04 28 06 16 70 92*"
sayi+="41 41 26 56 83 40 80 70 33*"
sayi+="41 48 72 33 47 32 37 16 94 29*"
sayi+="53 71 44 65 25 43 91 52 97 51 14*"
sayi+="70 11 33 28 77 73 17 78 39 68 17 57*"
sayi+="91 71 52 38 17 14 91 43 58 50 27 29 48*"
sayi+="63 66 04 68 89 53 67 30 73 16 69 87 40 31*"
sayi+="04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"


matris=np.zeros((15,15))
ySayi=sayi.split('*')
print(len(ySayi))

for i in range(0,len(ySayi)+1,1):
    satirSayi=ySayi[i].split(' ')
    for j in range(0,len(satirSayi)+1,1):
        matris[i][j]=satirSayi[j]

print(matris)