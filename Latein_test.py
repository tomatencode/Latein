output = {}
indikativ_konjungtiv = []
aktiv_passiv = []
tempus = []
SingPl = []
person = []

def diconary_erstellen(indikativ_konjungtiv,aktiv_passiv,tempus,SingPl,person):
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


        return output



print(diconary_erstellen(indikativ_konjungtiv,aktiv_passiv,tempus,SingPl,person))