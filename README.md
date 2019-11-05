# Razors-Edge

### Project Description
_This repository is creating a predictive sports betting model to find high value betting opportunities and increase the chances of winning bets. These algorithms are taking in multiple advanced team statistics for each sport from the last 4 years and training a model to see which features have the most impact on game outcomes based on the sport. Using this data the model will pick betting lines with the highest value from each day attempting to achieve 80 percent accuracy on its chosen bets. While most algorithms have previously determined a max successs at 75 percent, this program will try to increase this ceiling by selectively picking games for the highest chance of success and ignoring games with little confidence._
     
### TO DO

  1. Load in advanced statistics from the years 2016-2020 for the NFL, NCAAF, NBA, NCAAM, & MLB
      
  2. Load in betting lines and results for every game from 2016-2019 for the NFL, NCAAF, NBA, NCAAM, & MLB
      
  3. Split the betting datasets into Train/Test datasets
  
  4. Use a Naive Bayes Classifier to train a model based on the previous years data
  
  5. Use GridSearchCV to find the best hyperparameters for the model
  
  6. Predict outcomes for the test model and find the range of predicted outcomes that produce the highest success rate.
  
  7. Use the 2020 stats to predict the outcomes from daily matchups and record the success rates
