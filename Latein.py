import json
voc = {"laudare":["loben","preisen","anpriesen","gutheißen","rühmen","a"]}


#frage = input("Frage: ")
frage = "laudare"

# open a file
file1 = open("latein_ausnahmen.json", "r")

# read the file
ausnahmen_str = file1.read()
ausnahmen = json.loads(ausnahmen_str)

def übersetzung():
    for i in range(0,len(voc[frage])-1):
        print(voc[frage][i])
def konjugieren(indikativ,aktiv,zeit,mänliche_form,wort : str):
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

    elif zeit == "präsens" or zeit == "imperfekt" or zeit == "perfekt" and aktiv or zeit == "futur" or zeit == "futur2" and aktiv or zeit == "plusquamperfekt" and aktiv:
        grundform = wort.rstrip("re")

        if aktiv:
            endungsart = "aktiv"
        if not indikativ:
            endungsart = "aktiv_m"
        if not aktiv:
            endungsart = "passiv"
        if zeit == "präsens" and not indikativ:
            grundform = grundform.rstrip("a")+"e"
        if zeit == "plusquamperfekt":
            endungsart = "aktiv_m"
            if indikativ:
                grundform = grundform + "vera"
            else:
                grundform = grundform + "visse"
        if zeit == "futur2":
            grundform = grundform + "ver"
        if zeit == "imperfekt":
            if indikativ:
                grundform = grundform + "ba"
                endungsart = "aktiv_m"
            else:
                grundform = grundform + "re"
        if zeit == "futur":
            grundform = grundform + "b"
            if aktiv:
                endungsart = "futur"
            else:
                endungsart = "passiv_futur"
        if zeit == "perfekt":
            if indikativ:
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
        grundform = {"Mänlich":{"Sing":wort.rstrip("re")+"tus ","Pl":wort.rstrip("re")+"ti "},"Weiblich":{"Sing":wort.rstrip("are")+"a ","Pl":wort.rstrip("are")+"ae "}}

        if zeit == "perfekt":
            esse = konjugieren(indikativ,True,"präsens",True,"esse")
        if zeit == "plusquamperfekt":
            esse = konjugieren(indikativ,True,"imperfekt",True,"esse")
        if zeit == "futur2":
            esse = konjugieren(True,True,"futur",True,"esse")
        for SingPl in ["Sing","Pl"]:
            for p in ["1.","2.","3."]:
                output.append(grundform[mänliche_form][SingPl]+esse[int(p.rstrip("."))-1])


            
    return output
    

print(konjugieren(True,False,"plusquamperfekt","Weiblich",frage))

assert konjugieren(True,True,"präsens",True,"lauda") == ['laudo', 'laudas', 'laudat', 'laudamus', 'laudatis', 'laudant']