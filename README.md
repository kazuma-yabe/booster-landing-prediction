# Predicting Falcon 9 Booster Landing Success

## Project Overview
The goal of this project is to predict whether the Falcon 9 rocket’s first stage (booster) will land successfully. Falcon 9 launches are offered at a significantly lower cost than other rockets, primarily due to the reusability of the booster.

By predicting the likelihood of a successful landing, the cost of a Falcon 9 launch can be estimated. This information could be valuable for companies looking to compete with Falcon 9 in the rocket launch market.

---

## Project Structure
1. **Data Collection and Cleaning**  
   - Retrieve launch data using the SpaceX API and supplement it with web-scraped data.
   - Handle missing values and filter relevant information. 

2. **Data Processing**  
   - Transform categorical data into a binary target variable for model building.

3. **Exploratory Data Analysis (EDA)**  
   - Analyse the dataset using SQL queries to extract key insights.
   - Use visualisations to identify patterns and trends in landing success rates. 

4. **Feature Engineering**  
   - Select and refine key features to enhance model performance.
   - Apply one-hot encoding to categorical variables and ensure compatibility with machine learning models by converting data to float format.

5. **Geospatial Analysis**  
   - Map and visualise rocket launch site locations interactively using Folium, highlighting success rates and spatial patterns affecting landing outcomes

6. **Interactive Dashboard**  
   - Develop a Plotly Dash dashboard with dynamic visualisations of launch and landing data.

7. **Machine Learning Model Building and Evaluation**  
   - Build and evaluate multiple models using scikit-learn, including Logistic Regression, SVM, Decision Tree, and KNN.
   - Optimise hyperparameters with GridSearchCV and compare model performance to determine the most effective approach.
  

---

## Results and Key Findings

- Landing success rates have increased consistently from 2010 to 2020, reflecting improvements in technology and operations.
- Several factors influence landing success, including launch site, booster version, payload mass, and orbit type.
- Among the tested models, the **SVM model** achieved the highest accuracy in predicting Falcon 9 booster landing outcomes, correctly identifying:
  - 100% of unsuccessful landings.  
  - 86% of successful landings.

---

## Attribution
This project is based on [IBM Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science)capstone project. Building on the original version, I restructured the project, refactored the code, added new features and documentation, and conducted a phase-by-phase analysis of the results.
