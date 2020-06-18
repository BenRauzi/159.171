#question is worded quite misleadingly.... Worded that duplicate symptoms are ignored, but not that if you use the same name it adds toth at list
#I've taken a slightly different approach to achieve better time complexity than saving it as a list of tuples initially - final output is the same. Could be more efficient but this isn't 159.172
def build():
    patients = {} #using a dict for constant loopup time - AVERAGE: O(1)
    while True:
        name = input("name: ").strip()

        if name.lower() == "quit":
            break
        symptoms = input("symptoms: ").split(",")

        if name not in patients: #if they are a new patient add them to patients
            symtoms_list = []

            for symptom in symptoms: #prevents duplicates and strips whitespace
                if symptom not in symtoms_list:
                    symtoms_list.append(symptom.strip())

            patients[name] = symtoms_list
        else: #if they are a previous patient back again, add more symptoms
            symtoms_list = patients[name]

            for symptom in symptoms: #prevents duplicates and strips whitespace
                if symptom.strip() not in symtoms_list:
                    symtoms_list.append(symptom.strip())

            patients[name] = symtoms_list

    print([(i, patients[i]) for i in patients]) #prints in format [(name1, [symptom_1, symptom_2])]

build()