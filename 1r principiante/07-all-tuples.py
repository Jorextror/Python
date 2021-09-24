"""Jordi Oliveda
PROGRAMES EN PYTHON-07
En un sol programa fes les següents activitats (molt fàcils)
"""
ex=1
while ex != 0:
    ex=input("Quin exercici del 1-11? ")
    if ex == "1":
        print("Crea una tupla nova que sigui la tupla girada (al revés)")
        aTuple = (10, 20, 30, 40, 50)
        Tuple = tuple([aTuple[i] for i in range(4,-1,-1)]) #en la un altre vriable li fem un for in en range 5 i reduir -1 fins a -1
        print(Tuple)
        
    if ex == "2":
        print("Fes una tupla d’un sol element anomenada unSol i amb contingut 50")
        unSol=(50)#una tuple anomenat unSol que té "50"
        
    if ex == "3":
        print("Fes un swap de les següents tuples 2 versions, amb variable auxiliar i directament")
        tuple1 = (99, 88)
        tuple2 = (11, 22)
        
        #variable auxiliar
        temp = tuple1
        tuple1 = tuple2
        tuple2 = temp
        
        print(tuple1,tuple2)
        
        #directa
        tuple1,tuple2=tuple2,tuple1 #i fem un swap un altre cop pero directament amb les funcions de python.
        print(tuple1,tuple2)
        
    if ex == "4":
        print("Ordena la tupla pel segon element: algorismes treballats (bombolla, nan o inserció)")
        llista=[]
        resultat=[]
        tuple1=(('a', 23),('b', 37),('c', 11), ('d',29))
        for i in range(len(tuple1)):
            valor=tuple1[i][1]#treiem el num dels tuples i la posem en una llista
            llista.append(valor)
        #ordenacio per inccecció
        A=llista
        i=1
        while i < len(A):
            x=A[i] #guardem valor en X
            j=i-1
            while j >= 0 and A[j] > x: #si el valor de la x és més grand que el altre
                A[j+1]=A[j]
                j=j-1
            A[j+1]=x # posem el valor una pocisio menys
            i+=1
            #print(A)
        j=0
        #amb els num ordenats ara busquem els mateixos nums en las tuples
        for i in range(len(A)):
            for j in range(len(tuple1)):
                
                valor1=A[i]
                if valor1 in tuple1[j]:
                    resultat.append(tuple1[j])
        print(resultat)
        
    if ex == "5":
        print("Digues quantes vegades apareix el valor 50 en la tupla, i quin % representa?")
        tuple1 = (50, 10, 60, 70, 50)
        num=tuple1.count(50) #contem quants 50 hi han
        percent=2*100/5 #fem la mitjana per saber el porcentanje.
        print("Hi apareix",num,"50s",", i té ",percent,"% del total")

    if ex == "6":
        print("Comprova si tots els ítems de la tupla tenen el mateix valor")
        tuple1 = (45, 45, 45, 45)
        for el in tuple1:
            if max(tuple1)==el:#si és el núm el més alt
                print("El número,",el,"es igual al máxim")
                i=i+1 #un contador per mirar si tots son el mateix núm
                if i==3:
                    print("Tots els numeros tenen el mateix valor")
        
    if ex == "7":
        print("Com es crea una tupla buida? Com es converteix una tupla en una llista?")
        tuplaBuida=() #és un tuple buida
        list(tuplaBuida)#ara és una llista
        
    if ex == "8":
        print("Tenint una llista de números, escriviu un codi Python per crear una llista de tuples que tinguin el primer element com a número i el segon element com a cub del número.")
        print("Input: list = [1, 2, 3]")
        print("Output: [(1, 1), (2, 8), (3, 27)]")
        list1 = [1, 2, 3]
        lista2=[]
        for i in list1:
            afegit=i,i**3#El fem el valor al cub i ambe posem el valor sense al cup
            lista2.append(afegit)#Al afegim en una llista per anar guardan
        print(lista2)
        
    if ex == "9":
        print("Fes una llista de tuples de totes les combinacions  possibles de 2 tuples d'arguments. ")
        print("Input : t1 = (7, 2), t2 = (7, 8)")
        print("Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2),(8, 7), (8, 2)]")
        llista=[]
        t1 = (7, 2)
        t2 = (7, 8)
        
        for i in range(len(t1)):
            for j in range(len(t2)):
                r=t1[j],t2[i]
                r1=t2[i],t1[j]
                llista.append(r)
                llista.append(r1)
        print(llista)#no surt como el output de exemple pero suert les mateixes combinacios
    
    if ex == "10":
        print("Escriviu un codi en Python per trobar els elements repetits d’una llista i construeix una llista de tuples on surti en primer terme l’element i en segon terme quantes vegades apareix.")
        llista = [1,2,3,1,2,1,1]
        lista2=[]
        for i in range (len(llista)):
            vegades=0
            for j in llista:
                if llista[i]==j:#quanta els núm repetides
                    vegades+=1
            afegit=llista[i],vegades#La variable s'ajunta con el núm i el seu comtador
            if afegit not in lista2:#si no esta en la llista ho afegeix 
                lista2.append(tuple(afegit))
        
        print(lista2)
        
    if ex == "11":
        print("Troba en quina posició es troba l’element 20:")
        aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
        
        for i in aTuple:
            if "20" in str(i):#busca el 20 en la tuple
                print("El número 20 está a la posició",i,"de la tupla")#ja trobat el núm diu la pocisio amb el for
                for j in range(len(i)):#recore la pocision de la tuple
                    if i[j]==20:
                        print("Y a la posició ",j,"dins de un/a", type(i))#amb el type en diu que tipus és
                        
    else:
        if ex == "0" or ex < "11":
            ex=0