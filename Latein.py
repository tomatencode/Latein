import json
import copy
voc = {"laudare":["loben","preisen","anpriesen","gutheißen","rühmen","a"]}


#frage = input("Frage: ")
frage = "esse"

# open a file
file1 = open("latein_ausnahmen.json", "r")

# read the file
ausnahmen_str = file1.read()
ausnahmen = json.loads(ausnahmen_str)

def dictionary_erstellen(indikativ_konjungtiv,aktiv_passiv,tempus,SingPl,person):
    output = {}
    item = [indikativ_konjungtiv,"indikativ","konjungtiv"],[aktiv_passiv,"aktiv","passiv"],[tempus,"plusquamperfekt","perfekt","imperfekt","präsens","futur","futur2"],[SingPl,"Sing","Pl"],[person,"1.","2.","3."]
    for j in range(0,5):
            if item[j][0] == []:
                for i in range(1,len(item[j])):
                    item[j][0].append(item[j][i])
        
    for i in indikativ_konjungtiv:
        output[i] = {}
        for a in aktiv_passiv:
            output[i][a] = {}
            for t in tempus:
                output[i][a][t] = {}
                for s in SingPl:
                    output[i][a][t][s] = {}
                    for p in person:
                        output[i][a][t][s][p] = ""
    print(output)
    return output
def übersetzung():
    for i in range(0,len(voc[frage])-1):
        print(voc[frage][i])



def konjugieren(indikativ_oder_konjungtiv,aktiv_oder_passiv,zeiten,SingPl,p,mänliche_form = "", wort : str = ""):
    output = dictionary_erstellen(indikativ_oder_konjungtiv,aktiv_oder_passiv,zeiten,SingPl,p)
    for indikativ_konjungtiv in indikativ_oder_konjungtiv:
        for aktiv_passiv in aktiv_oder_passiv:
            for zeit in zeiten:
                if wort in ausnahmen:
                    for SingPl in ["Sing","Pl"]:
                        for p in ["1.","2.","3."]:
                            output[indikativ_konjungtiv][aktiv_passiv][zeit][SingPl][p] = ausnahmen[indikativ_konjungtiv][aktiv_passiv][zeit][SingPl][p]
                else:
                    if zeit == ["präsens"] or zeit == ["imperfekt"] or zeit == ["perfekt"] and aktiv_passiv == ["aktiv"] or zeit == ["futur"] or zeit == ["futur2"] and aktiv_passiv == ["aktiv"] or zeit == ["plusquamperfekt"] and aktiv_passiv == ["aktiv"]:
                        grundform = wort.rstrip("re")

                        if aktiv_passiv == "aktiv":
                            endungsart = "aktiv"
                        if not indikativ_konjungtiv == "indikativ":
                            endungsart = "aktiv_m"
                        if aktiv_passiv == "passiv":
                            endungsart = "passiv"
                        if zeit == "präsens" and indikativ_konjungtiv == "konjungtiv":
                            grundform = grundform.rstrip("a")+"e"
                        if zeit == "plusquamperfekt":
                            endungsart = "aktiv_m"
                            if indikativ_konjungtiv == "indikativ":
                                grundform = grundform + "vera"
                            else:
                                grundform = grundform + "visse"
                        if zeit == "futur2":
                            grundform = grundform + "ver"
                        if zeit == "imperfekt":
                            if indikativ_konjungtiv == "indikativ":
                                grundform = grundform + "ba"
                                endungsart = "aktiv_m"
                            else:
                                grundform = grundform + "re"
                        if zeit == "futur":
                            grundform = grundform + "b"
                            if aktiv_passiv == "aktiv":
                                endungsart = "futur"
                            else:
                                endungsart = "passiv_futur"
                        if zeit == "perfekt":
                            if indikativ_konjungtiv == "indikativ":
                                grundform = grundform + "v"
                                endungsart = "perfekt"
                            else:
                                grundform = grundform + "vri"
                        
                        endungen = {"aktiv":{"Sing":{"1.":"o","2.":"s","3.":"t"},"Pl":{"1.":"mus","2.":"tis","3.":"nt"}},
                                    "aktiv_m":{"Sing":{"1.":"m","2.":"s","3.":"t"},"Pl":{"1.":"mus","2.":"tis","3.":"nt"}},
                                    "passiv":{"Sing":{"1.":"r","2.":"ris","3.":"tur"},"Pl":{"1.":"mur","2.":"mini","3.":"ntur"}},
                                    "perfekt":{"Sing":{"1.":"i","2.":"isti","3.":"it"},"Pl":{"1.":"imus","2.":"istis","3.":"erunt"}},
                                    "futur":{"Sing":{"1.":"o","2.":"is","3.":"it"},"Pl":{"1.":"imus","2.":"itis","3.":"unt"}},
                                    "passiv_futur":{"Sing":{"1.":"or","2.":"eris","3.":"itur"},"Pl":{"1.":"imus","2.":"itis","3.":"untur"}}}
                        for SingPl in ["Sing","Pl"]:
                            for p in ["1.","2.","3."]:
                                    if grundform.endswith("a") and endungen[endungsart][SingPl][p] == "o" and zeit == "präsens":
                                        output.append(grundform.rstrip("a")+"o")
                                    elif grundform.endswith("a") and endungen[endungsart][SingPl][p] == "r" and zeit == "präsens":
                                        output.append(grundform.rstrip("a")+"or")
                                    else:
                                        output.append(grundform+endungen[endungsart][SingPl][p])

                    else:
                        grundform = {"mänlich":{"-1":wort.rstrip("re")+"tus ","2":wort.rstrip("re")+"ti "},"weiblich":{"-1":wort.rstrip("are")+"a ","2":wort.rstrip("are")+"ae "}}

                        if zeit == "perfekt":
                            esse = konjugieren(indikativ_konjungtiv,"aktiv","präsens","mänlich","esse")
                        if zeit == "plusquamperfekt":
                            esse = konjugieren(indikativ_konjungtiv,"aktiv","imperfekt","mänlich","esse")
                        if zeit == "futur2":
                            esse = konjugieren("indikatv","aktiv","futur","mänlich","esse")
                        for SingPl in [-1,2]:
                            for p in [1,2,3]:
                                output.append(grundform[mänliche_form][str(SingPl)]+esse[p+SingPl])

    return output
    

print(konjugieren(["indikativ"],["aktiv"],["präsens"],[],[],["mänlich"],frage))

assert konjugieren("indikativ","aktiv","präsens","","","mänlich","lauda") == ['laudo', 'laudas', 'laudat', 'laudamus', 'laudatis', 'laudant']