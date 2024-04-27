# Dev-Salary-Prediction
This is a ML Web App that provides a user interface for HR to predict the salary of potential developers to join a company.

## 1) The Problem
We were given the challenge of building a Web App for a HR team to estimate the yearly salary of professionals that work in the development area. The users need to interact with the Web App to inform the professional's informations so, in the end, the estimated salary is informed. This tool is necessary for the HR professionals because, lately, they have been having difficulties in estimating developers' salaries given that nowadays more and more variables influence the salary of these professionals. 

## 2) The Data
The data received came in a csv file containing the salaries and various informations regarding developers all over the world. In the EDA study these variables are explained and shown in more details.

## 3) The Tools Used
The ML Web App was developed using Flask, with the front-end being built using HTML and CSS. All the modeling was done through Python (scikit-learn).

## 4) The ML Web App

Below, the homepage the user sees when opening the Web App:

![image](https://github.com/T1burski/Dev-Salary-Prediction/assets/100734219/639087ec-eb54-4896-ac47-8419046a10c1)

As we can see, the user can select the values of the 4 variables chosen (the EDA notebook explains their choice). When the user selects them and clicks the button "Predict Salary", the result is shown.

## 5) Running the ML Web App
In order for you to run the App, follow the steps below. The Python version used was 3.9.13.

### 1) Clone this repository to a folder in your computer using:
git clone https://github.com/T1burski/Dev-Salary-Prediction.git

### 2) Open a Terminal within the folder previously selected and create an virtual environment:
python -m venv class_transactions

### 3) In the Terminal, activate the virtual environment:
class_transactions\Scripts\activate

### 4) In the Terminal, install the dependencies of the project:
pip install -r requirements.txt

### 5) Finally, run the Web App using Waitress:
waitress-serve --listen=127.0.0.1:5000 app:app

After the last step, a http path will be show in the Terminal which can be opened in your browser for you to try out the ML Web App! After using the Web App, press Ctrl+C in the Terminal.
