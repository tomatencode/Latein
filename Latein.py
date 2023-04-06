import json

voc = {"laudare":["loben","preisen","anpriesen","gutheißen","rühmen","a"]}

# frage = input("Frage: ")
frage = "laudare"

# open a file
file1 = open("latein_ausnahmen.json", "r")

# read the file
ausnahmen_str = file1.read()
ausnahmen = json.loads(ausnahmen_str)


def übersetzung():
    for i in range(0,len(voc[frage])-1):
        print(voc[frage][i])


def konjugieren(indikativ_konjunktiv : str,aktiv_passiv : str,tempus : str,numerus : str,person : str,Genus : str,vocabel : str):

    item = [indikativ_konjunktiv,"indikativ","konjungtiv"],[aktiv_passiv,"aktiv","passiv"],
    [tempus,"plusquamperfekt","perfekt","imperfekt","präsens","futur","futur2"],[numerus,"sing","pl"],[person,"1.","2.","3."],[Genus,"mänlich","weiblich"]

    for j in range(0,item.__len__()):
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
        funktionsliste_dict = {"a_konjugtion":{'indikativ': {'aktiv': {'plusquamperfekt': a_konj_ind_akt_plus(n,p,g,vocabel), 'perfekt': a_konj_ind_akt_perf(n,p,g,vocabel),'imperfekt': a_konj_ind_akt_imperf(n,p,g,vocabel), 'präsens': a_konj_ind_akt_prä(n,p,g,vocabel), 'futur': a_konj_ind_akt_fut(n,p,g,vocabel), 'futur2': a_konj_ind_akt_fut2(n,p,g,vocabel)},
                                                        'passiv': {'plusquamperfekt': a_konj_ind_pas_plus(n,p,g,vocabel), 'perfekt': a_konj_ind_pas_perf(n,p,g,vocabel), 'imperfekt': a_konj_ind_pas_imperf(n,p,g,vocabel), 'präsens': a_konj_ind_pas_prä(n,p,g,vocabel), 'futur': a_konj_ind_pas_fut(n,p,g,vocabel), 'futur2': a_konj_ind_pas_fut2(n,p,g,vocabel)}},
                                         'konjungtiv': {'aktiv': {'plusquamperfekt': a_konj_konj_akt_plus(n,p,g,vocabel), 'perfekt': a_konj_konj_akt_perf(n,p,g,vocabel), 'imperfekt': a_konj_konj_akt_imperf(n,p,g,vocabel), 'präsens': a_konj_konj_akt_prä(n,p,g,vocabel), 'futur': "", 'futur2': ""},
                                                        'passiv': {'plusquamperfekt': a_konj_konj_pas_plus(n,p,g,vocabel), 'perfekt': a_konj_konj_pas_perf(n,p,g,vocabel), 'imperfekt': a_konj_konj_pas_imperf(n,p,g,vocabel), 'präsens': a_konj_konj_pas_prä(n,p,g,vocabel), 'futur': "", 'futur2': ""}}}}
        return funktionsliste_dict['a_konjugtion'][i][a][t]


def irregulaere_verben(i,a,t,n,p,Vocabel : str):

    return ausnahmen[Vocabel][i][a][t][n][p]

# a-konjugation indikativ aktiv
def a_konj_ind_akt_prä(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"o","2.":"as","3.":"at"},
                "pl":{"1.":"amus","2.":"atis","3.":"ant"}}
    tempuszeichen = ""
    grundform = vocabel.rstrip("are")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_konj_ind_akt_imperf(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "ba"
    grundform = vocabel.rstrip("re")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_konj_ind_akt_perf(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"i","2.":"isti","3.":"it"},
                "pl":{"1.":"imus","2.":"istis","3.":"erunt"}}
    tempuszeichen = "v"
    grundform = vocabel.rstrip("re")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_konj_ind_akt_plus(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "vera"
    grundform = vocabel.rstrip("re")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_konj_ind_akt_fut(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"o","2.":"is","3.":"it"},
                "pl":{"1.":"imus","2.":"itis","3.":"unt"}}
    tempuszeichen = "b"
    grundform = vocabel.rstrip("re")
    return grundform  + tempuszeichen + endungen_dict[n][p]

def a_konj_ind_akt_fut2(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"o","2.":"is","3.":"it"},
                "pl":{"1.":"imus","2.":"itis","3.":"int"}}
    tempuszeichen = "ver"
    grundform = vocabel.rstrip("re")
    return grundform  + tempuszeichen + endungen_dict[n][p]

