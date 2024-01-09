### Skill Pilot
============================== 

![Skill Pilot Banner](C:\Users\Mohamed Gad\OneDrive\Desktop\R.png)

An end-to-end data science project that assists individuals in making informed decisions about their next steps in the software engineering industry.


## Project Description

### Motivation 
In the ever-evolving software industry, the rapid emergence and obsolescence of languages, technologies, platforms, and frameworks pose a challenge for individuals navigating their learning journey. Skill Pilot addresses this challenge by offering a personalized learning companion, guiding users through their learning path based on their current skill set, industry trends, and personal preferences. Whether you're a beginner or an experienced developer seeking to diversify your skill set, Skill Pilot aims to streamline your learning experience.

### Skill Pilot: Your Learning Companion
Skill Pilot is designed to simplify the decision-making process for learners, providing tailored recommendations. It acts as a personalized guide, considering your current skills, industry trends, and preferences to suggest the most suitable next steps in your learning path.



--------
## Project sturcure
for the aim of the organizing the project i used the cookiecutter data science project template
[Cookiecutter Data Science Project Template](https://github.com/drivendata/cookiecutter-data-science)


## Installation
To run this project, you need:

1. Python 3
2. Jupyter Notebook installed
2. An integrated development environment (IDE) such as Spyder
2. Clone the project and run the notebooks in the "notebooks" folder sequentially
2. Download the Stack Overflow yearly survey dataset (2023) and place it in the "raw data" folder
2. Run the Dash script for the final application
3. 
## Data
i used the stackoverflow yearly survey dataset (2023)
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
