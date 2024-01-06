# 455/555 R3 README
Follow the instructions in this README to recreate the data found inside of Wheelin’ and Dealin’: Automated Negotiation Agents.

## Overview
- directories:
    - `agents`: Contains all agents that can be used for tournaments. This includes our group's agents, `wolfpack_agent` and `lonewolf_agent`.
    - `project-results`: Contains the results from the 15 tournaments ran as part of our research.
- files:
    - `run_control_tournament.py`: Runs a tournament using the subset of 16 CSE3210 agents randomly selected for our research. 
    - `run_wolfpack_tournament.py`: Runs a tournament using the subset of 16 CSE3210 agents randomly selected for our research plus our team's social utility-seeking `wolfpack_agent`.  
    - `run_lonewolf_tournament.py`: Runs a tournament using the subset of 16 CSE3210 agents randomly selected for our research plus our team's personal utility-seeking `lonewolf_agent`. 
    - `/project-results/digest_data.py`: Collects all the data found inside `/project-results` and finds several averages for each tournament type, outputting this in `summary.xlsx`.

## Installation
Download or clone this repository. Inside the repository, create a virtual environment for Python 3.9. It is important that Python 3.9 is used as straying from this as other versions of Python 3 will result in potential bugs or failures.

Activate your Python virtual environment and install the requirements in `requirements.txt` using `pip install -r requirements.txt`.

Instructions on creating a virtual environment and installing via pip inside said environment can be found [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).

## Generating Data
Our report is based on the results from 15 total tournaments (5 tournaments per type of tournament). All of our results are found in the `/project-results` directory. To find the average utility and social welfare for each tournament type, run `/project-results/digest_data.py` to create a `summary.xlsx` file with the averages of all results for each tournament type.

To recreate this data with new tournament runs, you must run the `run_*_tournament` for each of the tournament types (`control`, `wolfpack`, and `lonewolf`) 5 times a piece. Note that each tournament takes about 80 minutes a piece, so creating this data will take about 20 hours total. Given these results, extract the `tournament_results_summary.csv` file from `/results/*` folders and use them to update the `/project-results/<type>/run*.csv` files. Run `/project-results/digest_data.py` with the new `/project-results` data to create a `summary.xlsx` file with the cumulative average of all results for each tournament type, as described above.

## Final Report
https://github.com/nrcase/SCDAI-Term-Project/blob/main/docs/Project%20R3.pdf

## Data gathered and summarized in our final report
https://github.com/nrcase/SCDAI-Term-Project/blob/main/docs/summary-data-averages.xlsx

## Final Presentation 
https://github.com/nrcase/SCDAI-Term-Project/blob/main/docs/Wheelin%20and%20Dealin%20Presentation.pdf

## Grad Section Term Paper (nrcase)
https://github.com/nrcase/SCDAI-Term-Project/blob/main/docs/CSC555%20Term%20Paper.pdf
