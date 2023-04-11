import json
from typing import List

# frage = input("Frage: ")
frage = "laudare"

# open a file
file1 = open("latein_ausnahmen.json", "r")

# read the file
ausnahmen_str = file1.read()
ausnahmen = json.loads(ausnahmen_str)

# open a file
file2 = open("vocabeln.json", "r")

# read the file
voc_str = file2.read()
voc = json.loads(voc_str)


def übersetzung():
    for i in range(1,len(voc[frage])-1):
        print(voc[frage][i])


def konjugieren(indikativ_konjunktiv : List[str],gennus_verbi : List[str],tempi : List[str],numeri : List[str],personen : List[str],geni : List[str],vocabel : List[str]):
    # aktiv passiv fachwort https://www.google.com/search?channel=fs&client=ubuntu-sn&q=aktiv+passiv+fachwort

    item = [indikativ_konjunktiv,"indikativ","konjungtiv"],[gennus_verbi,"aktiv","passiv"],[tempi,"plusquamperfekt","perfekt","imperfekt","präsens","futur","futur2"],[numeri,"sing","pl"],[personen,"1.","2.","3."],[geni,"mänlich","weiblich"]

    # replaces empty lists with default values
    for j in range(0,item.__len__()):
            if item[j][0] == []:
                for i in range(1,len(item[j])):
                    item[j][0].append(item[j][i])
    
    output = {}
    # to do: variablen umbennen
    for i in indikativ_konjunktiv:
        output[i] = {}
        for a in gennus_verbi:
            output[i][a] = {}
            for t in tempi:
                output[i][a][t] = {}
                for g in geni:
                    output[i][a][t][g] = {}
                    for n in numeri:
                        output[i][a][t][g][n] = {}
                        for p in personen:
                            output[i][a][t][g][n][p] = finden_der_richtigen_konjugationsart(i,a,t,n,p,g,vocabel)

    return output

def finden_der_richtigen_konjugationsart(i : str,a : str,t : str,n : str,p : str,g : str,vocabel : str):
    if vocabel in ausnahmen:
        return irregulaere_verben(i,a,t,n,p,vocabel)
    
    else:
        if voc[vocabel][0] != []:
            stammformen = [vocabel,voc[vocabel][0][0],voc[vocabel][0][1],voc[vocabel][0][2]]
        funktionsliste_dict = {"a_e_konjugtion":{'indikativ': {'aktiv': {'plusquamperfekt': a_e_konj_ind_akt_plus(n,p,g,stammformen[2]), 'perfekt': a_e_konj_ind_akt_perf(n,p,g,stammformen[2]),'imperfekt': a_e_konj_ind_akt_imperf(n,p,g,stammformen[0]), 'präsens': a_e_konj_ind_akt_prä(n,p,g,stammformen[0]), 'futur': a_e_konj_ind_akt_fut(n,p,g,stammformen[0]), 'futur2': a_e_konj_ind_akt_fut2(n,p,g,stammformen[2])},
        'passiv': {'plusquamperfekt': a_e_konj_ind_pas_plus(n,p,g,stammformen[0]), 'perfekt': a_e_konj_ind_pas_perf(n,p,g,stammformen[0]), 'imperfekt': a_e_konj_ind_pas_imperf(n,p,g,stammformen[0]), 'präsens': a_e_konj_ind_pas_prä(n,p,g,stammformen[0]), 'futur': a_e_konj_ind_pas_fut(n,p,g,stammformen[0]), 'futur2': a_e_konj_ind_pas_fut2(n,p,g,stammformen[0])}},
        'konjungtiv': {'aktiv': {'plusquamperfekt': a_e_konj_konj_akt_plus(n,p,g,stammformen[2]), 'perfekt': a_e_konj_konj_akt_perf(n,p,g,stammformen[2]), 'imperfekt': a_e_konj_konj_akt_imperf(n,p,g,stammformen[0]), 'präsens': a_e_konj_konj_akt_prä(n,p,g,stammformen[0]), 'futur': "", 'futur2': ""},
        'passiv': {'plusquamperfekt': a_e_konj_konj_pas_plus(n,p,g,stammformen[0]), 'perfekt': a_e_konj_konj_pas_perf(n,p,g,stammformen[0]), 'imperfekt': a_e_konj_konj_pas_imperf(n,p,g,stammformen[0]), 'präsens': a_e_konj_konj_pas_prä(n,p,g,stammformen[0]), 'futur': "", 'futur2': ""}}}}
        return funktionsliste_dict['a_e_konjugtion'][i][a][t]


