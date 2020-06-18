info = 'fish 15.967 salmon 12/05/2020'
info = info.split()
#could use a multi-line (triple-quotes) but this is simpler
print(f"Product: {info[0]}\nPrice: ${float(info[1]):.2f} per kilo\nType: '{info[2]}'\nDate: {info[3]}")