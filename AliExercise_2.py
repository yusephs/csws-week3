import csv
def searchByMovieTitle():
    movie_title=str(input('Enter Movie Title\n'))
    csv_file=csv.reader(open('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies.csv','r'))
    for row in csv_file:
        if movie_title in row[1]:
            print(row)

def searchByGeners():
    geners=str(input('Enter Geners to Show Geners\n'))
    csv_file=csv.reader(open('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies.csv','r'))

    for row in csv_file:
        if geners in row[5]:
            print(row)

print('Enter 1 to search by Movie title')
print('Enter 2 to search by Geners')

src=int(input('Enter here: '))

if src==1:
    searchByMovieTitle()
elif src==2:
    searchByGeners()
else:
    print('Sorry, invalid')
