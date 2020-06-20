#initalise question variables
#info = [ ['Emily', 35, 'female', '021345789', 'Albany, Auckland'], ['Peter', 47, 'male', '021000098', 'Massey, Auckland'] , ['James', 23, 'male', '0226663456', 'Takapuna, Auckland'] ]
#symptoms = [('Emily', ['fever', 'fatigue', 'headache']), ('Peter', ['fatigue', 'loss of appetite', 'headache'])]

def combine(info, symptoms):
    patient_info = {} #final output dictionary

    patient_symptoms = {}
    for i in symptoms: #adds symtoms to a dictionary. While this doesn't make much effect now - if we had larger lists this saves us a lot of unnesecary looping over 'symtoms'. Brings time complexity to O(n + m) average from O(n*m)
        patient_symptoms[i[0]] = i[1]
    
    
    for patient in info:
        name = patient[0]

        patient_details = [patient]
        if name in patient_symptoms: #adds patient symptoms if they have any
            patient_details.append(patient_symptoms[name])

        patient_info[name] = patient_details

    return patient_info #it should be noted due to my implementation the order the names are added in is not the same as the example. I add them in order of the 'info' list. Python  dictionaries are insertion order by default. Result is the same so changing this to match example perfectly is inefficient and has no point
                        #if you did want them to be in alphabetical order (which ISNT stated, however ONE example shows it in that order instead of insertion order, you could just sort info. E.g. info = sorted(info, key=lambda x: x[0]))
#print(combine(info, symptoms)) #call function / print final output at the end
#question does not state to print the function