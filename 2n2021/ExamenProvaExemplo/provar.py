class User(object):
    def __init__(self,nom,email):
        self.nick=nom
        self.email=email
        self.fans={}
        self.posts=[]
        self.__blocked=[]
    def show(self):
        print ("nick--->"+self.nick +"\n email-->"+self.email+"\nFans_list_nicks-->".join([nick for nick in self.fans]))
    def addFan(self,p):
        if p not in self.__blocked: #if p.nick not in self.__blocked:
            self.fans[p.nick]=p
        #else:
        #print("Not allowed")
    def listFans(self):#sin return
        #return self.nick .join([nick for nick in self.fans])
        for p in self.p:
            self.p[p].show()
    def blockUser(self, user):
        if user in self.fans:
            del self.fans[user]#user.nick
        self.__blocked.append(user)#user.nick
    def listBlocked(self):#rep extraño
        if len(self.__blocked)==0:
            print("NO fount Blocked")
        else:
            for i in self.__blocked:
                print(i)
    

if __name__=='__main__':
    g=User("pere","pere@daw.com")
    h=User("anna","anna@daw.com")
    l=User("maria","maria@daw.com")
    k=User("dimoni","dimoni@daw.com")
    g.addFan(h)
    g.addFan(l)
    g.show() #1
    g.listFans() #2
    g.blockUser(k)
    g.addFan(k) #3
    g.show() #4
    g.listBlocked() #5