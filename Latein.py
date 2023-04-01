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
        
    for i in indikativ_konjunktiv:
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

def konjugieren(indikativ_konjungtiv = str,aktiv_passiv = str,Tempus = str,Numerus = str,Person = str,Gennus = str,Vocabel = str):
    item = [indikativ_konjungtiv,"indikativ","konjungtiv"],[aktiv_passiv,"aktiv","passiv"],[Tempus,"plusquamperfekt","perfekt","imperfekt","präsens","futur","futur2"],[Numerus,"Sing","Pl"],[Person,"1.","2.","3."],[Gennus,"mänlich","weiblich"]
    for j in range(0,6):
            if item[j][0] == []:
                for i in range(1,len(item[j])):
                    item[j][0].append(item[j][i])
    output = dictionary_erstellen(indikativ_konjungtiv,aktiv_passiv,Tempus,Numerus,Person,Gennus)

    grundform = Vocabel.rstrip("re")

    #Tempuszeichen = 

    for i in indikativ_konjungtiv:
        for a in aktiv_passiv:
            for t in Tempus:
                for g in Gennus:
                    for n in Numerus:
                        for p in Person:
                            if Vocabel in ausnahmen:
                                output[i][a][t][g][n][p] = ausnahmen[Vocabel][i][a][t][n][p]
                            else:
                                akuelle_form = [i,a,t,g,n,p]
                                output[i][a][t][g][n][p] = grundform + ""

    return output
    


print(konjugieren([],[],[],[],[],[],frage))



### Tests ###

assert konjugieren([],[],[],[],[],[],frage) == {'indikativ': {'aktiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': 'fueram', '2.': 'fueras', '3.': 'fuerat'}, 'Pl': {'1.': 'fueramus', '2.': 'fueratis', '3.': 'fuerant'}}, 'weiblich': {'Sing': {'1.': 'fueram', '2.': 'fueras', '3.': 'fuerat'}, 'Pl': {'1.': 'fueramus', '2.': 'fueratis', '3.': 'fuerant'}}}, 'perfekt': {'mänlich': {'Sing': {'1.': 'fui', '2.': 'fuisti', '3.': 'fuit'}, 'Pl': {'1.': 'fuimus', '2.': 'fuistis', '3.': 'fuerant'}}, 'weiblich': {'Sing': {'1.': 'fui', '2.': 'fuisti', '3.': 'fuit'}, 'Pl': {'1.': 'fuimus', '2.': 'fuistis', '3.': 'fuerant'}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': 'eram', '2.': 'eras', '3.': 'erat'}, 'Pl': {'1.': 'eramus', '2.': 'eratis', '3.': 'erant'}}, 'weiblich': {'Sing': {'1.': 'eram', '2.': 'eras', '3.': 'erat'}, 'Pl': {'1.': 'eramus', '2.': 'eratis', '3.': 'erant'}}}, 'präsens': {'mänlich': {'Sing': {'1.': 'sum', '2.': 'es', '3.': 'est'}, 'Pl': {'1.': 'sumus', '2.': 'estis', '3.': 'sunt'}}, 'weiblich': {'Sing': {'1.': 'sum', '2.': 'es', '3.': 'est'}, 'Pl': {'1.': 'sumus', '2.': 'estis', '3.': 'sunt'}}}, 'futur': {'mänlich': {'Sing': {'1.': 'ero', '2.': 'eris', '3.': 'erit'}, 'Pl': {'1.': 'erimus', '2.': 'eritis', '3.': 'erunt'}}, 'weiblich': {'Sing': {'1.': 'ero', '2.': 'eris', '3.': 'erit'}, 'Pl': {'1.': 'erimus', '2.': 'eritis', '3.': 'erunt'}}}, 'futur2': {'mänlich': {'Sing': {'1.': 'fuero', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}, 'weiblich': {'Sing': {'1.': 'fuero', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'perfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'präsens': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '"', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '"', '3.': ''}}}, 'futur2': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}}}, 'konjungtiv': {'aktiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': 'fuissem', '2.': 'fuisses', '3.': 'fuisset'}, 'Pl': {'1.': 'fuissemus', '2.': 'fuissetis', '3.': 'fuissent'}}, 'weiblich': {'Sing': {'1.': 'fuissem', '2.': 'fuisses', '3.': 'fuisset'}, 'Pl': {'1.': 'fuissemus', '2.': 'fuissetis', '3.': 'fuissent'}}}, 'perfekt': {'mänlich': {'Sing': {'1.': 'fuerim', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}, 'weiblich': {'Sing': {'1.': 'fuerim', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': 'essem', '2.': 'esses', '3.': 'esset'}, 'Pl': {'1.': 'essemus', '2.': 'essetis', '3.': 'essent'}}, 'weiblich': {'Sing': {'1.': 'essem', '2.': 'esses', '3.': 'esset'}, 'Pl': {'1.': 'essemus', '2.': 'essetis', '3.': 'essent'}}}, 'präsens': {'mänlich': {'Sing': {'1.': 'sim', '2.': 'sis', '3.': 'sit'}, 'Pl': {'1.': 'simus', '2.': 'sitis', '3.': 'sint'}}, 'weiblich': {'Sing': {'1.': 'sim', '2.': 'sis', '3.': 'sit'}, 'Pl': {'1.': 'simus', '2.': 'sitis', '3.': 'sint'}}}, 'futur': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'perfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'präsens': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}}}}
