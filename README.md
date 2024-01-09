### Skill Pilot
============================== 


<img src="R.png" alt="Skill Pilot Banner" width="600" height="400">

An end-to-end data science project that assists individuals in making informed decisions about their next steps in the software engineering industry.


An end-to-end data science project that assists individuals in making informed decisions about their next steps in the software engineering industry.


## Project Description

### Motivation 
In the ever-evolving software industry, the rapid emergence and obsolescence of languages, technologies, platforms, and frameworks pose a challenge for individuals navigating their learning journey. Skill Pilot addresses this challenge by offering a personalized learning companion, guiding users through their learning path based on their current skill set, industry trends, and personal preferences. Whether you're a beginner or an experienced developer seeking to diversify your skill set, Skill Pilot aims to streamline your learning experience.

### Skill Pilot: Your Learning Companion
Skill Pilot is designed to simplify the decision-making process for learners, providing tailored recommendations. It acts as a personalized guide, considering your current skills, industry trends, and preferences to suggest the most suitable next steps in your learning path.



--------
## Project sturcure
- Notebooks folder : contains all the jupyter notebooks
- data folder contains 2 subfolders, one for the raw data and the other one for the proccessd data
- models : contains the mlflow outputs that keep track of each model
- reports contains the graph produced by plotly
- scripts : contains the scripts of the project

for the aim of the organizing the project i used the cookiecutter data science project template
[Cookiecutter Data Science Project Template](https://github.com/drivendata/cookiecutter-data-science)


## Installation
To run this project, you need:
    It's recommend to create ant activate a virtual environments before installing dependecies
1. Python 3
2. Jupyter Notebook installed
3. install differen packages on the requirements.txt
4. Clone the project 
5. Download the [Stackoverflow Yearly Suervey](https://survey.stackoverflow.co/) dataset (2023) and place it in the "raw data" folder
6. Run the notebooks in the "notebooks" folder sequentially
7. Finally run the Dash script
## Data
i used the stackoverflow yearly survey dataset (2023)
2 reasons for chosing it 
1. it's updated yearly so it's alwyas up to date
2. it's not focusing on a specific geopgrahical area, instead developers from all over the world participate in the suervey
[Stackoverflow Yearly Suervey](https://survey.stackoverflow.co/)

## Data Preprocessing & Cleaning
- Splitting multiple answers in a single column
- Correcting data types (e.g., years and age)
- Removing unwanted roles (e.g., Student, Designer)
- Balancing class differences using upsampling and downsampling
  
## Exploratory Data Analysis (EDA)
- Utilized treemaps to visualize skill frequency across different categories (language, database, web framework, etc.)
- Created role vs. skill heatmap and normalized it
- Employed dendrogram for hierarchical clustering to identify relationships between different role classes
- Examined skill specificity to different roles

## Feature Engineering
- Applied t-SNE to visualize high-dimensional data (250+ features)
- Conducted clustering using silhouette analysis
- Created new features based on these clusters, reducing the feature set from 250+ to 25 features and improving the base model accuracy

##. Modeling
- Developed a baseline model using a simple logistic regression
- Implemented a random forest classifier with PCA
- Fine-tuned the random forest model using grid search
- Saved models, parameters, and metrics using MLflow

## Prediction and Dash Scripts
- Created a script for preprocessing, predicting, and returning recommendations based on input skills and target roles
- Deployed the model using Dash from Plotly
  
## Discussion
Main challenges involved extensive data preprocessing to ensure data quality and format.


## Tools and Technologies
- MLflow for algorithm tracking
- Plotly and Matplotlib for visualization
- Pandas and NumPy for data handling
- Dash for model deployment
  
## Skills Demonstrated
- Data manipulation and preprocessing
- Data cleaning
- Effective visualizations
- Model deployment

## Acknowledgments
- Stack Overflow for providing the dataset
- Plotly for Dashh

## Contact Information
gad43617@gmail.com







<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
