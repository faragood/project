# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def imdb_score(movies, movie):
    for i in movies:
        if i["name"] == movie:
            if i["imdb"] > 5.5:
                return True
            else:
                return False

movie = str(input("Write film: "))
print(imdb_score(movies, movie))


#2
def imdb_score_list(movies):
    films = []
    for i in movies:
        if i["imdb"] > 5.5:
            films.append(i["name"])
    print(films)
    
imdb_score_list(movies)

#3
def categories(movies, category):
    films = []
    for i in movies:
        if i["category"] == category:
            films.append(i["name"])
    print(films)
    
movie = str(input("Write film: "))
categories(movies, movie)


#4
def aver(movies, movies_list):
    score = float(0)
    for i in movies_list:
        for j in movies:
            if i == j["name"]:
                score+=float(j["imdb"])
    return score/len(movies_list)
    
    
movies_stri = str(input("Write a list of movies separated by commas: "))
movies_list = list(movies_stri.split(","))
for i in range(len(movies_list)):
    movies_list[i] = movies_list[i].strip()
print(aver(movies, movies_list))
    

#5

def aver(movies, category):
    score = float(0)
    num = int(0)
    for i in movies:
        if category == i["category"]:
            score+=float(i["imdb"])
            num+=1
    return score/num
category = str(input("Write a category: "))
print(aver(movies, category))
