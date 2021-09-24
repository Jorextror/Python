"""Jordi Oliveda
PROGRAMES EN PYTHON-08
"""

ex=1
while ex != 0:
    ex=input("Quin exercici del 1-7? ")
    if ex == "1":
        print("Afegiu una llista d'elements a un conjunt determinat:")
        sampleSet = {"Yellow", "Orange", "Black"}
        sampleList = ["Blue", "Green", "Red"]
        my_set = ([sampleSet, sampleList])
        print(my_set)

    if ex == "2":
        print("Retorna un conjunt d’elements repetits")
        set1 = {10, 20, 30, 40, 50}
        set2 = {30, 40, 50, 60, 70}
        print(set1&set2) #& el simbol entre dos sets significa que de tots els conjunts de elemnts oh printea

    if ex == "3":
        print("Retorna un conjunt nou amb tots els elements dels dos conjunts eliminant els duplicats.")
        set1 = {10, 20, 30, 40, 50}
        set2 = {30, 40, 50, 60, 70}
        print(set1|set2) # el simbol | signifca la unio de dos sets
        
    if ex == "4":
        print("Tenint en compte dos conjunts de Python, actualitzeu el primer conjunt amb elements que només existeixen al primer conjunt i no al segon conjunt.")
        set1 = {10, 20, 30}
        set2 = {20, 40, 50}
        print(set1-set2) #el simbol - és per fer diferencias de un set a un altre. elemnts que no estan en el altre.
        
    if ex == "5":
        print("Traieu 10, 20, 30 element d'un conjunt següent alhora")
        set1 = {10, 20, 30, 40, 50}
        set2 = {10, 20, 30}
        print(set1-set2) # per borrar un conjunt de caracters al mateix temps he creat un set dels caracters que no volia i le fet una diferencial
        
    if ex == "6":
        print("Cerqueu si una cadena introduïda per teclat té caràcters únics.")
        text1 = "pala"
        text2 = set(text1)
        if len(text1) > len(text2):#si text1 té més paraules que text2 es perque hi ha duplicats. cuan es pasa caracters a set borra totos els duplicats
            rest=len(text1)-len(text2)#resto las longituts per saber cuants duplicats hi ha
            print(text1,"=> tè",rest,"duplicats" )
        if len(text1) == len(text2):#si no disminueix la longitut és que no hi ha duplicats
            print(text1,"=> Tè caracters únics")
        
    if ex == "7":
        print("Donades les variables TEX1 i TEX2  que trobaràs a https://repl.it/join/ontzbvzb-pilarmote que contenen textos de Josep Carner i Manuel de Pedrolo respectivament, utilitzeu de manera òptima els coneixements apresos fins ara per respondre a les següents preguntes:")
        TEXT1 = "Com les maduixes Menja maduixes l’àvia d’abans de Sant Joan; per més frescor, les vol collides d’un infant. Per això la néta més petita, que és Pandara, sabeu, la que s’encanta davant d’una claror i va creixent tranquil·la i en ‘admiració i a voltes, cluca d’ulls, aixeca al cel la cara, ella, que encar no diu paraules ben ardides i que en barreja en una música els sentits, cull ara les maduixes arrupides, tintat de rosa el capciró dels dits. Les prunes d’or Aglaia té una set que eixuga el seny, la parla… Superbament s’aixeca, damnant el seu descans, i enfonsa en la prunera les cobejoses mans i enlaira tot el rostre, com si volgués besar-la. I l’arbre, que amb un lleu serpejament de branques sembla oferir-nos l’or, la mel d’algun pecat, s’estremeix un moment de la ferocitat del gran perfum impúdic i de les dents tan blanques. XVI Els codonys tardorals Però ja saps com elles es tornen malgirbades  per fills i feines, o perquè no n’han tingut, i amb cara tediosa caminen desmarxades i són codonys, diries, el fruit més boterut—. I l’altre amic que deia: —Quan fina tot esclat, nosaltres rondinem, esgarriant les passes, i flagel·lem el dia amb folles amenaces, saturns a la memòria del goig mal escampat. Llavores, el codony, que es féu vell en la branca,  dins el calaix perfuma la nostra roba blanca, i si l’amorosim al caliu de la llar i l’acostem als llavis sorruts, és dolç, encar."
        TEXT2 = "Ho havia planificat tot durant 20 anys. S’havia desfet de tot i de tothom. Estava segur que, en aquells moments, ja no el coneixia ningú. No quedava cap fotografia amb el seu veritable físic. I havia tingut tantes identitats diferents que ni ell es recordava de totes. Ara havia decidit començar una nova vida en un lloc on no el coneixia ningú. Era un poble qualsevol que un dia va veure mentre feia un viatge. Havia pensat que seria un bon lloc per començar de zero. El trajecte era la part més difícil. A l’estació va comprar un bitllet de tren nocturn amb destinació a Manchester. No volia que el busquessin enlloc. Baixaria al poble que havia triat abans d’arribar a la ciutat. També s’havia preocupat pel físic: ara duia bigoti i inflava les galtes d’una manera que li canviava la cara. Dret al passadís va esperar la sortida del tren. I va encendre l’última cigarreta, perquè a la nova vida pensava desfer-se d’aquest costum. El tabac li va semblar més bo que altres vegades i va fumar lentament, per fer durar el plaer."
        punt = (",",".",";")
        con=0#contador para saber que ahi dos a
        #pregunta1
        print("punt1")
        TEXT1low= TEXT1.lower()#per posarlo en minuscula
        TEXT2low= TEXT2.lower()

        TEXT1supr=[i for i in TEXT1low if i not in punt]#per borar el (,.;)
        TEXT2supr=[i for i in TEXT2low if i not in punt]
        print(TEXT1supr)
        print(TEXT2supr)
        
        
        #Pregunta 2
        print("punt2")
        TEXT1P=[i for i in TEXT1low.split()]#converteixo en strings per palaures
        TEXT2P=[i for i in TEXT2low.split()]
        
        print("El text1 té",len(TEXT1P),"i el text2 té",len(TEXT2P))#amb un len podem saber cuantes paraules té ara
        #Pregunta 3
        palabrasA=[]
        print("punt3")
        for i in TEXT1P:
            if "a" in i:#miru si hi ha palaures que contingui a
                con=0
                for j in range(len(i)): #pasu la palaure que conte una a
                    if i[j]=="a": #si en aquesta pocisio té una a
                        con+=1 #suma les vegades que té una a per palaure
                    if con == 2:
                        if i in TEXT2P:
                            palabrasA.append(i)
        print(palabrasA)
        #Pregunta 4
        print("punt4")
        acc="áàéèíìóòúù"
        accents=[]
        accents2=[]
        for i in TEXT1P:#pasa per paraules per el splin
            for j in i:#pasa per caracter de la paraule
                if j in acc:#si te alguna vocal amb accent
                    if i in TEXT2P:#si té la paraule altre text
                        accents.append(i)#la afexim a una lista
        print(accents)
        #Pregunta 5
        print("punt 5")
        especial="'-·"
        paraulesespecials=[]
        for i in TEXT1P:
            for j in i:
                if j in especial:#lo mateix que abans for de paraule, caracter i si té lo que busquem
                    if i not in TEXT2P:#si altre text no ho te
                        paraulesespecials.append(i)
        print(paraulesespecials)
        #Pregunta 6
        print("punt 6")
        vocal="aeiouàèìòùáéíóú"
        conv=0
        listvocal=[]
        listvocal2=[]
        for i in TEXT1P:
            for j in i:
                if j in vocal:#lo mateix de abans, for per paraule, per caracter, si hi ha el caracter que busquem
                    conv+=1#sumo els caracters de vocals per paraule
                    if conv==4:#si té 4 vocals una paraule
                        listvocal.append(i)
        for i in TEXT2P:
            conv=0
            for j in i:
                if j in vocal:
                    conv+=1
                    if conv==4:
                        listvocal2.append(i)
        print("Paraules amb 4 vocals que no comparteixen en els dos texts:",set(listvocal) ^ set(listvocal2)) #la converteixo en set i faix una diferencia simetrica. és un conjunt dels elements que no esta en el altre.

    else:
        if ex == "0" or ex < "8":
            ex=0