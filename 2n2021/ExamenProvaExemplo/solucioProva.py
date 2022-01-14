# Implementar els mètodes que permeten gestionar els usuaris fans d’un usuari i
# bloquejar-los si és el cas. A tal efecte, haureu de gestionar els mètodes

# 1. show: Mostra la informació completa d’un usuari i dels nicks dels seus fans.

# 2. listFans: permet obtenir tota la informació dels fans d’un usuari.

# 3. blockUser: ha de permetre bloquejar un usuari, tan si és fan com si no. En el cas
# que sí que sigui fan, l’ha d’esborrar de la collection de fans. Tanmateix, caldrà
# afegir-ne el nick a la collection de fans bloquejats.

# 4. listBlocked: permet obtenir els nicks dels fans bloquejats.

# 5. addFan: ha de permetre afegir un fan a la collection de fans de l’user. No es pot
# afegir un fan que s’ha bloquejat prèviament (que apareix a la collection de blocked
# de l’usuari en qüestió).

import time

class User(object):
    def __init__(self,nom,email):
        self.nick=nom
        self.email=email
        self.fans={} #dicc
        self.posts=[]
        self.__blocked=[]
        
    def show(self):
        print("nick --> "+self.nick)
        print("email --> "+self.email)
        if len(self.fans)==0:
            print("No fans yet")
        else:
            text="Fans_list_nicks --> "
            for i,fan in enumerate(self.fans):
                if i==(len(self.fans)-1):#Mira si es el ultimo. para no termianr en ","
                    text+=fan
                else:
                    text+=fan+", "
            print(text)
        if len(self.posts)==0:
            print("No posts yet")
        else:   
            print("posts :", self.posts)
        
    def addFan(self, fan):
        if fan.nick not in self.__blocked: #si no esta en blockeds
            self.fans[fan.nick]=fan #añade nick en fans
        else:
            print("Not allowed")
        
    def listFans(self):
        for fan in self.fans:
            self.fans[fan].show()
            
    def blockUser(self, user):
        self.__blocked.append(user.nick) #añade en bloqueds
        if user.nick in self.fans: #si esta en fans
            del self.fans[user.nick] #elimina dels fans
        
    def listBlocked(self):
        if len(self.__blocked)==0:
            print("No blocked fans")
        else:
            text="Blocked users --> "
            for i,fan in enumerate(self.__blocked):
                if i==(len(self.__blocked)-1):
                    text+=fan
                else:
                    text+=fan+", "
            print(text)
    
    def post(self,p): # apartat b)
        dataActual = time.strftime("%c")
        #definir var
        hashtag=""
        hashtags=[]
        friend=""
        friends=[]
        text=""
        #boleands
        hash_flag=False
        friend_flag=False
        text_flag=True

        for lletra in p:
            if lletra=="#":
                hash_flag=True
                text_flag=False
            elif lletra=="@":
                friend_flag=True
                text_flag=False                

            if text_flag:
                text+=lletra
            elif hash_flag:
                if lletra==" ":
                    #a un espacio quita el hast añade la frase a la llista y vacia el string
                    hash_flag=False
                    hashtags.append(hashtag)
                    hashtag=""
                else:
                    hashtag+=lletra

            elif friend_flag:
                if lletra==" ":
                    friend_flag=False
                    friends.append(friend)
                    friend=""
                else:
                    friend+=lletra
        # Per l'últim hashtag o últim friend, ja que no trobarà un espai:
        if hash_flag==True:
            hashtags.append(hashtag)
        elif friend_flag==True:
            friends.append(friend)

        #-- lo añade a la otra clase --
        post=Post(text,dataActual)

        for hashtag in hashtags:
            post.addHashtag(hashtag)#def en el post class
            
        for friend in friends:
            if friend[1:] not in self.__blocked:
                post.addFriend(friend) #def en el post class

        self.posts.append(post) #lo que salga de class post lo guarda en la lista de post
        
    def printPostsDate(self):
        for post in self.posts:
            post.show()
            print()

class Post(object): # apartat b)
    def __init__(self,text,date):
        self.content=text
        self.date=date
        self.hashtags=[]
        self.friends=[]
        
    def show(self):
        print("Content --> "+self.content)
        print("Date --> "+self.date)
        if len(self.hashtags)!=0:
            text="Hashtags --> "
            for has in self.hashtags:
                text+=has+" "
            print(text)
        if len(self.friends)!=0:
            text="Labbeled users --> "
            for fri in self.friends:
                text+=fri+" "
            print(text)
            
    def addHashtag(self,h):
        self.hashtags+=[h]
        
    def addFriend(self,f):
        self.friends+=[f]

if __name__=="__main__":
    print("Apartat a)\n")

    g=User("pere","pere@daw.com")
    h=User("anna","anna@daw.com")
    l=User("maria","maria@daw.com")
    k=User("dimoni","dimoni@daw.com")
    g.addFan(h)
    g.addFan(l)
    g.show()                        #1
    print()
    g.listFans()                    #2
    print()
    g.blockUser(k)                  #3
    g.addFan(k)
    print()
    g.show()                        #4
    print()
    g.listBlocked()                 #5
    print("\n")
    
    print("Apartat b)\n")
    g=User("pere","pere@daw.com")
    l=User("maria","maria@daw.com")
    g.addFan(l)
    g.blockUser(l)
    g.post("Next starting project #newproject #newversion #workingcopy @eva @maria @jordina")
    g.post("Holidays are comming #finishing_project")
    g.post("End of exams @jordi @eva @maria")
    g.post("no way")
    g.printPostsDate()