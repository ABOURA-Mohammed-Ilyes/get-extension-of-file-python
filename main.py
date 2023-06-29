fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definitions_extension = (
    ("doc","Document Word"),
    ("exe","Executable"),
    ("txt","Document texte"),
    ("jpeg","Image JPEG")
)

def check_in(extension) :
    for e in definitions_extension :
        if e[0].lower() == extension.lower() :
            return e[1]
    return "Extension non connus"

def check( fichiers ):
    for fichier in fichiers :
        splited = fichier.split(".")
        if len(splited) > 1 :
            print(f"{fichier} ({check_in(splited[-1])})")
        else :
            print(f"{fichier} (Aucune extension)")

check(fichiers) 

'''lentgh = [len(x) for x in fichiers]
print (sum(lentgh))'''