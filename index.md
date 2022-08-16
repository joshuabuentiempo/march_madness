

# March Madness Bracket Predictor

The goal of this project was to be able to predict the winner of each game in the March Madness tournament.

## Webscraping

Used the Python web-scraping library BeautifulSoup4 to scrape data from https://www.sports-reference.com/cbb/.

Game data was pulled from each bracket starting in 2012 all the way to 2022.
ex. https://www.sports-reference.com/cbb/postseason/2018-ncaa.html

Each participating team had their season statistics pulled.
ex. https://www.sports-reference.com/cbb/schools/villanova/2018.html


## MySQL database

The scraped data was then stored into 2 different tables

"Games" table stored all of the game data (team a, team b, score of team a, score of team b, winner)
[Link](url) and ![Image](src)

"Teams" table stored all statistics for each participating team (fg, fga, ......, pts)
[Link](url) and ![Image](src)



## Analysis

Each game was analyzed be taking the difference of a statistic from team A and team B. (For this experiment, team A is always the team listed on
top). For example, let's say team A averaged 28 field goals made per game (fg) while team B only averaged 25 fg, then the difference would be 3.
(with team A as the reference)

  team A stat - team B stat = stat difference (with respect to the given game)


This difference was calculated for every game played and was tested for every team statistic.

### Binary Logistic Regression

To implement a binary logistic regression model,

**Data Visualizations**
Utilized Matplotlib package to graph the data for each variable

ex. PTS difference graph
[Link](url) and ![Image](src)

ex. stl difference graph
[Link](url) and ![Image](src)


### Linear Discriminant Analysis

**Data Visualizations**



## Results


