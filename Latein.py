import json
voc = {"laudare":["loben","preisen","anpriesen","gutheißen","rühmen","a"]}


#frage = input("Frage: ")
frage = "esse"

# open a file
file1 = open("latein_ausnahmen.json", "r")

# read the file
ausnahmen_str = file1.read()
ausnahmen = json.loads(ausnahmen_str)

def übersetzung():
    for i in range(0,len(voc[frage])-1):
        print(voc[frage][i])
def konjugieren(indikativ,aktiv,zeit,wort : str):
    output = []
    if wort in ausnahmen:
        if indikativ:
            indikativ_Konjungtiv = "indikativ"
        else:
            indikativ_Konjungtiv = "konjungtiv"
        if aktiv:
            aktiv_passiv = "aktiv"
        else:
            aktiv_passiv = "passiv"
        for SingPl in ["Sing","Pl"]:
            for p in ["1.","2.","3."]:
                output.append(ausnahmen[wort][indikativ_Konjungtiv][aktiv_passiv][zeit][SingPl][p])
    else:
        grundform = wort.rstrip("re")
        if zeit == "plusquamperfekt":
            grundform = grundform + "vera"
        if zeit == "futur2":
            grundform = grundform + "ver"
        if zeit == "imperfekt":
            grundform = grundform + "ba"
        if zeit == "futur":
            grundform = grundform + "b"
            endungsart = "futur"
        elif zeit == "perfekt":
            grundform = grundform + "v"
            endungsart = "perfekt"
        elif aktiv:
            endungsart = "aktiv"
        else:
            endungsart = "passiv"
        endungen = {"aktiv":{"Sing":{"1.":"o","2.":"s","3.":"t"},"Pl":{"1.":"mus","2.":"tis","3.":"nt"}},
                    "passiv":{"Sing":{"1.":"r","2.":"ris","3.":"tur"},"Pl":{"1.":"mur","2.":"mini","3.":"ntur"}},
                    "perfekt":{"Sing":{"1.":"i","2.":"isti","3.":"it"},"Pl":{"1.":"imus","2.":"istis","3.":"erunt"}},
                    "futur":{"Sing":{"1.":"o","2.":"is","3.":"it"},"Pl":{"1.":"imus","2.":"itis","3.":"unt"}}}
        if indikativ:
            if zeit == "präsens" or zeit == "imperfekt" or zeit == "perfekt" and aktiv or zeit == "futur" and aktiv or zeit == "futur2" and aktiv or zeit == "plusquamperfekt" and aktiv:
                for SingPl in ["Sing","Pl"]:
                    for p in ["1.","2.","3."]:
                            if endungen[endungsart][SingPl][p] == "o" and zeit == "imperfekt" or endungen[endungsart][SingPl][p] == "o" and zeit == "plusquamperfekt":
                                output.append(grundform+"m")
                            elif grundform.endswith("a") and endungen[endungsart][SingPl][p] == "o" and zeit == "präsens":
                                output.append(grundform.rstrip("a")+"o")
                            else:
                                output.append(grundform+endungen[endungsart][SingPl][p])
            
    return output
    

print(konjugieren(True,True,"präsens",frage))

assert konjugieren(True,True,"präsens","lauda") == ['laudo', 'laudas', 'laudat', 'laudamus', 'laudatis', 'laudant']