# a-konjugation indikativ passiv
def a_konj_ind_pas_prä(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"or","2.":"aris","3.":"atur"},
                "pl":{"1.":"amur","2.":"amini","3.":"antur"}}
    tempuszeichen = ""
    grundform = vocabel.rstrip("are")
    return grundform  + tempuszeichen + endungen_dict[n][p]


def a_konj_ind_pas_imperf(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"r","2.":"ris","3.":"tur"},
                "pl":{"1.":"mur","2.":"mini","3.":"ntur"}}
    tempuszeichen = "ba"
    grundform = vocabel.rstrip("re")
    return grundform  + tempuszeichen + endungen_dict[n][p]

def a_konj_ind_pas_fut(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"or","2.":"eris","3.":"itur"},
                "pl":{"1.":"imur","2.":"imini","3.":"untur"}}
    tempuszeichen = "b"
    grundform = vocabel.rstrip("re")
    return grundform  + tempuszeichen + endungen_dict[n][p]


def a_konj_ind_pas_perf(n : str,p : str,g : str,vocabel : str):
    sonderzeichen_dict = {"mänlich":{"sing":"tus ","pl":"ti "},
                          "weiblich":{"sing":"ta ","pl":"tae "}}
    grundform = vocabel.rstrip("re")
    esse_form_str = konjugieren(["indikativ"],["aktiv"],["präsens"],[n],[p],["mänlich"],"esse") ["indikativ"]["aktiv"]["präsens"]["mänlich"][n][p]
    return grundform  + sonderzeichen_dict[g][n] + esse_form_str

def a_konj_ind_pas_plus(n : str,p : str,g : str,vocabel : str):
    sonderzeichen_dict = {"mänlich":{"sing":"tus ","pl":"ti "},
                          "weiblich":{"sing":"ta ","pl":"tae "}}
    grundform = vocabel.rstrip("re")
    esse_form_str = konjugieren(["indikativ"],["aktiv"],["imperfekt"],[n],[p],["mänlich"],"esse") ["indikativ"]["aktiv"]["imperfekt"]["mänlich"][n][p]
    return grundform  + sonderzeichen_dict[g][n] + esse_form_str

def a_konj_ind_pas_fut2(n : str,p : str,g : str,vocabel : str):
    sonderzeichen_dict = {"mänlich":{"sing":"tus ","pl":"ti "},
                          "weiblich":{"sing":"ta ","pl":"tae "}}
    grundform = vocabel.rstrip("re")
    esse_form_str = konjugieren(["indikativ"],["aktiv"],["futur"],[n],[p],["mänlich"],"esse") ["indikativ"]["aktiv"]["futur"]["mänlich"][n][p]
    return grundform  + sonderzeichen_dict[g][n] + esse_form_str

