import json

voc = {"laudare":["loben","preisen","anpriesen","gutheißen","rühmen","a"]}

#frage = input("Frage: ")
frage = "lobare"

# open a file
file1 = open("latein_ausnahmen.json", "r")

# read the file
ausnahmen_str = file1.read()
ausnahmen = json.loads(ausnahmen_str)


def übersetzung():
    for i in range(0,len(voc[frage])-1):
        print(voc[frage][i])


def konjugieren(indikativ_konjunktiv : str,aktiv_passiv : str,tempus : str,numerus : str,person : str,Genus : str,vocabel : str):

    item = [indikativ_konjunktiv,"indikativ","konjungtiv"],[aktiv_passiv,"aktiv","passiv"],[tempus,"plusquamperfekt","perfekt","imperfekt","präsens","futur","futur2"],[numerus,"Sing","Pl"],[person,"1.","2.","3."],[Genus,"mänlich","weiblich"]
    for j in range(0,6):
            if item[j][0] == []:
                for i in range(1,len(item[j])):
                    item[j][0].append(item[j][i])
    output = {}
        
    for i in indikativ_konjunktiv:
        output[i] = {}
        for a in aktiv_passiv:
            output[i][a] = {}
            for t in tempus:
                output[i][a][t] = {}
                for g in Genus:
                    output[i][a][t][g] = {}
                    for n in numerus:
                        output[i][a][t][g][n] = {}
                        for p in person:
                            output[i][a][t][g][n][p] = zwischenfunktion(i,a,t,n,p,g,vocabel)
    return output

def zwischenfunktion(i : str,a : str,t : str,n : str,p : str,g : str,vocabel : str):
    if vocabel in ausnahmen:
        return irregulaere_verben(i,a,t,n,p,vocabel)
    else:
        funktionsliste = {"a_konjugtion":{'indikativ': {'aktiv': {'plusquamperfekt': a_konj_ind_akt_plus(n,p,g,vocabel), 'perfekt': a_konj_ind_akt_perf(n,p,g,vocabel), 'imperfekt': a_konj_ind_akt_imperf(n,p,g,vocabel), 'präsens': a_konj_ind_akt_prä(n,p,g,vocabel), 'futur': a_konj_ind_akt_fut(n,p,g,vocabel), 'futur2': a_konj_ind_akt_fut2(n,p,g,vocabel)},
                                                        'passiv': {'plusquamperfekt': "", 'perfekt': "", 'imperfekt': "", 'präsens': "", 'futur': "", 'futur2': ""}},
                                         'konjungtiv': {'aktiv': {'plusquamperfekt': "", 'perfekt': "", 'imperfekt': "", 'präsens': "", 'futur': "", 'futur2': ""},
                                                        'passiv': {'plusquamperfekt': "", 'perfekt': "", 'imperfekt': "", 'präsens': "", 'futur': "", 'futur2': ""}}}}
        return funktionsliste['a_konjugtion'][i][a][t]


def irregulaere_verben(i,a,t,n,p,Vocabel : str):

    return ausnahmen[Vocabel][i][a][t][n][p]


def a_konj_ind_akt_plus(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"veram","2.":"veras","3.":"verat"},
                "Pl":{"1.":"veramus","2.":"veratis","3.":"verant"}}
    grundform = vocabel.rstrip("re")
    return grundform + endungen[n][p]

def a_konj_ind_akt_perf(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"vi","2.":"visti","3.":"vit"},
                "Pl":{"1.":"vimus","2.":"vistis","3.":"verunt"}}
    grundform = vocabel.rstrip("re")
    return grundform + endungen[n][p]

def a_konj_ind_akt_imperf(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"bam","2.":"bas","3.":"bat"},
                "Pl":{"1.":"bamus","2.":"batis","3.":"bant"}}
    grundform = vocabel.rstrip("re")
    return grundform + endungen[n][p]


def a_konj_ind_akt_prä(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"o","2.":"as","3.":"at"},
                "Pl":{"1.":"amus","2.":"atis","3.":"ant"}}
    grundform = vocabel.rstrip("are")
    return grundform + endungen[n][p]

def a_konj_ind_akt_fut(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"bo","2.":"bis","3.":"bit"},
                "Pl":{"1.":"bimus","2.":"bitis","3.":"bunt"}}
    grundform = vocabel.rstrip("re")
    return grundform + endungen[n][p]

