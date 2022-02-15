import csv
#from decimal import ROUND_DOWN
#from tkinter.tix import COLUMN, ROW
csv_file=csv.reader(open('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies.csv','r'))
print(csv_file)

def searchByMovieTitle():
    movie_title=str(input('Enter Movie Title\n'))
    csv_file=csv.reader(open('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies.csv','r'))
    for row in csv_file:
        if movie_title in row[1]:
            print(row[5])

def searchByGenres():
    genres=str(input('Enter Genress to Show Actors and run time\n'))
    csv_file=csv.reader(open('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies.csv','r'))

    for row in csv_file:
        if genres in row[5]:
            print(row[8:11])

def searchByDirector():
    director=str(input('Enter Director Name to show the Genres \n'))
    csv_file=csv.reader(open('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Desktop/computer scince workshop/dataset/rotten_tomatoes_movies.csv','r'))

    for row in csv_file:
        if director in row [6]:
            print (row [5])


print('Enter 1 to search by Movie title')
print('Enter 2 to search by Geners')
print('Enter 3 to search by Director')

src=int(input('Enter here: '))

if src==1:
    searchByMovieTitle()
elif src==2:
    searchByGenres()
elif src==3:
    searchByDirector()
else:
    print('Sorry, invalid')
