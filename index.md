

# March Madness Bracket Predictor

The goal of this project was to predict the winner of each game in future March Madness tournaments. This was achieved by analyzing data on previous tournaments and the respective teams that participated in each, and then creating multiple classification models to determine which team would win. The 2 models that were tested are binary logistic regression and linear discriminant analysis.

## Web scraping

The Python web scraping library BeautifulSoup4 was used to scrape data from the following website.
https://www.sports-reference.com/cbb/

Game data from each bracket was pulled starting in 2012 all the way to 2022.
ex. https://www.sports-reference.com/cbb/postseason/2018-ncaa.html

![bracket_sample](https://user-images.githubusercontent.com/48895748/184991835-4c35946e-f768-436a-a530-9a0c663341c8.png)



Each participating team had their season statistics pulled.
ex. https://www.sports-reference.com/cbb/schools/villanova/2018.html

![team_stats_sample](https://user-images.githubusercontent.com/48895748/184991912-0e7a89b6-6f04-4a37-b75a-e1a9765d04d6.png)




## MySQL database

The scraped data was then stored into 2 different tables


"Games" table stored all of the game data (team a, team b, score of team a, score of team b, winner)
![games_table](https://user-images.githubusercontent.com/48895748/184992000-f2c7255e-00a5-4291-87dd-c6bf7c8230b6.png)



"Teams" table stored all statistics for each participating team (fg, fga, fg%, ......, pts)
![teams_table](https://user-images.githubusercontent.com/48895748/184992017-50651b12-1b9e-4a83-bd21-c5b4d7ac1ad3.png)



## Analysis

Each game was analyzed be taking the difference of a statistic from team A and team B. (For this experiment, team A is always the team listed on top). For example, let's say team A averaged 28 field goals made per game (fg) while team B only averaged 25 fg, then the difference would be 3.
(with team A as the reference)

  team A stat - team B stat = stat difference (with respect to the given game)


This difference was calculated for every game played and was tested for every team statistic.

### Binary Logistic Regression

To implement a binary logistic regression model,

Utilized Matplotlib package to graph the data for each variable

ex. PTS difference graph
![Image](src)

ex. stl difference graph
![Image](src)


### Linear Discriminant Analysis

**Data Visualizations**



## Results


