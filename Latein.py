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
                                                        'passiv': {'plusquamperfekt': "", 'perfekt': a_konj_ind_pas_perf(n,p,g,vocabel), 'imperfekt': a_konj_ind_pas_imperf(n,p,g,vocabel), 'präsens': a_konj_ind_pas_prä(n,p,g,vocabel), 'futur': a_konj_ind_pas_fut(n,p,g,vocabel), 'futur2': ""}},
                                         'konjungtiv': {'aktiv': {'plusquamperfekt': "", 'perfekt': "", 'imperfekt': "", 'präsens': "", 'futur': "", 'futur2': ""},
                                                        'passiv': {'plusquamperfekt': "", 'perfekt': "", 'imperfekt': "", 'präsens': "", 'futur': "", 'futur2': ""}}}}
        return funktionsliste['a_konjugtion'][i][a][t]


def irregulaere_verben(i,a,t,n,p,Vocabel : str):

    return ausnahmen[Vocabel][i][a][t][n][p]

### a-konjugation indikativ aktiv ###

def a_konj_ind_akt_prä(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"o","2.":"as","3.":"at"},
                "Pl":{"1.":"amus","2.":"atis","3.":"ant"}}
    tempuszeichen = ""
    grundform = vocabel.rstrip("are")
    return grundform + tempuszeichen + endungen[n][p]

def a_konj_ind_akt_imperf(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"m","2.":"s","3.":"t"},
                "Pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "ba"
    grundform = vocabel.rstrip("re")
    return grundform + tempuszeichen + endungen[n][p]

def a_konj_ind_akt_perf(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"i","2.":"isti","3.":"it"},
                "Pl":{"1.":"imus","2.":"istis","3.":"erunt"}}
    tempuszeichen = "v"
    grundform = vocabel.rstrip("re")
    return grundform + tempuszeichen + endungen[n][p]

def a_konj_ind_akt_plus(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"m","2.":"s","3.":"t"},
                "Pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "vera"
    grundform = vocabel.rstrip("re")
    return grundform + tempuszeichen + endungen[n][p]

def a_konj_ind_akt_fut(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"o","2.":"is","3.":"it"},
                "Pl":{"1.":"imus","2.":"itis","3.":"unt"}}
    tempuszeichen = "b"
    grundform = vocabel.rstrip("re")
    return grundform  + tempuszeichen + endungen[n][p]

def a_konj_ind_akt_fut2(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"o","2.":"is","3.":"it"},
                "Pl":{"1.":"imus","2.":"itis","3.":"int"}}
    tempuszeichen = "ver"
    grundform = vocabel.rstrip("re")
    return grundform  + tempuszeichen + endungen[n][p]

### a-konjugation indikativ passiv ###

def a_konj_ind_pas_prä(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"or","2.":"aris","3.":"atur"},
                "Pl":{"1.":"amur","2.":"amini","3.":"antur"}}
    tempuszeichen = ""
    grundform = vocabel.rstrip("are")
    return grundform  + tempuszeichen + endungen[n][p]


def a_konj_ind_pas_imperf(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"r","2.":"ris","3.":"tur"},
                "Pl":{"1.":"mur","2.":"mini","3.":"ntur"}}
    tempuszeichen = "ba"
    grundform = vocabel.rstrip("re")
    return grundform  + tempuszeichen + endungen[n][p]

def a_konj_ind_pas_fut(n : str,p : str,g : str,vocabel : str):
    endungen = {"Sing":{"1.":"or","2.":"eris","3.":"itur"},
                "Pl":{"1.":"imur","2.":"imini","3.":"untur"}}
    tempuszeichen = "b"
    grundform = vocabel.rstrip("re")
    return grundform  + tempuszeichen + endungen[n][p]


def a_konj_ind_pas_perf(n : str,p : str,g : str,vocabel : str):
    sonderzeichen = {"mänlich":{"Sing":"tus ","Pl":"ti "},"weiblich":{"Sing":"ta ","Pl":"tae "}}
    grundform = vocabel.rstrip("re")
    return grundform  + sonderzeichen[g][n] + konjugieren(["indikativ"],["aktiv"],["präsens"],[n],[p],["mänlich"],"esse")




print(konjugieren(["indikativ"],["passiv"],["perfekt"],[],[],["mänlich"],frage))



### Tests ###