def a_konj_ind_akt_fut2(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"vero","2.":"veris","3.":"verit"},
                "Pl":{"1.":"verimus","2.":"veritis","3.":"verint"}}
    grundform = vocabel.rstrip("re")
    return grundform + endungen[n][p]





print(konjugieren(["indikativ"],["aktiv"],[],[],[],["mänlich"],frage))



### Tests ###

assert konjugieren([],[],[],[],[],[],"esse") == {'indikativ': {'aktiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': 'fueram', '2.': 'fueras', '3.': 'fuerat'}, 'Pl': {'1.': 'fueramus', '2.': 'fueratis', '3.': 'fuerant'}}, 'weiblich': {'Sing': {'1.': 'fueram', '2.': 'fueras', '3.': 'fuerat'}, 'Pl': {'1.': 'fueramus', '2.': 'fueratis', '3.': 'fuerant'}}}, 'perfekt': {'mänlich': {'Sing': {'1.': 'fui', '2.': 'fuisti', '3.': 'fuit'}, 'Pl': {'1.': 'fuimus', '2.': 'fuistis', '3.': 'fuerant'}}, 'weiblich': {'Sing': {'1.': 'fui', '2.': 'fuisti', '3.': 'fuit'}, 'Pl': {'1.': 'fuimus', '2.': 'fuistis', '3.': 'fuerant'}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': 'eram', '2.': 'eras', '3.': 'erat'}, 'Pl': {'1.': 'eramus', '2.': 'eratis', '3.': 'erant'}}, 'weiblich': {'Sing': {'1.': 'eram', '2.': 'eras', '3.': 'erat'}, 'Pl': {'1.': 'eramus', '2.': 'eratis', '3.': 'erant'}}}, 'präsens': {'mänlich': {'Sing': {'1.': 'sum', '2.': 'es', '3.': 'est'}, 'Pl': {'1.': 'sumus', '2.': 'estis', '3.': 'sunt'}}, 'weiblich': {'Sing': {'1.': 'sum', '2.': 'es', '3.': 'est'}, 'Pl': {'1.': 'sumus', '2.': 'estis', '3.': 'sunt'}}}, 'futur': {'mänlich': {'Sing': {'1.': 'ero', '2.': 'eris', '3.': 'erit'}, 'Pl': {'1.': 'erimus', '2.': 'eritis', '3.': 'erunt'}}, 'weiblich': {'Sing': {'1.': 'ero', '2.': 'eris', '3.': 'erit'}, 'Pl': {'1.': 'erimus', '2.': 'eritis', '3.': 'erunt'}}}, 'futur2': {'mänlich': {'Sing': {'1.': 'fuero', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}, 'weiblich': {'Sing': {'1.': 'fuero', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'perfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'präsens': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '"', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '"', '3.': ''}}}, 'futur2': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}}}, 'konjungtiv': {'aktiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': 'fuissem', '2.': 'fuisses', '3.': 'fuisset'}, 'Pl': {'1.': 'fuissemus', '2.': 'fuissetis', '3.': 'fuissent'}}, 'weiblich': {'Sing': {'1.': 'fuissem', '2.': 'fuisses', '3.': 'fuisset'}, 'Pl': {'1.': 'fuissemus', '2.': 'fuissetis', '3.': 'fuissent'}}}, 'perfekt': {'mänlich': {'Sing': {'1.': 'fuerim', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}, 'weiblich': {'Sing': {'1.': 'fuerim', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': 'essem', '2.': 'esses', '3.': 'esset'}, 'Pl': {'1.': 'essemus', '2.': 'essetis', '3.': 'essent'}}, 'weiblich': {'Sing': {'1.': 'essem', '2.': 'esses', '3.': 'esset'}, 'Pl': {'1.': 'essemus', '2.': 'essetis', '3.': 'essent'}}}, 'präsens': {'mänlich': {'Sing': {'1.': 'sim', '2.': 'sis', '3.': 'sit'}, 'Pl': {'1.': 'simus', '2.': 'sitis', '3.': 'sint'}}, 'weiblich': {'Sing': {'1.': 'sim', '2.': 'sis', '3.': 'sit'}, 'Pl': {'1.': 'simus', '2.': 'sitis', '3.': 'sint'}}}, 'futur': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'perfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'präsens': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}}}}
