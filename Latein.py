import json

voc = {"laudare":["loben","preisen","anpriesen","gutheißen","rühmen","a"]}


#frage = input("Frage: ")
frage = "esse"

# open a file
file1 = open("latein_ausnahmen.json", "r")

# read the file
ausnahmen_str = file1.read()
ausnahmen = json.loads(ausnahmen_str)

def dictionary_erstellen(indikativ_konjungtiv,aktiv_passiv,tempus,SingPl,person,Gennus):
    output = {}
        
    for i in indikativ_konjungtiv:
        output[i] = {}
        for a in aktiv_passiv:
            output[i][a] = {}
            for t in tempus:
                output[i][a][t] = {}
                for g in Gennus:
                    output[i][a][t][g] = {}
                    for s in SingPl:
                        output[i][a][t][g][s] = {}
                        for p in person:
                            output[i][a][t][g][s][p] = ""
    return output
def übersetzung():
    for i in range(0,len(voc[frage])-1):
        print(voc[frage][i])

def konjugieren(indikativ_konjungtiv,aktiv_passiv,Tempus,Numerus,Person,Genus = "", Vocabel : str = ""):
    item = [indikativ_konjungtiv,"indikativ","konjungtiv"],[aktiv_passiv,"aktiv","passiv"],[Tempus,"plusquamperfekt","perfekt","imperfekt","präsens","futur","futur2"],[Numerus,"Sing","Pl"],[Person,"1.","2.","3."],[Genus,"Mänlich","weiblich"]
    for j in range(0,6):
            if item[j][0] == []:
                for i in range(1,len(item[j])):
                    item[j][0].append(item[j][i])
    output = dictionary_erstellen(indikativ_konjungtiv,aktiv_passiv,Tempus,Numerus,Person,Genus)
    return output
    

print(konjugieren(["indikativ"],["Aktiv"],["Präsens"],[],[],[],frage))
