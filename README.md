# Causal-inference-in-DotA-2-when-estimated-through-randomized-data
TUDELFT-CSE-research-project
This project is part of the [Research Project](https://github.com/TU-Delft-CSE/Research-Project) provided by [TU DELFT](https://github.com/TU-Delft-CSE) in the year of 2022. 
The project includes 4 scripts which complement each other. 
<ol>
  <li>Opendota.py</li>
  Gathers the data and saves it to file match.csv
  <li>Main.py</li>
  Takes match.csv and calculates the Average causal effect, variances and the uncertainty
  <li>IndepedenceTest.py</li>
  Runs the Chi-square tests on the infromation produced by Main.py and 
  <li>Plotgeneration.py</li>
  Creates the plots and writes the causal effects for each hero side by side to file.
  
</ol>
Libraries used: Python 3.9, Scipy, Numpy, Pandas, Matplotlib
