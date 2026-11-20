    # # 1. Define your parameter search space
    # search_space = SearchSpace(
    #     parameters=[
    #         ChoiceParameter(name="current", parameter_type=ParameterType.FLOAT, is_ordered=True, sort_values=True,  values=[.1, .2, .4, .8, 1.6, 3.2, 6.4]),
    #         ChoiceParameter(name="voltage", parameter_type=ParameterType.FLOAT, is_ordered=True, sort_values=True, values=[5.00, 10.00, 15.00, 20.00, 25.00]),
    #         RangeParameter(name="x_counts", parameter_type=ParameterType.INT, lower=1000000, upper=16000000)
    #     ]
    # )

    #     # 2. Initialize the Sobol model bridge
    # # Optional arguments: seed (int) for reproducibility, scramble (bool) to toggle scrambling
    # sobol_model = get_sobol(search_space=search_space, seed=42)

    # # 3. Generate a GeneratorRun containing n samples
    # generator_run = sobol_model.gen(n=6)

    # # 4. Extract parameters into a clean Python list of dicts or a NumPy array
    # samples = np.array([np.array(list(arm.parameters.values())) for arm in generator_run.arms])
    # print(samples)
    # sobol = pd.DataFrame(samples, columns=["current", "voltage", "x_counts"])
    # sobol.to_csv("init_sobol_samples.csv")
    # # Preview the results
    # for i, sample in enumerate(samples[:3]):
    #     print(f"Sample {i}: {sample}")