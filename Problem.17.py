def tanimla(sayi):
    global rakam
    if(sayi<10):
        if(sayi==1):
            rakam="one"
        if(sayi==2):
            rakam="two"
        if(sayi==3):
            rakam="three"
        if(sayi==4):
            rakam="four"
        if(sayi==5):
            rakam="five"
        if(sayi==6):
            rakam="six"
        if(sayi==7):
            rakam="seven"
        if(sayi==8):
            rakam="eight"
        if(sayi==9):
            rakam="nine"
    elif(sayi>9 and sayi<20):
        if(sayi==10):
            rakam="ten"
        if(sayi==11):
            rakam="eleven"
        if(sayi==12):
            rakam="twelve"
        if(sayi==13):
            rakam="thirteen"
        if(sayi==14):
            rakam="fourteen"
        if(sayi==15):
            rakam="fifteen"
        if(sayi==16):
            rakam="sixteen"
        if(sayi==17):
            rakam="seventeen"
        if(sayi==18):
            rakam="eighteen"
        if(sayi==19):
            rakam="nineteen"
    elif(sayi>19 and sayi<100):
        sayi=str(sayi)
        if(sayi[0]=="2"):
            rakam="twenty"
        if(sayi[0]=="3"):
            rakam="thirty"
        if(sayi[0]=="4"):
            rakam="fourty"
        if(sayi[0]=="5"):
            rakam="fifty"
        if(sayi[0]=="6"):
            rakam="sixty"
        if(sayi[0]=="7"):
            rakam="seventy"
        if(sayi[0]=="8"):
            rakam="eighty"
        if(sayi[0]=="9"):
            rakam="ninety"
        
        if(sayi[1]=="1"):
            rakam+="one"
        if(sayi[1]=="2"):
            rakam+="two"
        if(sayi[1]=="3"):
            rakam+="three"
        if(sayi[1]=="4"):
            rakam+="four"
        if(sayi[1]=="5"):
            rakam+="five"
        if(sayi[1]=="6"):
            rakam+="six"
        if(sayi[1]=="7"):
            rakam+="seven"
        if(sayi[1]=="8"):
            rakam+="eight"
        if(sayi[1]=="9"):
            rakam+="nine"
    elif(sayi>99 and sayi<1000):
        sayi=str(sayi)

        if(sayi[0]=="1"):
            rakam="onehundredand"
        if(sayi[0]=="2"):
            rakam="twohundredand"
        if(sayi[0]=="3"):
            rakam="threehundredand"
        if(sayi[0]=="4"):
            rakam="fourhundredand"
        if(sayi[0]=="5"):
            rakam="fivehundredand"
        if(sayi[0]=="6"):
            rakam="sixhundredand"
        if(sayi[0]=="7"):
            rakam="sevenhundredand"
        if(sayi[0]=="8"):
            rakam="eighthundredand"
        if(sayi[0]=="9"):
            rakam="ninehundredand"
        
        if(sayi[1]=="2"):
            rakam+="twenty"
        if(sayi[1]=="3"):
            rakam+="thirty"
        if(sayi[1]=="4"):
            rakam+="fourty"
        if(sayi[1]=="5"):
            rakam+="fifty"
        if(sayi[1]=="6"):
            rakam+="sixty"
        if(sayi[1]=="7"):
            rakam+="seventy"
        if(sayi[1]=="8"):
            rakam+="eighty"
        if(sayi[1]=="9"):
            rakam+="ninety"

        if(sayi[2]=="1"):
            rakam+="-one"
        if(sayi[2]=="2"):
            rakam+="-two"
        if(sayi[2]=="3"):
            rakam+="-three"
        if(sayi[2]=="4"):
            rakam+="-four"
        if(sayi[2]=="5"):
            rakam+="-five"
        if(sayi[2]=="6"):
            rakam+="-six"
        if(sayi[2]=="7"):
            rakam+="-seven"
        if(sayi[2]=="8"):
            rakam+="-eight"
        if(sayi[2]=="9"):
            rakam+="-nine"
        if(sayi==1000):
            rakam="onethousand"

    return len(rakam);

toplam=0
for i in range(1,1001,1):
    toplam+=tanimla(i)
print(toplam)
