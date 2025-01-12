# Predicting SpaceX Falcon 9 Landing Success

## Project Overview
The goal of this project is to predict whether the Falcon 9 first stage will land successfully. SpaceX advertises Falcon 9 rocket launches on its website at a cost significantly lower than other providers. Much of this cost efficiency is due to SpaceX's ability to reuse the first stage of the rocket.

By predicting the likelihood of a successful first-stage landing, the cost of a launch by SpaceX can be estimated. This information could be valuable for alternative companies looking to bid competitively against SpaceX for rocket launches.

---

## Project Structure
1. **Data Collection and Cleaning**  
   - Collect data via the SpaceX API, filter it, and handle missing values.  
   - Additional data is sourced from a SpaceX related web page using web scraping.  

2. **Data Processing**  
   - Create a binary column from a categorical one to be used as the target variable for model building.  

3. **Exploratory Data Analysis (EDA)**  
   - Analyse the dataset to extract key insights by querying the database using MySQL.  
   - Visualise data through various plots to understand patterns and trends.  

4. **Feature Engineering**  
   - Refine the dataset by retaining only the necessary features.  
   - Perform one-hot encoding on categorical columns and convert the data frame to a float format for compatibility with machine learning models.  

5. **Geospatial Analysis**  
   - Map SpaceX launch site locations interactively using the Folium library.  

6. **Interactive Dashboard**  
   - Build an interactive dashboard to visualise SpaceX data using Plotly Dash.  

7. **Machine Learning Model Building and Evaluation**  
   - Develop logistic regression, SVM, decision tree, and KNN models.  
   - Evaluate and compare their performance to determine the most effective model.
  

---

## Results

A high-level summary of the project's key findings:

- The overall **landing success rate** has shown a consistent increase between 2010 and 2020, reflecting advancements in technology and operational efficiency.  
- Variables such as **launch site**, **flight number**, **payload mass**, and **orbit** have all been found to influence the **landing success rate** to varying degrees.  
- The **KSC LC-39A launch site** recorded the highest success rate among all launch sites.  
- Among the models built, the **SVM model** achieved the highest accuracy in predicting SpaceX landing outcomes, correctly identifying:
  - **100%** of unsuccessful landings.  
  - **86%** of successful landings.

---

## Credit
This project is based on the capstone project from the [IBM Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science) course. Building on the original version, I restructured the project, refactored the code, added new features and documentation, and conducted an analysis of the results at each phase.
