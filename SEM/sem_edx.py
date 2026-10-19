import numpy as np
from ax.service.ax_client import AxClient, ObjectiveProperties
from ax.modelbridge.factory import Models
from ax.modelbridge.generation_strategy import GenerationStep, GenerationStrategy
from botorch.acquisition.multi_objective import qLogNoisyExpectedHypervolumeImprovement
import pandas as pd
import os
from datetime import datetime
from ax.modelbridge.factory import get_sobol
from ax.core.parameter import ParameterType, RangeParameter, ChoiceParameter
from ax.core.search_space import SearchSpace
from ax.modelbridge.factory import get_sobol


TRUE_PCT_ALSIMG = np.array([80, 10, 10])

def run_experiments(prev_data: pd.DataFrame=None):
    # define these names as variables for reuse (e.g., branin function return)
    obj1_name = "acq_time"
    obj2_name = "comp_error"
    gs = GenerationStrategy(steps=[
            # GenerationStep(
            #     model=Models.SOBOL,
            #     num_trials=6,
            #     max_parallelism=1
            # ), 
            GenerationStep(
                model=Models.BOTORCH_MODULAR,
                num_trials=-1,  # No limitation on how many trials should be produced from this step
                max_parallelism=3,  # Parallelism limit for this step, often lower than for Sobol
                model_kwargs={"botorch_acqf_class": qLogNoisyExpectedHypervolumeImprovement}
            ),
        ])
    ax_client = AxClient(generation_strategy=gs, verbose_logging=False, random_seed=42)

    # Define your search space and objectives
    ax_client.create_experiment(
        parameters=[
            {"name": "voltage", "type": "choice", "is_ordered": True, "value_type":"float", "sort_values":True, "values": [5.00, 10.00, 15.00, 20.00, 25.00]},
            {"name": "current", "type": "choice", "is_ordered": True, "value_type":"float", "sort_values":True, "values": [.1, .2, .4, .8, 1.6, 3.2, 6.4, 13.0, 26.0, 51.0, 100.0, 200.0, 410.0]},
            {
                "name": "x_counts",
                "type": "range",
                "value_type":"int",
                "bounds": [1000000, 16000000],
            },
        ],
        objectives={
            obj1_name: ObjectiveProperties(minimize=True),
            obj2_name: ObjectiveProperties(minimize=True),
        },
    )

    # 1. Define your parameter search space
    search_space = SearchSpace(
        parameters=[
            ChoiceParameter(name="current", parameter_type=ParameterType.FLOAT, is_ordered=True, sort_values=True,  values=[.1, .2, .4, .8, 1.6, 3.2, 6.4, 13.0, 26.0, 51.0, 100.0, 200.0, 410.0]),
            ChoiceParameter(name="voltage", parameter_type=ParameterType.FLOAT, is_ordered=True, sort_values=True, values=[5.00, 10.00, 15.00, 20.00, 25.00]),
            RangeParameter(name="x_counts", parameter_type=ParameterType.INT, lower=1000000, upper=16000000)
        ]
    )

    for exp in prev_data.iterrows():
        exp = exp[1]
        print("here")
        parameters = {pair[0]:pair[1] for pair in zip(["voltage", "current", "x_counts"], exp[["voltage", "current", "x_counts"]])}
        _, trial_index = ax_client.attach_trial(parameters=parameters)

        # 2. Complete the trial with your evaluated raw data
        ax_client.complete_trial(
            trial_index=trial_index,
            raw_data={
                obj1_name:(exp[obj1_name], None), obj2_name:(exp[obj2_name], None)
            },
        )

    # optimization loop
    while True:

        # get_next_trial performs model fitting and acquisition function evaluation
        parameterizations, optimization_complete = ax_client.get_next_trials(max_trials=3)
        
        for trial_index, parameterization in list(parameterizations.items()):
            # extract parameters
            x1 = parameterization["voltage"]
            x2 = parameterization["current"]
            x3 = parameterization["x_counts"]
            print(f"Parameters to test for Trial {trial_index}:\nVoltage -> {x1} kV\nCurrent -> {x2} nA\nNum X-Rays to collect -> {x3}")
            while True:
                ans = input("Did you get the parameters? (Y/N): ").strip().lower()
                if ans == "y":
                    break
                elif ans == "n":
                    print_parameters(parameterization)
                    break

            live_time, dead_time_pct, total_time = x_to_live_time(x3)
            
            # evaluate the dummy objective function
            print("Now run the experiment under these conditions")
            pct_Al = float(input(f"What was the recorded percent of Al: "))
            pct_Si = float(input(f"What was the recorded percent of Silicon: "))
            pct_Mg = float(input(f"What was the recorded percent of Magnesium: "))

            comp_err = np.sum((np.array([pct_Al, pct_Si, pct_Mg]) - TRUE_PCT_ALSIMG)**2)

            # report the results back to the algorithm
            ax_client.complete_trial(trial_index=trial_index, raw_data={"comp_error": comp_err, "acq_time": total_time})
            now = datetime.now()

            formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
            prev_data = pd.concat( (prev_data, pd.DataFrame([[x1, x2, x3, comp_err, total_time, formatted_time, pct_Al, pct_Si, pct_Mg, live_time, dead_time_pct]], columns=["voltage", "current", "x_counts", "comp_error", "acq_time", "datetime", "pct_Al", "pct_Si", "pct_Mg", "live_time", "pct_dead_time"])), ignore_index=True, axis=0)
            prev_data.to_csv("SEM_ALSI10MG_OPTIM_data.csv")
    pareto_results = ax_client.get_pareto_optimal_parameters()

