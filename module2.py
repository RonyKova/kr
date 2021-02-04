with open('ucheniki.txt', 'r') as f:

    Ballsg = {}
    Clas =  {}
    Ballsa =  {}
    maxi = dict.fromkeys(['8','9','10','11'],0)
    maxa =dict.fromkeys(['8','9','10','11'],0)
    maxg = dict.fromkeys(['8','9','10','11'],0)
    lisa = list()
    lisg = list()
    lis = list()

    for i in f:  #определение максимума для каждого класса
        surname,name,clas,bala,balg = i.split()
        if (int(bala)+ int(balg)) > maxi[clas]:
            maxi[clas] = int(bala)+int(balg)

        if int(bala) > maxa[clas]:
            maxa[clas] = int(bala)

        if int(balg) > maxg[clas]:
            maxg[clas] = int(balg)


    for k in range(8,11): #поиск людей с максимальным баллом
        f.seek(0)
        for i in f:
                surname,name,clas,bala,balg = i.split()

                if clas == str(k):

                    if (int(bala)+ int(balg)) == maxi[clas]:
                        lis.append({surname+' '+name:maxi[clas]})
                        Clas = lis

                    if int(bala) == maxa[clas]:
                        lisa.append({surname+' '+name:maxa[clas]})
                        Ballsa= lisa

                    if int(balg)==maxg[clas]:
                        lisg.append({surname+' '+name:maxg[clas]})
                        Ballsg=lisg

        print(k)
        print('Победитель по всем предметам')
        print(Clas)
        print('Победитель по алгебре')
        print(Ballsa)
        print('Победитель по геометрии')
        print(Ballsg)

        lisa = list()
        lisg = list()
        lis = list()
        Ballsg = {}
        Clas =  {}
        Ballsa =  {}