assert konjugieren([],[],[],[],[],[],"esse") == {'indikativ': {'aktiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': 'fueram', '2.': 'fueras', '3.': 'fuerat'}, 'Pl': {'1.': 'fueramus', '2.': 'fueratis', '3.': 'fuerant'}}, 'weiblich': {'Sing': {'1.': 'fueram', '2.': 'fueras', '3.': 'fuerat'}, 'Pl': {'1.': 'fueramus', '2.': 'fueratis', '3.': 'fuerant'}}}, 'perfekt': {'mänlich': {'Sing': {'1.': 'fui', '2.': 'fuisti', '3.': 'fuit'}, 'Pl': {'1.': 'fuimus', '2.': 'fuistis', '3.': 'fuerant'}}, 'weiblich': {'Sing': {'1.': 'fui', '2.': 'fuisti', '3.': 'fuit'}, 'Pl': {'1.': 'fuimus', '2.': 'fuistis', '3.': 'fuerant'}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': 'eram', '2.': 'eras', '3.': 'erat'}, 'Pl': {'1.': 'eramus', '2.': 'eratis', '3.': 'erant'}}, 'weiblich': {'Sing': {'1.': 'eram', '2.': 'eras', '3.': 'erat'}, 'Pl': {'1.': 'eramus', '2.': 'eratis', '3.': 'erant'}}}, 'präsens': {'mänlich': {'Sing': {'1.': 'sum', '2.': 'es', '3.': 'est'}, 'Pl': {'1.': 'sumus', '2.': 'estis', '3.': 'sunt'}}, 'weiblich': {'Sing': {'1.': 'sum', '2.': 'es', '3.': 'est'}, 'Pl': {'1.': 'sumus', '2.': 'estis', '3.': 'sunt'}}}, 'futur': {'mänlich': {'Sing': {'1.': 'ero', '2.': 'eris', '3.': 'erit'}, 'Pl': {'1.': 'erimus', '2.': 'eritis', '3.': 'erunt'}}, 'weiblich': {'Sing': {'1.': 'ero', '2.': 'eris', '3.': 'erit'}, 'Pl': {'1.': 'erimus', '2.': 'eritis', '3.': 'erunt'}}}, 'futur2': {'mänlich': {'Sing': {'1.': 'fuero', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}, 'weiblich': {'Sing': {'1.': 'fuero', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'perfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'präsens': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '"', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '"', '3.': ''}}}, 'futur2': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}}}, 'konjungtiv': {'aktiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': 'fuissem', '2.': 'fuisses', '3.': 'fuisset'}, 'Pl': {'1.': 'fuissemus', '2.': 'fuissetis', '3.': 'fuissent'}}, 'weiblich': {'Sing': {'1.': 'fuissem', '2.': 'fuisses', '3.': 'fuisset'}, 'Pl': {'1.': 'fuissemus', '2.': 'fuissetis', '3.': 'fuissent'}}}, 'perfekt': {'mänlich': {'Sing': {'1.': 'fuerim', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}, 'weiblich': {'Sing': {'1.': 'fuerim', '2.': 'fueris', '3.': 'fuerit'}, 'Pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': 'essem', '2.': 'esses', '3.': 'esset'}, 'Pl': {'1.': 'essemus', '2.': 'essetis', '3.': 'essent'}}, 'weiblich': {'Sing': {'1.': 'essem', '2.': 'esses', '3.': 'esset'}, 'Pl': {'1.': 'essemus', '2.': 'essetis', '3.': 'essent'}}}, 'präsens': {'mänlich': {'Sing': {'1.': 'sim', '2.': 'sis', '3.': 'sit'}, 'Pl': {'1.': 'simus', '2.': 'sitis', '3.': 'sint'}}, 'weiblich': {'Sing': {'1.': 'sim', '2.': 'sis', '3.': 'sit'}, 'Pl': {'1.': 'simus', '2.': 'sitis', '3.': 'sint'}}}, 'futur': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'perfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'präsens': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'Sing': {'1.': '', '2.': '', '3.': ''}, 'Pl': {'1.': '', '2.': '', '3.': ''}}}}}}
assert konjugieren(["indikativ"],["aktiv"],[],[],[],["mänlich"],"lobare") == {'indikativ': {'aktiv': {'plusquamperfekt': {'mänlich': {'Sing': {'1.': 'lobaveram', '2.': 'lobaveras', '3.': 'lobaverat'}, 'Pl': {'1.': 'lobaveramus', '2.': 'lobaveratis', '3.': 'lobaverant'}}}, 'perfekt': {'mänlich': {'Sing': {'1.': 'lobavi', '2.': 'lobavisti', '3.': 'lobavit'}, 'Pl': {'1.': 'lobavimus', '2.': 'lobavistis', '3.': 'lobaverunt'}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': 'lobabam', '2.': 'lobabas', '3.': 'lobabat'}, 'Pl': {'1.': 'lobabamus', '2.': 'lobabatis', '3.': 'lobabant'}}}, 'präsens': {'mänlich': {'Sing': {'1.': 'lobo', '2.': 'lobas', '3.': 'lobat'}, 'Pl': {'1.': 'lobamus', '2.': 'lobatis', '3.': 'lobant'}}}, 'futur': {'mänlich': {'Sing': {'1.': 'lobabo', '2.': 'lobabis', '3.': 'lobabit'}, 'Pl': {'1.': 'lobabimus', '2.': 'lobabitis', '3.': 'lobabunt'}}}, 'futur2': {'mänlich': {'Sing': {'1.': 'lobavero', '2.': 'lobaveris', '3.': 'lobaverit'}, 'Pl': {'1.': 'lobaverimus', '2.': 'lobaveritis', '3.': 'lobaverint'}}}}}}
assert konjugieren(["indikativ"],["passiv"],["präsens","imperfekt","futur"],[],[],["mänlich"],"lobare") == {'indikativ': {'passiv': {'präsens': {'mänlich': {'Sing': {'1.': 'lobor', '2.': 'lobaris', '3.': 'lobatur'}, 'Pl': {'1.': 'lobamur', '2.': 'lobamini', '3.': 'lobantur'}}}, 'imperfekt': {'mänlich': {'Sing': {'1.': 'lobabar', '2.': 'lobabaris', '3.': 'lobabatur'}, 'Pl': {'1.': 'lobabamur', '2.': 'lobabamini', '3.': 'lobabantur'}}}, 'futur': {'mänlich': {'Sing': {'1.': 'lobabor', '2.': 'lobaberis', '3.': 'lobabitur'}, 'Pl': {'1.': 'lobabimur', '2.': 'lobabimini', '3.': 'lobabuntur'}}}}}}