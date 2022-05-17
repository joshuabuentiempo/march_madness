# march_madness

This project involves predicting a March Madness Bracket.


Overview
- Create a webscraper using python to pull team statitstics for each particpating team in the March Madness basketball tournament and game results for each game played
- Store relevant data into MySQL Database:
    "teams" table to store team data -> TeamID, year, team, teamstats ....
    "games" table to store game data -> GameID, year, teamA, teamB, scoreA, scoreB, winner
- Create a logistic regression model by analyzing the difference in season statistics for each variable
- Utilize the data from 2012-2019 to train model
- Test the model using 2021 and 2022 bracket
