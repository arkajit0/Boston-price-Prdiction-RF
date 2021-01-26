# Boston-price-Prdiction-RF
Boston-price Prediction deployment URL: https://cryptic-reef-10908.herokuapp.com/

## Introduction

### In this project, we will develop and evaluate the performance and predictive power of a model trained and tested on data collected from houses located in Boston

#### Once we get a stabel model we will use it to predict the monetary value of house located in Boston

#### The datset used has in total 14 columns with historical datas collected from different areas in Boston that we will divide into 13 features and 1 target column

***The Columns are Given as:***
- CRIM: This is the per capita crime rate by town
- ZN: This is the proportion of residential land zoned for lots larger than 25,000 sq.ft.
- INDUS: This is the proportion of non-retail business acres per town.
- CHAS: This is the Charles River dummy variable (this is equal to 1 if tract bounds river; 0 otherwise)
- NOX: This is the nitric oxides concentration (parts per 10 million)
- RM: This is the average number of rooms per dwelling
- AGE: This is the proportion of owner-occupied units built prior to 1940
- DIS: This is the weighted distances to five Boston employment centers
- RAD: This is the index of accessibility to radial highways
- TAX: This is the full-value property-tax rate per  \$10,000
- PTRATIO: This is the pupil-teacher ratio by town
- B: This is calculated as 1000(Bk — 0.63)², where Bk is the proportion of people of African American descent by town
- LSTAT: This is the percentage lower status of the population
- MEDV: This is the median value of owner-occupied homes in $1000s

### Instruction to run the file
***Step 1***
**Create and activate an environment**
- Using Conda <br>
conda create -n [your environment name] python=3.7 <br>
Then activate the environment by writing <br>
conda activate [your environment name] <br>

- Using default Environments <br>
python3 -m venv [your environment name] <br>
Then activate the environment by writing <br>
[your environment name]\Scripts\activate.bat [For windows users] <br>
source [your environment name]/bin/activate [For Mac/Ubuntu users] <br>

NOTE: you can give any python version and ignore brackets while giving environment name

***Step 2***
**Install Dependencies**
- For library installations  write <br>
pip install -r requirements.txt 

***Step 3***
**Run The File**
- To run the file write <br>
python app.py
