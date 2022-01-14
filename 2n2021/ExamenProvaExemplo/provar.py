import time
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
    def post(self,p):
        dataActual = time.strftime("%c")
        hash=[]
        friend=[]
        text=""
        hash_flag=False
        friend_flag=False
        text_flag=True

        for letra in p:
            if letra == "#":
                hash_flag=True
                text_flag=False
            elif letra == "@":
                friend_flag=True
                text_flag=False

            if text_flag:
                text+=letra
            elif hash_flag:
                hash_flag=False


        post=Post(text,dataActual)

        self.posts.append(post)


        #TO FINISH
    def printPostsDate(self):
        for post in self.posts:
            post.show()
            print()

class Post(object):
    def __init__(self,text,date):
        self.content=text
        self.date=date
        self.hashtags=[]
        self.friends=[]
    def show(self):
        print("Content --> "+self.content)
        print("Date--> "+ self.date)
        if len(self.hashtags)==0:
            print("No hashtags")
        else:
            print(" ".join(self.hashtags))
        if len(self.friends)==0:
            print("No friends")
        else:
            print(" ".join(self.friends))

    def addHashtag(self,h):
        self.hashtags+=[h]
    def addFriend(self,f):
        self.friends+=[f]
        
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
    # g=User("pere","pere@daw.com")
    # l=User("maria","maria@daw.com")
    # g.addFan(l)
    # g.blockUser(l)
    # g.post("Next starting project #newproject #newversion #workingcopy @eva @maria @jordina")
    # g.post("Holidays are comming #finishing_project")
    # g.post("End of exams @jordi @eva @maria")
    # g.post("no way")
    # g.printPostsDate()