def irregulaere_verben(i,a,t,n,p,Vocabel : str):

    return ausnahmen[Vocabel][i][a][t][n][p]

# a-konjugation indikativ aktiv
def a_e_konj_ind_akt_prä(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"o","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = ""
    if n == "sing" and p == "1." and voc[vocabel][2] == "a":
        grundform = vocabel.partition("are")[0]
    else:
        grundform = vocabel.partition("re")[0]
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_e_konj_ind_akt_imperf(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "ba"
    grundform = vocabel.partition("re")[0]
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_e_konj_ind_akt_perf(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"i","2.":"isti","3.":"it"},
                "pl":{"1.":"imus","2.":"istis","3.":"erunt"}}
    tempuszeichen = ""
    grundform = vocabel.rstrip("i")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_e_konj_ind_akt_plus(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "era"
    grundform = vocabel.rstrip("i")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_e_konj_ind_akt_fut(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"o","2.":"is","3.":"it"},
                "pl":{"1.":"imus","2.":"itis","3.":"unt"}}
    tempuszeichen = "b"
    grundform = vocabel.partition("re")[0]
    return grundform  + tempuszeichen + endungen_dict[n][p]

def a_e_konj_ind_akt_fut2(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"o","2.":"is","3.":"it"},
                "pl":{"1.":"imus","2.":"itis","3.":"int"}}
    tempuszeichen = "er"
    grundform = vocabel.partition("i")[0]
    return grundform  + tempuszeichen + endungen_dict[n][p]

# a-konjugation indikativ passiv
def a_e_konj_ind_pas_prä(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"or","2.":"aris","3.":"atur"},
                "pl":{"1.":"amur","2.":"amini","3.":"antur"}}
    tempuszeichen = ""
    grundform = vocabel.rstrip("are")
    return grundform  + tempuszeichen + endungen_dict[n][p]


def a_e_konj_ind_pas_imperf(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"r","2.":"ris","3.":"tur"},
                "pl":{"1.":"mur","2.":"mini","3.":"ntur"}}
    tempuszeichen = "ba"
    grundform = vocabel.partition("re")[0]
    return grundform  + tempuszeichen + endungen_dict[n][p]

def a_e_konj_ind_pas_fut(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"or","2.":"eris","3.":"itur"},
                "pl":{"1.":"imur","2.":"imini","3.":"untur"}}
    tempuszeichen = "b"
    grundform = vocabel.partition("re")[0]
    return grundform  + tempuszeichen + endungen_dict[n][p]


def a_e_konj_ind_pas_perf(n : str,p : str,g : str,vocabel : str)->str:
    sonderzeichen_dict = {"mänlich":{"sing":"tus ","pl":"ti "},
                          "weiblich":{"sing":"ta ","pl":"tae "}}
    if voc[vocabel][2] == "a":
        grundform = vocabel.partition("re")[0]
    elif voc[vocabel][2] == "e":
        grundform = vocabel.partition("ere")[0] + "i"
    esse_form_str = konjugieren(["indikativ"],["aktiv"],["präsens"],[n],[p],["mänlich"],"esse") ["indikativ"]["aktiv"]["präsens"]["mänlich"][n][p]
    return grundform  + sonderzeichen_dict[g][n] + esse_form_str

def a_e_konj_ind_pas_plus(n : str,p : str,g : str,vocabel : str)->str:
    sonderzeichen_dict = {"mänlich":{"sing":"tus ","pl":"ti "},
                          "weiblich":{"sing":"ta ","pl":"tae "}}
    if voc[vocabel][2] == "a":
        grundform = vocabel.partition("re")[0]
    elif voc[vocabel][2] == "e":
        grundform = vocabel.partition("ere")[0] + "i"
    esse_form_str = konjugieren(["indikativ"],["aktiv"],["imperfekt"],[n],[p],["mänlich"],"esse") ["indikativ"]["aktiv"]["imperfekt"]["mänlich"][n][p]
    return grundform  + sonderzeichen_dict[g][n] + esse_form_str

