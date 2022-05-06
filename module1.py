import csv

pays = []
with open('countries.csv', newline='') as csvfile: # Ouverture du fichier .csv
     reader = csv.DictReader(csvfile, delimiter=';') # Objet DictReader (itérateur)
     for row in reader:
         pays.append(dict(row)) #Conversion du type OrderedD    ict en dictionnaire

print([p['Name']for p in pays if p['Currency_Name']=='Dollar'])
print([(p['Name'],int(p['Population']))for p in pays if int(p['Population']) >= int('100000000')])
