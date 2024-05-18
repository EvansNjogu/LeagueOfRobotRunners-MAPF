import MAPF
from typing import Dict, List, Tuple, Set
from queue import PriorityQueue
import numpy as np

from EECBSPlanner import EECBSPlanner

class pyMAPFPlanner:
    def __init__(self, pyenv=None) -> None:
        if pyenv is not None:
            self.env = pyenv.env
        self.planner = EECBSPlanner(self.env)
        self.solution_dict = {}
        print("pyMAPFPlanner using EECBS created! python debug")

    def initialize(self, preprocess_time_limit: int):
        pass
        print("planner initialize done... python debug")
        return True

    def plan(self, time_limit):
        if len(self.solution_dict) != 0 and max([len(path) for path in self.solution_dict.values()]) >= 2:
            actions = self.planner.compute_actions(self.solution_dict)
            for agent_id in self.solution_dict.keys():
                if len(self.solution_dict[agent_id]) >= 1:
                    self.solution_dict[agent_id].pop(0)
        else:
            actions, self.solution_dict = self.planner.plan(time_limit)

        return actions

if __name__ == "__main__":
    test_planner = pyMAPFPlanner()
    test_planner.initialize(100)
