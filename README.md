### Skill Pilot
==============================

A end to end data science project that helps you decide your next step on your software enginerring industry

## Project Description

### Motivations 

In today's fast-paced software industry, numerous languages, technologies, platforms, and frameworks emerge and evolve rapidly, while others become obsolete. For individuals taking their first steps in this dynamic environment, deciding what to learn next can be a daunting challenge. Recognizing this struggle, the motivation behind Skill Pilot is to provide a solution that simplifies and guides newcomers through their learning journey.

### Skill Pilot: Your Learning Companion

End2End-Projct introduces Skill Pilot, a feature designed to alleviate the confusion and uncertainty associated with choosing the next steps in your learning path. Skill Pilot acts as your personalized learning companion, offering recommendations based on your current skill set, industry trends, and personal preferences. Whether you are a beginner or an experienced developer looking to diversify your skill set, Skill Pilot aims to make your learning experience smoother and more tailored to your goals.


--------
## Project sturcure
for the aim of the organizing the project i used the cookiecutter data science project template
https://github.com/drivendata/cookiecutter-data-science


## Installation
1) you need python 3
2) you need jupyter notebook installed
3) spyder or any other ide
4) just clone the projct and run the notebooks on the notebooks folder one by one
5) you will need to download the data from Stackoverflow and place it on the raw data folder
6) finally you are ready to run the dash script

## Data
i used the stackoverflow yearly survey dataset (2023)

## Data Preprocessing & Cleaning
- Splitting multible answers on a single columns
- fix the data type of columns such as years and age
- drop the unwanted roles such as Student, Designer, ...
- balancing class difereneced using upsampling and downsampling

## Exploratory Data Analysis (EDA)
- using treemap to show skill frequency of different categories (language, database, webframe, .. etc)
- Creating rolve vs skill heatmap and normaizled it
- using dendrogram for hierarchical clusetring to see relations between different role classes
- finally checking for skills specificty to different roles

## Feature Engineering
- apply tsne to visualize the high diemsnion data (+250 features)
- cluestring using silhouetter
- create new features based on these clusters
 Result, went from 250+ features to 25 features, and the accuracy of the base model increased

##. Modeling
- started by using a basseline model avery simple logistic regression model
- moved on to randomforest classifier using Pca
- and finally fine tune the reandomforest model using gridsearch
Note : all the models were saved with it's coressponding parameters and metrics using mlflow


## Prediction and Dash Scripts
- made a script that takes on skills and target role and then apply all the apply all the preprocssing and predict and reurn the recommendations
- deploying the model using Dash from plotly
- 
## Discussion
main chanllenges were that the data wanted alot of preprocessing to make it in a good format

13. Tools and Technologies
used mlflow for tracking algorithms, plotly and matplotlib for visualizng , pandas and numpy for handling the data and dash for the model deployement
14. Skills Demonstrated
data manipulation and preprocessing
data clearinng
good visualizations
model deployement

16. Acknowledgments
Stack overflow for the data set
plotly for the dash

18. Contact Information
gad43617@gmail.com







<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
