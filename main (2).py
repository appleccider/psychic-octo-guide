import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Fullmetal Alchemist: The Sacred Star of Milos"

print("My favorite movie is " + favMovie)

print("\nThe data for my favorite movie is:")
favMovieBooleanList = movieData["movie_title"] == favMovie
favMovieData = movieData.loc[favMovieBooleanList]

print(favMovieData)
print("\n\n")

animationMovieBooleanList = movieData["genres"].str.contains("Animation")

animationMovieData = movieData.loc[animationMovieBooleanList]

numOfMovies = animationMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Animation in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Animation.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#find min
min = animationMovieData['audience_rating'].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 61 points higher than the lowest rated movie.")
print()

#find max
max = animationMovieData['audience_rating'].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 17 points lower than the highest rated movie.")
print()

#find mean
mean = animationMovieData['audience_rating'].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

#find median
median = animationMovieData['audience_rating'].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(animationMovieData["audience_rating"], range = (0, 100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Animation Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Animation Movies")

#Prints interpretation of histogram
print(
  "The histogram is heavily skewed towards one direction, meaning that the general mean/median score was rather high for all the movies in the Animation data set."
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = animationMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "As the critic ratings slowly increase,  so do the audience ratings. Based on this, it can be inferred that the general mean/median score was higher for movies in the Animation data set, as mentioned before. Both audience and critic ratings were skewed."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")