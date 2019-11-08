# Razors-Edge

### Project Description
_This repository is creating a predictive sports betting model to find high value betting opportunities and increase the chances of winning bets. The goal of this program is to obtain a model that will pick a variety of games to bet on for each day and have a success rate of 80%. Although, previous research papers on sports betting algorithms have predicted a max ceiling of 75%, I believe using a new approach combining both supervised and unsupervised learning that this theoretical "ceiling" can be beat. The advantage of the algorithms I've created using a supervised learning approach with regression is that they take in no team bias and have found a trend only within the betting lines themselves to determine what kinds of lines most often produce a certain result. This has yielded me a good amount of success that came out with around a 65% accuracy on my testing data from previous years. The downside of this, is that certain matchups will not fit this mold based on the nature of the teams playing. That is where supervised learning comes in. Using a clustering algorithm I can create a model of different types of matchups based on advanced metrics and team efficiency data. This allows me to train different algorithms for each matchup type cluster using a classification algorithm to predict which team will win and the likely margin of victory in a 3 point range. Based on this principle, I will create a program to implement these algorithms and select the lines with the highest predicted cover margin._
     
### TO DO

  1. Load in advanced statistics from the years 2016-2020 for the NFL, NCAAF, NBA, NCAAM, & MLB
      
  2. Load in betting lines and results for every game from 2016-2019 for the NFL, NCAAF, NBA, NCAAM, & MLB
      
  3. Split the betting datasets into Train/Test datasets
