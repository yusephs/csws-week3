#import csv
#file = open('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies.csv','r', encoding="utf8")
#csvreader = csv.reader(file)
#header = next(csvreader)
#print(header)
#rows = []
#for row in csvreader:
    #rows.append(row)
#print(rows)
#file.close()

#import csv
#rows = []
#with open('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies.csv','r', encoding="utf8") as file:
    #csvreader = csv.reader(file)
    #header = next(csvreader)
    #for row in csvreader:
        #rows.append(row)
#print(header)
#print(rows)

with open('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies.csv','r', encoding="utf8") as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
#print(header)
print(rows[5:])