# a-konjugation konjungtiv aktiv
def a_konj_konj_akt_prä(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "e"
    grundform = vocabel.rstrip("are")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_konj_konj_akt_imperf(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = ""
    grundform = vocabel.rstrip("")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_konj_konj_akt_perf(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "veri"
    grundform = vocabel.rstrip("re")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_konj_konj_akt_plus(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "visse"
    grundform = vocabel.rstrip("re")
    return grundform + tempuszeichen + endungen_dict[n][p]

# a-konjugation konjungtiv passiv
def a_konj_konj_pas_prä(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"r","2.":"ris","3.":"tur"},
                "pl":{"1.":"mur","2.":"mini","3.":"ntur"}}
    tempuszeichen = "e"
    grundform = vocabel.rstrip("are")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_konj_konj_pas_imperf(n : str,p : str,g : str,vocabel : str):
    endungen_dict = {"sing":{"1.":"r","2.":"ris","3.":"tur"},
                "pl":{"1.":"mur","2.":"mini","3.":"ntur"}}
    tempuszeichen = ""
    grundform = vocabel.rstrip("")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_konj_konj_pas_perf(n : str,p : str,g : str,vocabel : str):
    sonderzeichen_dict = {"mänlich":{"sing":"tus ","pl":"ti "},"weiblich":{"sing":"ta ","pl":"tae "}}
    grundform = vocabel.rstrip("re")
    esse_form_str = konjugieren(["konjungtiv"],["aktiv"],["präsens"],[n],[p],["mänlich"],"esse") ["konjungtiv"]["aktiv"]["präsens"]["mänlich"][n][p]
    return grundform  + sonderzeichen_dict[g][n] + esse_form_str

def a_konj_konj_pas_plus(n : str,p : str,g : str,vocabel : str):
    sonderzeichen_dict = {"mänlich":{"sing":"tus ","pl":"ti "},"weiblich":{"sing":"ta ","pl":"tae "}}
    grundform = vocabel.rstrip("re")
    esse_form_str = konjugieren(["konjungtiv"],["aktiv"],["imperfekt"],[n],[p],["mänlich"],"esse") ["konjungtiv"]["aktiv"]["imperfekt"]["mänlich"][n][p]
    return grundform  + sonderzeichen_dict[g][n] + esse_form_str

print(konjugieren([],[],[],[],[],[],frage))


# Tests 
assert konjugieren([],[],[],[],[],[],"esse") == {'indikativ': {'aktiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'fueram', '2.': 'fueras', '3.': 'fuerat'}, 'pl': {'1.': 'fueramus', '2.': 'fueratis', '3.': 'fuerant'}}, 'weiblich': {'sing': {'1.': 'fueram', '2.': 'fueras', '3.': 'fuerat'}, 'pl': {'1.': 'fueramus', '2.': 'fueratis', '3.': 'fuerant'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'fui', '2.': 'fuisti', '3.': 'fuit'}, 'pl': {'1.': 'fuimus', '2.': 'fuistis', '3.': 'fuerant'}}, 'weiblich': {'sing': {'1.': 'fui', '2.': 'fuisti', '3.': 'fuit'}, 'pl': {'1.': 'fuimus', '2.': 'fuistis', '3.': 'fuerant'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'eram', '2.': 'eras', '3.': 'erat'}, 'pl': {'1.': 'eramus', '2.': 'eratis', '3.': 'erant'}}, 'weiblich': {'sing': {'1.': 'eram', '2.': 'eras', '3.': 'erat'}, 'pl': {'1.': 'eramus', '2.': 'eratis', '3.': 'erant'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'sum', '2.': 'es', '3.': 'est'}, 'pl': {'1.': 'sumus', '2.': 'estis', '3.': 'sunt'}}, 'weiblich': {'sing': {'1.': 'sum', '2.': 'es', '3.': 'est'}, 'pl': {'1.': 'sumus', '2.': 'estis', '3.': 'sunt'}}}, 'futur': {'mänlich': {'sing': {'1.': 'ero', '2.': 'eris', '3.': 'erit'}, 'pl': {'1.': 'erimus', '2.': 'eritis', '3.': 'erunt'}}, 'weiblich': {'sing': {'1.': 'ero', '2.': 'eris', '3.': 'erit'}, 'pl': {'1.': 'erimus', '2.': 'eritis', '3.': 'erunt'}}}, 'futur2': {'mänlich': {'sing': {'1.': 'fuero', '2.': 'fueris', '3.': 'fuerit'}, 'pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}, 'weiblich': {'sing': {'1.': 'fuero', '2.': 'fueris', '3.': 'fuerit'}, 'pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'perfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'imperfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'präsens': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '"', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '"', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}}, 'konjungtiv': {'aktiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'fuissem', '2.': 'fuisses', '3.': 'fuisset'}, 'pl': {'1.': 'fuissemus', '2.': 'fuissetis', '3.': 'fuissent'}}, 'weiblich': {'sing': {'1.': 'fuissem', '2.': 'fuisses', '3.': 'fuisset'}, 'pl': {'1.': 'fuissemus', '2.': 'fuissetis', '3.': 'fuissent'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'fuerim', '2.': 'fueris', '3.': 'fuerit'}, 'pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}, 'weiblich': {'sing': {'1.': 'fuerim', '2.': 'fueris', '3.': 'fuerit'}, 'pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'essem', '2.': 'esses', '3.': 'esset'}, 'pl': {'1.': 'essemus', '2.': 'essetis', '3.': 'essent'}}, 'weiblich': {'sing': {'1.': 'essem', '2.': 'esses', '3.': 'esset'}, 'pl': {'1.': 'essemus', '2.': 'essetis', '3.': 'essent'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'sim', '2.': 'sis', '3.': 'sit'}, 'pl': {'1.': 'simus', '2.': 'sitis', '3.': 'sint'}}, 'weiblich': {'sing': {'1.': 'sim', '2.': 'sis', '3.': 'sit'}, 'pl': {'1.': 'simus', '2.': 'sitis', '3.': 'sint'}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'perfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'imperfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'präsens': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}}}
assert konjugieren([],[],[],[],[],[],"lobare") == {'indikativ': {'aktiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'lobaveram', '2.': 'lobaveras', '3.': 'lobaverat'}, 'pl': {'1.': 'lobaveramus', '2.': 'lobaveratis', '3.': 'lobaverant'}}, 'weiblich': {'sing': {'1.': 'lobaveram', '2.': 'lobaveras', '3.': 'lobaverat'}, 'pl': {'1.': 'lobaveramus', '2.': 'lobaveratis', '3.': 'lobaverant'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'lobavi', '2.': 'lobavisti', '3.': 'lobavit'}, 'pl': {'1.': 'lobavimus', '2.': 'lobavistis', '3.': 'lobaverunt'}}, 'weiblich': {'sing': {'1.': 'lobavi', '2.': 'lobavisti', '3.': 'lobavit'}, 'pl': {'1.': 'lobavimus', '2.': 'lobavistis', '3.': 'lobaverunt'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'lobabam', '2.': 'lobabas', '3.': 'lobabat'}, 'pl': {'1.': 'lobabamus', '2.': 'lobabatis', '3.': 'lobabant'}}, 'weiblich': {'sing': {'1.': 'lobabam', '2.': 'lobabas', '3.': 'lobabat'}, 'pl': {'1.': 'lobabamus', '2.': 'lobabatis', '3.': 'lobabant'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'lobo', '2.': 'lobas', '3.': 'lobat'}, 'pl': {'1.': 'lobamus', '2.': 'lobatis', '3.': 'lobant'}}, 'weiblich': {'sing': {'1.': 'lobo', '2.': 'lobas', '3.': 'lobat'}, 'pl': {'1.': 'lobamus', '2.': 'lobatis', '3.': 'lobant'}}}, 'futur': {'mänlich': {'sing': {'1.': 'lobabo', '2.': 'lobabis', '3.': 'lobabit'}, 'pl': {'1.': 'lobabimus', '2.': 'lobabitis', '3.': 'lobabunt'}}, 'weiblich': {'sing': {'1.': 'lobabo', '2.': 'lobabis', '3.': 'lobabit'}, 'pl': {'1.': 'lobabimus', '2.': 'lobabitis', '3.': 'lobabunt'}}}, 'futur2': {'mänlich': {'sing': {'1.': 'lobavero', '2.': 'lobaveris', '3.': 'lobaverit'}, 'pl': {'1.': 'lobaverimus', '2.': 'lobaveritis', '3.': 'lobaverint'}}, 'weiblich': {'sing': {'1.': 'lobavero', '2.': 'lobaveris', '3.': 'lobaverit'}, 'pl': {'1.': 'lobaverimus', '2.': 'lobaveritis', '3.': 'lobaverint'}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'lobatus eram', '2.': 'lobatus eras', '3.': 'lobatus erat'}, 'pl': {'1.': 'lobati eramus', '2.': 'lobati eratis', '3.': 'lobati erant'}}, 'weiblich': {'sing': {'1.': 'lobata eram', '2.': 'lobata eras', '3.': 'lobata erat'}, 'pl': {'1.': 'lobatae eramus', '2.': 'lobatae eratis', '3.': 'lobatae erant'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'lobatus sum', '2.': 'lobatus es', '3.': 'lobatus est'}, 'pl': {'1.': 'lobati sumus', '2.': 'lobati estis', '3.': 'lobati sunt'}}, 'weiblich': {'sing': {'1.': 'lobata sum', '2.': 'lobata es', '3.': 'lobata est'}, 'pl': {'1.': 'lobatae sumus', '2.': 'lobatae estis', '3.': 'lobatae sunt'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'lobabar', '2.': 'lobabaris', '3.': 'lobabatur'}, 'pl': {'1.': 'lobabamur', '2.': 'lobabamini', '3.': 'lobabantur'}}, 'weiblich': {'sing': {'1.': 'lobabar', '2.': 'lobabaris', '3.': 'lobabatur'}, 'pl': {'1.': 'lobabamur', '2.': 'lobabamini', '3.': 'lobabantur'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'lobor', '2.': 'lobaris', '3.': 'lobatur'}, 'pl': {'1.': 'lobamur', '2.': 'lobamini', '3.': 'lobantur'}}, 'weiblich': {'sing': {'1.': 'lobor', '2.': 'lobaris', '3.': 'lobatur'}, 'pl': {'1.': 'lobamur', '2.': 'lobamini', '3.': 'lobantur'}}}, 'futur': {'mänlich': {'sing': {'1.': 'lobabor', '2.': 'lobaberis', '3.': 'lobabitur'}, 'pl': {'1.': 'lobabimur', '2.': 'lobabimini', '3.': 'lobabuntur'}}, 'weiblich': {'sing': {'1.': 'lobabor', '2.': 'lobaberis', '3.': 'lobabitur'}, 'pl': {'1.': 'lobabimur', '2.': 'lobabimini', '3.': 'lobabuntur'}}}, 'futur2': {'mänlich': {'sing': {'1.': 'lobatus ero', '2.': 'lobatus eris', '3.': 'lobatus erit'}, 'pl': {'1.': 'lobati erimus', '2.': 'lobati eritis', '3.': 'lobati erunt'}}, 'weiblich': {'sing': {'1.': 'lobata ero', '2.': 'lobata eris', '3.': 'lobata erit'}, 'pl': {'1.': 'lobatae erimus', '2.': 'lobatae eritis', '3.': 'lobatae erunt'}}}}}, 'konjungtiv': {'aktiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'lobavissem', '2.': 'lobavisses', '3.': 'lobavisset'}, 'pl': {'1.': 'lobavissemus', '2.': 'lobavissetis', '3.': 'lobavissent'}}, 'weiblich': {'sing': {'1.': 'lobavissem', '2.': 'lobavisses', '3.': 'lobavisset'}, 'pl': {'1.': 'lobavissemus', '2.': 'lobavissetis', '3.': 'lobavissent'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'lobaverim', '2.': 'lobaveris', '3.': 'lobaverit'}, 'pl': {'1.': 'lobaverimus', '2.': 'lobaveritis', '3.': 'lobaverint'}}, 'weiblich': {'sing': {'1.': 'lobaverim', '2.': 'lobaveris', '3.': 'lobaverit'}, 'pl': {'1.': 'lobaverimus', '2.': 'lobaveritis', '3.': 'lobaverint'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'lobarem', '2.': 'lobares', '3.': 'lobaret'}, 'pl': {'1.': 'lobaremus', '2.': 'lobaretis', '3.': 'lobarent'}}, 'weiblich': {'sing': {'1.': 'lobarem', '2.': 'lobares', '3.': 'lobaret'}, 'pl': {'1.': 'lobaremus', '2.': 'lobaretis', '3.': 'lobarent'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'lobem', '2.': 'lobes', '3.': 'lobet'}, 'pl': {'1.': 'lobemus', '2.': 'lobetis', '3.': 'lobent'}}, 'weiblich': {'sing': {'1.': 'lobem', '2.': 'lobes', '3.': 'lobet'}, 'pl': {'1.': 'lobemus', '2.': 'lobetis', '3.': 'lobent'}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'lobatus essem', '2.': 'lobatus esses', '3.': 'lobatus esset'}, 'pl': {'1.': 'lobati essemus', '2.': 'lobati essetis', '3.': 'lobati essent'}}, 'weiblich': {'sing': {'1.': 'lobata essem', '2.': 'lobata esses', '3.': 'lobata esset'}, 'pl': {'1.': 'lobatae essemus', '2.': 'lobatae essetis', '3.': 'lobatae essent'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'lobatus sim', '2.': 'lobatus sis', '3.': 'lobatus sit'}, 'pl': {'1.': 'lobati simus', '2.': 'lobati sitis', '3.': 'lobati sint'}}, 'weiblich': {'sing': {'1.': 'lobata sim', '2.': 'lobata sis', '3.': 'lobata sit'}, 'pl': {'1.': 'lobatae simus', '2.': 'lobatae sitis', '3.': 'lobatae sint'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'lobarer', '2.': 'lobareris', '3.': 'lobaretur'}, 'pl': {'1.': 'lobaremur', '2.': 'lobaremini', '3.': 'lobarentur'}}, 'weiblich': {'sing': {'1.': 'lobarer', '2.': 'lobareris', '3.': 'lobaretur'}, 'pl': {'1.': 'lobaremur', '2.': 'lobaremini', '3.': 'lobarentur'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'lober', '2.': 'loberis', '3.': 'lobetur'}, 'pl': {'1.': 'lobemur', '2.': 'lobemini', '3.': 'lobentur'}}, 'weiblich': {'sing': {'1.': 'lober', '2.': 'loberis', '3.': 'lobetur'}, 'pl': {'1.': 'lobemur', '2.': 'lobemini', '3.': 'lobentur'}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}}}