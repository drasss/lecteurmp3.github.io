import os.path,os,time,urllib.parse
#recuperation des noms de musiques dans un fichier txt (a cause de l'enodage UTF-8 on peut pas faire une seule commande)
#expliquant les "encoding="utf-8""
os.system("start recupmp3.bat")
time.sleep(0.5)
#lecture des noms du fichier txt dans une variable
lect=open("recup.txt","r",encoding="utf-8")
noms=lect.read()+"₾"
lect.close()
#séparation des noms dans un tuple
tab=("",)
i=0
st=""
#tant que le fichier n'est pas fini(
#     tant que le fichier n'est pas fini et qu'il n'y a pas de retour a la ligne(
#           lire la lettre et l'ajouter dans le str qui conserve la phrase)
#     prendre la phrase et la rajouter dans le tableau (puis repartir de 0))
while noms[i]!="₾":
      while (noms[i]!="." or noms[i+1]!="m" or noms[i+2]!="p" or noms[i+3]!="3") and noms[i]!="₾":
            st+=noms[i]
            i+=1
      tab+=(st,)
      st=""
      i+=5

#exriture du fichier html
fichier=open("lecteur.html","w",encoding="utf-8")
fichier.write("<html><style type=\"text/css\" media=\"all\">@import \"css.css\";</style>\n")
#head
fichier.write("<head>")
fichier.write("<title>Lecteur Mp3</title>") #titre
fichier.write("<link rel=\"icon\" href=\"img\icone.png\" />") #icone
fichier.write("<meta charset=\"UTF-8\">")#utf-8 pour mozilla
fichier.write("")#
#mise en place des sons
fichier.write("\n</head><body>\n")
#pour ne pas utiliser de variable j utiliser "i+1" 
for i in range(len(tab)-1):
      fichier.write("<p>"+tab[i+1]+"</p>\n")
      fichier.write("<audio controls=\"\" preload=\"none\" loop=\"true\"><source src=\"..\mp3\\"+urllib.parse.quote(tab[i+1])+".mp3\" type=\"audio/mpeg\"></audio>") #urllib.parse.quote() sert a transformer le char en url
fichier.write("</body>\n</html>\n")
fichier.close()
#os.system("start lecteur.html")
