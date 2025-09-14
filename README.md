# Renewable-energy-project-final
# Week-1-project
# EduNet Green Skills & AI - Renewable Energy Project

This project is part of the EduNet Green Skills & AI initiative.  
It uses renewable energy datasets from Kaggle to analyze, clean, and generate insights about global renewable energy adoption.

## Repository Structure
edunet-green-skills-ai/
│ app.py # Main application script
│ energy_model.pkl # Trained ML model
│ predicted_report.csv # Predicted results
│ renewable_energy.csv # Original dataset
│ renewable_energy.ipynb # Jupyter notebook for analysis
│ scaler.pkl # Preprocessing scaler
│ README.md # Project documentation


## How to Use
1. Clone this repository:
   git clone https://github.com/pujithamedasani/Renewable-energy-project-final.git
   cd Renewable-energy-project-final
Set up Kaggle API (if you need to re-download the dataset):

Create a Kaggle account and download kaggle.json from Kaggle Account Settings.

Place it in:

Linux/Mac: ~/.kaggle/kaggle.json

Windows: C:\Users\<username>\.kaggle\kaggle.json

Run the notebook or app:

jupyter notebook renewable_energy.ipynb
# or run the app
python app.py
The predicted results will be saved in:

predicted_report.csv
Features
Loads renewable energy dataset

Cleans and processes missing values & units

Builds and saves ML model (energy_model.pkl)

Generates predictions and saves as CSV

Preprocessing with saved scaler (scaler.pkl)

## Requirements

Python 3.8+

pandas, numpy, matplotlib, seaborn, scikit-learn, Flask (if app.py uses it)

Install with:

pip install -r requirements.txt

## Credits

Dataset: Sample datatset 
Developed as part of EduNet Green Skills & AI project