def a_e_konj_ind_pas_fut2(n : str,p : str,g : str,vocabel : str)->str:
    sonderzeichen_dict = {"mänlich":{"sing":"tus ","pl":"ti "},
                          "weiblich":{"sing":"ta ","pl":"tae "}}
    if voc[vocabel][2] == "a":
        grundform = vocabel.partition("re")[0]
    elif voc[vocabel][2] == "e":
        grundform = vocabel.partition("ere")[0] + "i"
    esse_form_str = konjugieren(["indikativ"],["aktiv"],["futur"],[n],[p],["mänlich"],"esse") ["indikativ"]["aktiv"]["futur"]["mänlich"][n][p]
    return grundform  + sonderzeichen_dict[g][n] + esse_form_str

# a-konjugation konjungtiv aktiv
def a_e_konj_konj_akt_prä(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    
    if voc[vocabel][2] == "a":
        tempuszeichen = "e"
        grundform = vocabel.partition("are")[0]
    elif voc[vocabel][2] == "e":
        tempuszeichen = "a"
        grundform = vocabel.partition("re")[0]
    
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_e_konj_konj_akt_imperf(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = ""
    grundform = vocabel.rstrip("")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_e_konj_konj_akt_perf(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "eri"
    grundform = vocabel.rstrip("i")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_e_konj_konj_akt_plus(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"m","2.":"s","3.":"t"},
                "pl":{"1.":"mus","2.":"tis","3.":"nt"}}
    tempuszeichen = "sse"
    grundform = vocabel.rstrip("")
    return grundform + tempuszeichen + endungen_dict[n][p]

# a-konjugation konjungtiv passiv
def a_e_konj_konj_pas_prä(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"r","2.":"ris","3.":"tur"},
                "pl":{"1.":"mur","2.":"mini","3.":"ntur"}}
    
    if voc[vocabel][2] == "a":
        tempuszeichen = "e"
        grundform = vocabel.partition("are")[0]
    elif voc[vocabel][2] == "e":
        tempuszeichen = "a"
        grundform = vocabel.partition("re")[0]

    return grundform + tempuszeichen + endungen_dict[n][p]

def a_e_konj_konj_pas_imperf(n : str,p : str,g : str,vocabel : str)->str:
    endungen_dict = {"sing":{"1.":"r","2.":"ris","3.":"tur"},
                "pl":{"1.":"mur","2.":"mini","3.":"ntur"}}
    tempuszeichen = ""
    grundform = vocabel.rstrip("")
    return grundform + tempuszeichen + endungen_dict[n][p]

def a_e_konj_konj_pas_perf(n : str,p : str,g : str,vocabel : str)->str:
    sonderzeichen_dict = {"mänlich":{"sing":"tus ","pl":"ti "},"weiblich":{"sing":"ta ","pl":"tae "}}
    if voc[vocabel][2] == "a":
        grundform = vocabel.partition("re")[0]
    elif voc[vocabel][2] == "e":
        grundform = vocabel.partition("ere")[0] + "i"
    esse_form_str = konjugieren(["konjungtiv"],["aktiv"],["präsens"],[n],[p],["mänlich"],"esse") ["konjungtiv"]["aktiv"]["präsens"]["mänlich"][n][p]
    return grundform  + sonderzeichen_dict[g][n] + esse_form_str

def a_e_konj_konj_pas_plus(n : str,p : str,g : str,vocabel : str)->str:
    sonderzeichen_dict = {"mänlich":{"sing":"tus ","pl":"ti "},"weiblich":{"sing":"ta ","pl":"tae "}}
    if voc[vocabel][2] == "a":
        grundform = vocabel.partition("re")[0]
    elif voc[vocabel][2] == "e":
        grundform = vocabel.partition("ere")[0] + "i"
    esse_form_str = konjugieren(["konjungtiv"],["aktiv"],["imperfekt"],[n],[p],["mänlich"],"esse") ["konjungtiv"]["aktiv"]["imperfekt"]["mänlich"][n][p]
    return  grundform  + sonderzeichen_dict[g][n] + esse_form_str

print(json.dumps(konjugieren([],[],[],[],[],[],"tacere"),indent=2))


# Tests 
assert konjugieren([],[],[],[],[],[],"esse") == {'indikativ': {'aktiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'fueram', '2.': 'fueras', '3.': 'fuerat'}, 'pl': {'1.': 'fueramus', '2.': 'fueratis', '3.': 'fuerant'}}, 'weiblich': {'sing': {'1.': 'fueram', '2.': 'fueras', '3.': 'fuerat'}, 'pl': {'1.': 'fueramus', '2.': 'fueratis', '3.': 'fuerant'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'fui', '2.': 'fuisti', '3.': 'fuit'}, 'pl': {'1.': 'fuimus', '2.': 'fuistis', '3.': 'fuerant'}}, 'weiblich': {'sing': {'1.': 'fui', '2.': 'fuisti', '3.': 'fuit'}, 'pl': {'1.': 'fuimus', '2.': 'fuistis', '3.': 'fuerant'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'eram', '2.': 'eras', '3.': 'erat'}, 'pl': {'1.': 'eramus', '2.': 'eratis', '3.': 'erant'}}, 'weiblich': {'sing': {'1.': 'eram', '2.': 'eras', '3.': 'erat'}, 'pl': {'1.': 'eramus', '2.': 'eratis', '3.': 'erant'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'sum', '2.': 'es', '3.': 'est'}, 'pl': {'1.': 'sumus', '2.': 'estis', '3.': 'sunt'}}, 'weiblich': {'sing': {'1.': 'sum', '2.': 'es', '3.': 'est'}, 'pl': {'1.': 'sumus', '2.': 'estis', '3.': 'sunt'}}}, 'futur': {'mänlich': {'sing': {'1.': 'ero', '2.': 'eris', '3.': 'erit'}, 'pl': {'1.': 'erimus', '2.': 'eritis', '3.': 'erunt'}}, 'weiblich': {'sing': {'1.': 'ero', '2.': 'eris', '3.': 'erit'}, 'pl': {'1.': 'erimus', '2.': 'eritis', '3.': 'erunt'}}}, 'futur2': {'mänlich': {'sing': {'1.': 'fuero', '2.': 'fueris', '3.': 'fuerit'}, 'pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}, 'weiblich': {'sing': {'1.': 'fuero', '2.': 'fueris', '3.': 'fuerit'}, 'pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'perfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'imperfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'präsens': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '"', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '"', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}}, 'konjungtiv': {'aktiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'fuissem', '2.': 'fuisses', '3.': 'fuisset'}, 'pl': {'1.': 'fuissemus', '2.': 'fuissetis', '3.': 'fuissent'}}, 'weiblich': {'sing': {'1.': 'fuissem', '2.': 'fuisses', '3.': 'fuisset'}, 'pl': {'1.': 'fuissemus', '2.': 'fuissetis', '3.': 'fuissent'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'fuerim', '2.': 'fueris', '3.': 'fuerit'}, 'pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}, 'weiblich': {'sing': {'1.': 'fuerim', '2.': 'fueris', '3.': 'fuerit'}, 'pl': {'1.': 'fuerimus', '2.': 'fueritis', '3.': 'fuerint'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'essem', '2.': 'esses', '3.': 'esset'}, 'pl': {'1.': 'essemus', '2.': 'essetis', '3.': 'essent'}}, 'weiblich': {'sing': {'1.': 'essem', '2.': 'esses', '3.': 'esset'}, 'pl': {'1.': 'essemus', '2.': 'essetis', '3.': 'essent'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'sim', '2.': 'sis', '3.': 'sit'}, 'pl': {'1.': 'simus', '2.': 'sitis', '3.': 'sint'}}, 'weiblich': {'sing': {'1.': 'sim', '2.': 'sis', '3.': 'sit'}, 'pl': {'1.': 'simus', '2.': 'sitis', '3.': 'sint'}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'perfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'imperfekt': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'präsens': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}}}
assert konjugieren([],[],[],[],[],[],"laudare") == {'indikativ':{'aktiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'laudaveram', '2.': 'laudaveras', '3.': 'laudaverat'}, 'pl': {'1.': 'laudaveramus', '2.': 'laudaveratis', '3.': 'laudaverant'}}, 'weiblich': {'sing': {'1.': 'laudaveram', '2.': 'laudaveras', '3.': 'laudaverat'}, 'pl': {'1.': 'laudaveramus', '2.': 'laudaveratis', '3.': 'laudaverant'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'laudavi', '2.': 'laudavisti', '3.': 'laudavit'}, 'pl': {'1.': 'laudavimus', '2.': 'laudavistis', '3.': 'laudaverunt'}}, 'weiblich': {'sing': {'1.': 'laudavi', '2.': 'laudavisti', '3.': 'laudavit'}, 'pl': {'1.': 'laudavimus', '2.': 'laudavistis', '3.': 'laudaverunt'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'laudabam', '2.': 'laudabas', '3.': 'laudabat'}, 'pl': {'1.': 'laudabamus', '2.': 'laudabatis', '3.': 'laudabant'}}, 'weiblich': {'sing': {'1.': 'laudabam', '2.': 'laudabas', '3.': 'laudabat'}, 'pl': {'1.': 'laudabamus', '2.': 'laudabatis', '3.': 'laudabant'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'laudo', '2.': 'laudas', '3.': 'laudat'}, 'pl': {'1.': 'laudamus', '2.': 'laudatis', '3.': 'laudant'}}, 'weiblich': {'sing': {'1.': 'laudo', '2.': 'laudas', '3.': 'laudat'}, 'pl': {'1.': 'laudamus', '2.': 'laudatis', '3.': 'laudant'}}}, 'futur': {'mänlich': {'sing': {'1.': 'laudabo', '2.': 'laudabis', '3.': 'laudabit'}, 'pl': {'1.': 'laudabimus', '2.': 'laudabitis', '3.': 'laudabunt'}}, 'weiblich': {'sing': {'1.': 'laudabo', '2.': 'laudabis', '3.': 'laudabit'}, 'pl': {'1.': 'laudabimus', '2.': 'laudabitis', '3.': 'laudabunt'}}}, 'futur2': {'mänlich': {'sing': {'1.': 'laudavero', '2.': 'laudaveris', '3.': 'laudaverit'}, 'pl': {'1.': 'laudaverimus', '2.': 'laudaveritis', '3.': 'laudaverint'}}, 'weiblich': {'sing': {'1.': 'laudavero', '2.': 'laudaveris', '3.': 'laudaverit'}, 'pl': {'1.': 'laudaverimus', '2.': 'laudaveritis', '3.': 'laudaverint'}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'laudatus eram', '2.': 'laudatus eras', '3.': 'laudatus erat'}, 'pl': {'1.': 'laudati eramus', '2.': 'laudati eratis', '3.': 'laudati erant'}}, 'weiblich': {'sing': {'1.': 'laudata eram', '2.': 'laudata eras', '3.': 'laudata erat'}, 'pl': {'1.': 'laudatae eramus', '2.': 'laudatae eratis', '3.': 'laudatae erant'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'laudatus sum', '2.': 'laudatus es', '3.': 'laudatus est'}, 'pl': {'1.': 'laudati sumus', '2.': 'laudati estis', '3.': 'laudati sunt'}}, 'weiblich': {'sing': {'1.': 'laudata sum', '2.': 'laudata es', '3.': 'laudata est'}, 'pl': {'1.': 'laudatae sumus', '2.': 'laudatae estis', '3.': 'laudatae sunt'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'laudabar', '2.': 'laudabaris', '3.': 'laudabatur'}, 'pl': {'1.': 'laudabamur', '2.': 'laudabamini', '3.': 'laudabantur'}}, 'weiblich': {'sing': {'1.': 'laudabar', '2.': 'laudabaris', '3.': 'laudabatur'}, 'pl': {'1.': 'laudabamur', '2.': 'laudabamini', '3.': 'laudabantur'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'laudor', '2.': 'laudaris', '3.': 'laudatur'}, 'pl': {'1.': 'laudamur', '2.': 'laudamini', '3.': 'laudantur'}}, 'weiblich': {'sing': {'1.': 'laudor', '2.': 'laudaris', '3.': 'laudatur'}, 'pl': {'1.': 'laudamur', '2.': 'laudamini', '3.': 'laudantur'}}}, 'futur': {'mänlich': {'sing': {'1.': 'laudabor', '2.': 'laudaberis', '3.': 'laudabitur'}, 'pl': {'1.': 'laudabimur', '2.': 'laudabimini', '3.': 'laudabuntur'}}, 'weiblich': {'sing': {'1.': 'laudabor', '2.': 'laudaberis', '3.': 'laudabitur'}, 'pl': {'1.': 'laudabimur', '2.': 'laudabimini', '3.': 'laudabuntur'}}}, 'futur2': {'mänlich': {'sing': {'1.': 'laudatus ero', '2.': 'laudatus eris', '3.': 'laudatus erit'}, 'pl': {'1.': 'laudati erimus', '2.': 'laudati eritis', '3.': 'laudati erunt'}}, 'weiblich': {'sing': {'1.': 'laudata ero', '2.': 'laudata eris', '3.': 'laudata erit'}, 'pl': {'1.': 'laudatae erimus', '2.': 'laudatae eritis', '3.': 'laudatae erunt'}}}}}, 'konjungtiv': {'aktiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'laudavissem', '2.': 'laudavisses', '3.': 'laudavisset'}, 'pl': {'1.': 'laudavissemus', '2.': 'laudavissetis', '3.': 'laudavissent'}}, 'weiblich': {'sing': {'1.': 'laudavissem', '2.': 'laudavisses', '3.': 'laudavisset'}, 'pl': {'1.': 'laudavissemus', '2.': 'laudavissetis', '3.': 'laudavissent'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'laudaverim', '2.': 'laudaveris', '3.': 'laudaverit'}, 'pl': {'1.': 'laudaverimus', '2.': 'laudaveritis', '3.': 'laudaverint'}}, 'weiblich': {'sing': {'1.': 'laudaverim', '2.': 'laudaveris', '3.': 'laudaverit'}, 'pl': {'1.': 'laudaverimus', '2.': 'laudaveritis', '3.': 'laudaverint'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'laudarem', '2.': 'laudares', '3.': 'laudaret'}, 'pl': {'1.': 'laudaremus', '2.': 'laudaretis', '3.': 'laudarent'}}, 'weiblich': {'sing': {'1.': 'laudarem', '2.': 'laudares', '3.': 'laudaret'}, 'pl': {'1.': 'laudaremus', '2.': 'laudaretis', '3.': 'laudarent'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'laudem', '2.': 'laudes', '3.': 'laudet'}, 'pl': {'1.': 'laudemus', '2.': 'laudetis', '3.': 'laudent'}}, 'weiblich': {'sing': {'1.': 'laudem', '2.': 'laudes', '3.': 'laudet'}, 'pl': {'1.': 'laudemus', '2.': 'laudetis', '3.': 'laudent'}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'laudatus essem', '2.': 'laudatus esses', '3.': 'laudatus esset'}, 'pl': {'1.': 'laudati essemus', '2.': 'laudati essetis', '3.': 'laudati essent'}}, 'weiblich': {'sing': {'1.': 'laudata essem', '2.': 'laudata esses', '3.': 'laudata esset'}, 'pl': {'1.': 'laudatae essemus', '2.': 'laudatae essetis', '3.': 'laudatae essent'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'laudatus sim', '2.': 'laudatus sis', '3.': 'laudatus sit'}, 'pl': {'1.': 'laudati simus', '2.': 'laudati sitis', '3.': 'laudati sint'}}, 'weiblich': {'sing': {'1.': 'laudata sim', '2.': 'laudata sis', '3.': 'laudata sit'}, 'pl': {'1.': 'laudatae simus', '2.': 'laudatae sitis', '3.': 'laudatae sint'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'laudarer', '2.': 'laudareris', '3.': 'laudaretur'}, 'pl': {'1.': 'laudaremur', '2.': 'laudaremini', '3.': 'laudarentur'}}, 'weiblich': {'sing': {'1.': 'laudarer', '2.': 'laudareris', '3.': 'laudaretur'}, 'pl': {'1.': 'laudaremur', '2.': 'laudaremini', '3.': 'laudarentur'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'lauder', '2.': 'lauderis', '3.': 'laudetur'}, 'pl': {'1.': 'laudemur', '2.': 'laudemini', '3.': 'laudentur'}}, 'weiblich': {'sing': {'1.': 'lauder', '2.': 'lauderis', '3.': 'laudetur'}, 'pl': {'1.': 'laudemur', '2.': 'laudemini', '3.': 'laudentur'}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}}}
assert konjugieren([],[],[],[],[],[],"tacere") == {'indikativ': {'aktiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'tacueram', '2.': 'tacueras', '3.': 'tacuerat'}, 'pl': {'1.': 'tacueramus', '2.': 'tacueratis', '3.': 'tacuerant'}}, 'weiblich': {'sing': {'1.': 'tacueram', '2.': 'tacueras', '3.': 'tacuerat'}, 'pl': {'1.': 'tacueramus', '2.': 'tacueratis', '3.': 'tacuerant'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'tacui', '2.': 'tacuisti', '3.': 'tacuit'}, 'pl': {'1.': 'tacuimus', '2.': 'tacuistis', '3.': 'tacuerunt'}}, 'weiblich': {'sing': {'1.': 'tacui', '2.': 'tacuisti', '3.': 'tacuit'}, 'pl': {'1.': 'tacuimus', '2.': 'tacuistis', '3.': 'tacuerunt'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'tacebam', '2.': 'tacebas', '3.': 'tacebat'}, 'pl': {'1.': 'tacebamus', '2.': 'tacebatis', '3.': 'tacebant'}}, 'weiblich': {'sing': {'1.': 'tacebam', '2.': 'tacebas', '3.': 'tacebat'}, 'pl': {'1.': 'tacebamus', '2.': 'tacebatis', '3.': 'tacebant'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'taceo', '2.': 'taces', '3.': 'tacet'}, 'pl': {'1.': 'tacemus', '2.': 'tacetis', '3.': 'tacent'}}, 'weiblich': {'sing': {'1.': 'taceo', '2.': 'taces', '3.': 'tacet'}, 'pl': {'1.': 'tacemus', '2.': 'tacetis', '3.': 'tacent'}}}, 'futur': {'mänlich': {'sing': {'1.': 'tacebo', '2.': 'tacebis', '3.': 'tacebit'}, 'pl': {'1.': 'tacebimus', '2.': 'tacebitis', '3.': 'tacebunt'}}, 'weiblich': {'sing': {'1.': 'tacebo', '2.': 'tacebis', '3.': 'tacebit'}, 'pl': {'1.': 'tacebimus', '2.': 'tacebitis', '3.': 'tacebunt'}}}, 'futur2': {'mänlich': {'sing': {'1.': 'tacuero', '2.': 'tacueris', '3.': 'tacuerit'}, 'pl': {'1.': 'tacuerimus', '2.': 'tacueritis', '3.': 'tacuerint'}}, 'weiblich': {'sing': {'1.': 'tacuero', '2.': 'tacueris', '3.': 'tacuerit'}, 'pl': {'1.': 'tacuerimus', '2.': 'tacueritis', '3.': 'tacuerint'}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'tacitus eram', '2.': 'tacitus eras', '3.': 'tacitus erat'}, 'pl': {'1.': 'taciti eramus', '2.': 'taciti eratis', '3.': 'taciti erant'}}, 'weiblich': {'sing': {'1.': 'tacita eram', '2.': 'tacita eras', '3.': 'tacita erat'}, 'pl': {'1.': 'tacitae eramus', '2.': 'tacitae eratis', '3.': 'tacitae erant'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'tacitus sum', '2.': 'tacitus es', '3.': 'tacitus est'}, 'pl': {'1.': 'taciti sumus', '2.': 'taciti estis', '3.': 'taciti sunt'}}, 'weiblich': {'sing': {'1.': 'tacita sum', '2.': 'tacita es', '3.': 'tacita est'}, 'pl': {'1.': 'tacitae sumus', '2.': 'tacitae estis', '3.': 'tacitae sunt'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'tacebar', '2.': 'tacebaris', '3.': 'tacebatur'}, 'pl': {'1.': 'tacebamur', '2.': 'tacebamini', '3.': 'tacebantur'}}, 'weiblich': {'sing': {'1.': 'tacebar', '2.': 'tacebaris', '3.': 'tacebatur'}, 'pl': {'1.': 'tacebamur', '2.': 'tacebamini', '3.': 'tacebantur'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'tacor', '2.': 'tacaris', '3.': 'tacatur'}, 'pl': {'1.': 'tacamur', '2.': 'tacamini', '3.': 'tacantur'}}, 'weiblich': {'sing': {'1.': 'tacor', '2.': 'tacaris', '3.': 'tacatur'}, 'pl': {'1.': 'tacamur', '2.': 'tacamini', '3.': 'tacantur'}}}, 'futur': {'mänlich': {'sing': {'1.': 'tacebor', '2.': 'taceberis', '3.': 'tacebitur'}, 'pl': {'1.': 'tacebimur', '2.': 'tacebimini', '3.': 'tacebuntur'}}, 'weiblich': {'sing': {'1.': 'tacebor', '2.': 'taceberis', '3.': 'tacebitur'}, 'pl': {'1.': 'tacebimur', '2.': 'tacebimini', '3.': 'tacebuntur'}}}, 'futur2': {'mänlich': {'sing': {'1.': 'tacitus ero', '2.': 'tacitus eris', '3.': 'tacitus erit'}, 'pl': {'1.': 'taciti erimus', '2.': 'taciti eritis', '3.': 'taciti erunt'}}, 'weiblich': {'sing': {'1.': 'tacita ero', '2.': 'tacita eris', '3.': 'tacita erit'}, 'pl': {'1.': 'tacitae erimus', '2.': 'tacitae eritis', '3.': 'tacitae erunt'}}}}}, 'konjungtiv': {'aktiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'tacuissem', '2.': 'tacuisses', '3.': 'tacuisset'}, 'pl': {'1.': 'tacuissemus', '2.': 'tacuissetis', '3.': 'tacuissent'}}, 'weiblich': {'sing': {'1.': 'tacuissem', '2.': 'tacuisses', '3.': 'tacuisset'}, 'pl': {'1.': 'tacuissemus', '2.': 'tacuissetis', '3.': 'tacuissent'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'tacuerim', '2.': 'tacueris', '3.': 'tacuerit'}, 'pl': {'1.': 'tacuerimus', '2.': 'tacueritis', '3.': 'tacuerint'}}, 'weiblich': {'sing': {'1.': 'tacuerim', '2.': 'tacueris', '3.': 'tacuerit'}, 'pl': {'1.': 'tacuerimus', '2.': 'tacueritis', '3.': 'tacuerint'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'tacerem', '2.': 'taceres', '3.': 'taceret'}, 'pl': {'1.': 'taceremus', '2.': 'taceretis', '3.': 'tacerent'}}, 'weiblich': {'sing': {'1.': 'tacerem', '2.': 'taceres', '3.': 'taceret'}, 'pl': {'1.': 'taceremus', '2.': 'taceretis', '3.': 'tacerent'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'taceam', '2.': 'taceas', '3.': 'taceat'}, 'pl': {'1.': 'taceamus', '2.': 'taceatis', '3.': 'taceant'}}, 'weiblich': {'sing': {'1.': 'taceam', '2.': 'taceas', '3.': 'taceat'}, 'pl': {'1.': 'taceamus', '2.': 'taceatis', '3.': 'taceant'}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}, 'passiv': {'plusquamperfekt': {'mänlich': {'sing': {'1.': 'tacitus essem', '2.': 'tacitus esses', '3.': 'tacitus esset'}, 'pl': {'1.': 'taciti essemus', '2.': 'taciti essetis', '3.': 'taciti essent'}}, 'weiblich': {'sing': {'1.': 'tacita essem', '2.': 'tacita esses', '3.': 'tacita esset'}, 'pl': {'1.': 'tacitae essemus', '2.': 'tacitae essetis', '3.': 'tacitae essent'}}}, 'perfekt': {'mänlich': {'sing': {'1.': 'tacitus sim', '2.': 'tacitus sis', '3.': 'tacitus sit'}, 'pl': {'1.': 'taciti simus', '2.': 'taciti sitis', '3.': 'taciti sint'}}, 'weiblich': {'sing': {'1.': 'tacita sim', '2.': 'tacita sis', '3.': 'tacita sit'}, 'pl': {'1.': 'tacitae simus', '2.': 'tacitae sitis', '3.': 'tacitae sint'}}}, 'imperfekt': {'mänlich': {'sing': {'1.': 'tacerer', '2.': 'tacereris', '3.': 'taceretur'}, 'pl': {'1.': 'taceremur', '2.': 'taceremini', '3.': 'tacerentur'}}, 'weiblich': {'sing': {'1.': 'tacerer', '2.': 'tacereris', '3.': 'taceretur'}, 'pl': {'1.': 'taceremur', '2.': 'taceremini', '3.': 'tacerentur'}}}, 'präsens': {'mänlich': {'sing': {'1.': 'tacear', '2.': 'tacearis', '3.': 'taceatur'}, 'pl': {'1.': 'taceamur', '2.': 'taceamini', '3.': 'taceantur'}}, 'weiblich': {'sing': {'1.': 'tacear', '2.': 'tacearis', '3.': 'taceatur'}, 'pl': {'1.': 'taceamur', '2.': 'taceamini', '3.': 'taceantur'}}}, 'futur': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}, 'futur2': {'mänlich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}, 'weiblich': {'sing': {'1.': '', '2.': '', '3.': ''}, 'pl': {'1.': '', '2.': '', '3.': ''}}}}}}