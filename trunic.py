from phonemizer import phonemize
from phonemizer.separator import Separator
import matplotlib.pyplot as plt

sep=Separator(phone="|", word=" ",syllable="")

mot = input()

resultat = phonemize(
    mot,
    language="en-gb",
    backend="espeak",
    separator=sep,
    strip=True,
    with_stress=False
)

print(resultat)

d={"k":["c","0000001110010"],
   "a":["v","1110000000000"],
   "t":["c","0000010110100"],
   "ɒ":["v","0110000000000"],
   "n":["c","0000010001010"],
   "ʃ":["c","0000010111110"],
   "ɪ":["v","0001100000000"],
   "i":["v","0001100000000"],
   "p":["c","0000000110100"],
   "b":["c","0000001010010"],
   "ɛ":["v","0011100000000"],
   "d":["c","0000001011010"],
   "ɡ":["c","0000000110110"],
   "ʊ":["v","0011000000000"],
   "ə":["v","1100000000000"],
   "ɐ":["v","0001100000000"],
   "iː":["v","0111100000000"],
   "uː":["v","1111000000000"],
   "ɜː":["v","1011100000000"],
   "ɔː":["v","1110100000000"],
   "ɑː":["v","1101100000000"],
   "f":["c","0000000111100"],
   "h":["c","0000001010110"],
   "iə":["v","0110100000000"],
   "w":["c","0000010100000"],
   "eɪ":["v","0100000000000"],
   "m":["c","0000000001010"],
   "aɪ":["v","1000000000000"],               
   "ʌ":["v","0001000000000"],      
   "aʊ":["v","0000100000000"],           
   "əʊ":["v","1111100000000"],                
   "eə":["v","0010100000000"],              
   "s":["c","0000001111100"],
   "ŋ":["c","0000011111110"],
   "dʒ":["c","0000001011000"],
   "tʃ":["c","0000010010100"],
   "l":["c","0000001010100"],
   "v":["c","0000011010010"],
   "θ":["c","0000011110100"],
   "ð":["c","0000001011110"],
   "z":["c","0000011010110"],
   "ʒ":["c","0000011111010"],
   "ɹ":["c","0000001110100"],
   "j":["c","0000011010100"],
   " ":[" ","0000000000000"]
   }

def tracer(texte,pos):

    coords={0:[0,2,3,2],
            1:[0,-2,3,2],
            2:[-2,-2,2,-2],
            3:[-2,0,-2,-3],
            4:[0,2,-3,-2],
            5:[-2,0,2,1],
            6:[0,0,1,3],
            7:[0,2,1,2],
            8:[0,0,1,-1],
            9:[0,-2,-1,-2],
            10:[0,0,-1,-3],
            11:[0,2,-1,-2]}


    def trait(coords,pos):
        x1,x2,y1,y2=coords[0],coords[1],coords[2],coords[3]
        plt.plot([pos[0]+x1,pos[0]+x2],[pos[1]+y1,pos[1]+y2],color="black",linewidth=3)



    for b in range(len(texte)-1):
        if texte[b]=="1":
            trait(coords[b],pos)
    if texte[12]=="1":
        cercle=plt.Circle((pos[0],pos[1]-4),0.5,fill=False, color="black",linewidth=3)
        plt.gca().add_patch(cercle)
    return


def phonem_to_rune(texte,d):
    i=0
    pos=[0,0]
    debut_mot=pos[0]-2.5
    texte=texte.replace(" ","| |")
    texte=texte.replace("ɔɪ","ɒ")
    texte=texte.replace("ʊə","ʊ|ə")
    texte=texte.replace("əl","ə|l")
    texte=texte.split("|")
    while i <=len(texte):
        j=i+1
        phonem1=texte[i]
        if j<len(texte):
            phonem2=texte[j]
        else:
            phonem2=" "

        a=d[phonem1]
        b=d[phonem2]

        if a[0]==b[0] or phonem1==" " or phonem2==" ":
            tracer(a[1],pos)
            i+=1
            pos[0]+=4
        else:
            c = ""
            for k in range(len(a[1])):
                c += str(int(a[1][k]) + int(b[1][k]))
            if a[0]=="v":
                c=c[:-1]+"1"
            tracer(c,pos)
            i+=2
            pos[0]+=4

        if phonem1==" ":
            plt.plot([debut_mot,pos[0]-4.5],[pos[1],pos[1]],color="black",linewidth=3)
            if pos[0]>=60:
                pos[1]-=8.2
                pos[0]=0
            debut_mot=pos[0]-2.5

        if i >=len(texte):
            plt.plot([debut_mot,pos[0]-0.5],[pos[1],pos[1]],color="black",linewidth=3)
            break

    plt.axis("equal")
    plt.show()


        
phonem_to_rune(resultat,d)