def x_to_live_time(x_counts):
    while True:
        X_rate = float(input("What is the X ray count rate: "))
        live_time = x_counts / X_rate
        dead_time_pct = float(input("What is the dead time (will be percentage): "))
        total_time = live_time + dead_time_pct / 100 *live_time
        print(f"This is the Live Time for EDAX: {live_time}")
        ans = input("Did you get the Live Time? (Type Y/y to move on): ")
        if ans.strip().lower() == "y":
            break
    return live_time, dead_time_pct, total_time

def print_parameters(parameters):
    while True:
        print("Parameters to Test:\n")
        for name, param in parameters.items():
            print(f"{name} -> {param}\n")
        ans = input("Did you get the parameters? (Type Y/y to move on): ")
        if ans.strip().lower() == "y":
            break


search_root = "./"
target_file = "SEM_ALSI10MG_OPTIM_data.csv"
full_path = None

for root, dirs, files in os.walk(search_root):
    if target_file in files:
        full_path = os.path.join(root, target_file)
if full_path == None:
    data = pd.DataFrame([[5.0, 1.6, 1000003, 5.65, 30.5, "dfsdf", 81, 10, 9, 210, 22]], columns=["voltage", "current", "x_counts", "comp_error", "acq_time", "datetime", "pct_Al", "pct_Si", "pct_Mg", "live_time", "pct_dead_time"])
else:
    data = pd.read_csv(full_path)

run_experiments(data)


    # # 2. Initialize the Sobol model bridge
    # # Optional arguments: seed (int) for reproducibility, scramble (bool) to toggle scrambling
    # sobol_model = get_sobol(search_space=search_space, seed=42)

    # # 3. Generate a GeneratorRun containing n samples
    # generator_run = sobol_model.gen(n=6)

    # # 4. Extract parameters into a clean Python list of dicts or a NumPy array
    # samples = np.array([np.array(list(arm.parameters.values())) for arm in generator_run.arms])
    # print(samples)
    # sobol = pd.DataFrame(samples, columns=["current", "voltage", "x_counts"])
    # sobol.to_csv("init_sobol_samples.csv")
    # Preview the results
    # for i, sample in enumerate(samples[:3]):
    #     print(f"Sample {i}: {sample}")