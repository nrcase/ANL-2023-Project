import json
import os
from pathlib import Path
import time

from utils.runners import run_tournament

RESULTS_DIR = Path("results", time.strftime('%Y%m%d-%H%M%S'))

# create results directory if it does not exist
if not RESULTS_DIR.exists():
    RESULTS_DIR.mkdir(parents=True)

# Settings to run a negotiation session:
#   You need to specify the classpath of 2 agents to start a negotiation. Parameters for the agent can be added as a dict (see example)
#   You need to specify the preference profiles for both agents. The first profile will be assigned to the first agent.
#   You need to specify a time deadline (is milliseconds (ms)) we are allowed to negotiate before we end without agreement.
tournament_settings = {
    "agents": [
        {
            "class": "agents.CSE3210.agent2.agent2.Agent2",
        },
        {
            "class": "agents.CSE3210.agent3.agent3.Agent3",
        },
        {
            "class": "agents.CSE3210.agent14.agent14.Agent14",
        },
        {
            "class": "agents.CSE3210.agent18.agent18.Agent18",
        },
        {
            "class": "agents.CSE3210.agent22.agent22.Agent22",
        },
        {
            "class": "agents.CSE3210.agent24.agent24.Agent24",
        },
        {
            "class": "agents.CSE3210.agent25.agent25.Agent25",
        },
        {
            "class": "agents.CSE3210.agent27.agent27.Agent27",
        },
        {
            "class": "agents.CSE3210.agent29.agent29.Agent29",
        },
        {
            "class": "agents.CSE3210.agent32.agent32.Agent32",
        },
        {
            "class": "agents.CSE3210.agent33.agent33.Agent33",
        },
        {
            "class": "agents.CSE3210.agent41.agent41.Agent41",
        },
        {
            "class": "agents.CSE3210.agent61.agent61.Agent61",
        },
        {
            "class": "agents.CSE3210.agent64.agent64.Agent64",
        },
        {
            "class": "agents.CSE3210.agent67.agent67.Agent67",
        },
        {
            "class": "agents.CSE3210.agent68.agent68.Agent68",
        },
        {
            "class": "agents.wolfpack_agent.wolfpack_agent.WolfpackAgent",
            "parameters": {"storage_dir": "agent_storage/WolfpackAgent"},
        },
        # {
        #     "class": "agents.lonewolf_agent.lonewolf_agent.LoneWolfAgent",
        #     "parameters": {"storage_dir": "agent_storage/LoneWolfAgent"},
        # },
    ],
    "profile_sets": [
        ["domains/domain26/profileA.json", "domains/domain26/profileB.json"],
        ["domains/domain43/profileA.json", "domains/domain43/profileB.json"],
    ],
    "deadline_time_ms": 10000,
}

# run a session and obtain results in dictionaries
tournament_steps, tournament_results, tournament_results_summary = run_tournament(tournament_settings)

# save the tournament settings for reference
with open(RESULTS_DIR.joinpath("tournament_steps.json"), "w", encoding="utf-8") as f:
    f.write(json.dumps(tournament_steps, indent=2))
# save the tournament results
with open(RESULTS_DIR.joinpath("tournament_results.json"), "w", encoding="utf-8") as f:
    f.write(json.dumps(tournament_results, indent=2))
# save the tournament results summary
tournament_results_summary.to_csv(RESULTS_DIR.joinpath("tournament_results_summary.csv"))
