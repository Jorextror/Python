"""Es el m`odul que s’encarrega de determinar a quina xifra representa una imatge concreta."""
import img
import os
import imgio
import transf
import discret

def load_patterns(prefix="patro"):
    """Aquesta funci ́o rep com a par`ametre el prefix dels noms dels fitxers que contenen els patrons
    dels d ́ıgits i retorna la llista d’imatges corresponent als patrons dels d ́ıgits ordenats de 0 a 9.
    Per exemple, si l’argument  ́es patro voldr`a dir que els arxius dels patrons que s’hauran de
    llegir s’anomenaran: patro_0.jpeg, patro_1.jpeg, . . . , patro_9.jpeg."""   
    path="2n2021/1matricula/patrons"
    content = os.listdir(path)
    for i in range(len(content)):
        archiu=content[i].split("_")
        archiu[0]=prefix
        print(archiu)
        os.rename(path+"/"+content[i],path+"/"+"_".join(archiu))
    for i in range(len(content)-1):
        print(content[i])
        if content[i].split("_")[1]=="gruixut":
            try:
                if content[i].split("_")[2]>content[i+1].split("_")[2]:
                    content[i],content[i+1]=content[i+1],content[i]
            except:
                pass
    return content
        os.rename(path+"/"+content[i],path+"/"+"_".join(archiu))
     for i in range(len(content)-1):
            if content[i].split("_")[1]=="gruixut":
            try:
                if content[i].split("_")[2]>content[i+1].split("_")[2]:
                    content[i],content[i+1]=content[i+1],content[i]
            except:
                pass
    return content

def match(img,patlst):
    def ordena(elem):
        return elem[1]
    """Donada una llista de patrons patlst i una imatge img retorna un enter que correspon amb el
    dıgit mes semblant d’acord amb els conjunt de patrons usat. La imatge img ha de tenir la
    mateixa alçada que els patrons."""
    PixelIgual=[]
    k=0
    for l in range(len(patlst)):
        pi=0
        patrons=read_bn("2 n/Tasca4.1/patrons/"+patlst[l])
        img=vtrim(img)
        if len(patrons[1])<len(img[1]):
            img=scale(img,len(patrons[1]))
        else:
            patrons=scale(patrons,len(img[1]))
        if len(patrons[1][0])>len(img[1][0]):
            column=len(patrons[1])
            row=len(patrons[1][0])
            RowImg=len(img[1][0])
            longer=patrons[1]
            shorter=img[1]
        else:
            column=len(img[1])
            row=len(img[1][0])
            RowImg=len(patrons[1][0])
            longer=img[1]
            shorter=patrons[1]
        for i in range(row):
            for k in range(i,i+row-RowImg+1):
                for j in range(column):
                    if longer[j][k]==shorter[j][k]:
                        pi+=1
        PixelIgual.append((patlst[l].split("_")[len(patlst[l].split("_"))-1][0],pi))
    PixelIgual.sort(key=ordena,reverse=True)
    print(PixelIgual)
    return PixelIgual[0][0]