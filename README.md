# march_madness

This project involves predicting a March Madness Bracket.


Steps:
- Create a webscraper using python to pull team statitstics for each particpating team in the March Madness basketball tournament and game results (who won/lost) for each game       played (starting in 2010 to 2018)
- Store relevant data into MySQL Database:
    Master db for team data -> year, team, teamID, team_stats.....
    Master db for game data -> year, gameID, winner (teamID), loser (teamID)
- Create a logistic regression model by analyzing all games based off of only winning team and losing team
- Create secondary logistic regression model by analying winning team and losing team per round (first round all the way to championship therefore 6 rounds in total)
- Utilize the data from 2010-2018 to train model and test on 2019 and 2021
- Predict for 2022 
- ** Bonus ** Create webpage or GUI that can show completed bracket
