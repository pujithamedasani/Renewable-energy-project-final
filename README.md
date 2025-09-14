# Renewable-energy-project-final
# EduNet Green Skills & AI (Sustainable Agriculture) - Renewable Energy Project

This project is part of the EduNet Green Skills & AI initiative.  
It uses renewable energy datasets from Kaggle to analyze, clean, and generate insights about global renewable energy adoption.

##  Repository Structure
``` bash
edunet-green-skills-ai/
│ renewable_energy.csv    # cleaned dataset (sample included)
│ renewable_energy.ipynb  # Jupyter notebook
│ app.py                  # Python script version
| predicted_report.csv    # predicted report by app developed in streamlit
| energy_model            # ML model
| scalar.pkl
| outputs                 # This folder conatins output screenshots 
│ README.md
```

##  How to Use
1. Clone this repository:
   ``` bash
   git clone https://github.com/<yourusername>/Renewable-energy-project-final.git
   cd Renewable-energy-project-final
   ```

2. Set up Kaggle API:
   - Create a Kaggle account and download `kaggle.json` from [Kaggle Account Settings](https://www.kaggle.com/account).
   - Place it in:  
     - Linux/Mac: `~/.kaggle/kaggle.json`  
     - Windows: `C:\Users\<username>\.kaggle\kaggle.json`

3. Download dataset:
   ``` bash
   kaggle datasets
   I used sample dataset 
   ```

4. Run the notebook or script:
   ``` bash
   jupyter notebook notebooks/renewable_energy.ipynb
   or
   python app.py
   ```

5. The dataset will be saved to:
   ``` bash
   data/renewable_energy.csv
   ```
6. The predicted results will be saved in:
   ``` bash
   predicted_report.csv
   ```
   
## Features
- Loads renewable energy dataset from Kaggle
- Cleans and processes missing values & units
- Calculates renewable share of total energy
- Estimates yearly growth trends
- Saves cleaned dataset for analysis

##  Requirements
- Python 3.8+ , Jupyter Notebook , Streamlit 
- pandas, numpy, matplotlib, seaborn, scikit-learn , tensorflow

Install with:
``` bash
pip install -r requirements.txt
```
## Credits

- Dataset: Kaggle - Renewable Energy and modified into my sample csv file data set 
- Developed as part of EduNet Green Skills & AI project

