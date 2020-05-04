#Based on question working we can make assumption:
#Dictionaries can have different keys - so you must account for adding uncommon keys (wording: 'values added up for common keys')

def combine(d1, d2):
    d3 = d1.copy() #Create a shallow copy of the original dict so we are not modifying it
    for i in d2:
        if not(i in d3): #if it doesn't exist in the base list (d1/d3) then create it
            d3[i] = d2[i]
        else: #if it does exist in the base list (d1/d3) then add the values together
            d3[i] += d2[i]
    return d3
