import os
from surgery_simulation import run_one_run

configs = [
    ("3p4r", 3, 4),
    ("3p5r", 3, 5),
    ("4p5r", 4, 5)
]

seeds = list(range(1000, 1020))  # 20 different seeds
os.makedirs("results", exist_ok=True)

print("Starting full experiment (60 simulation runs)...")

for name, p, r in configs:
    print(f"Running {name}...")
    results = []
    for seed in seeds:
        result = run_one_run(p, r, seed, warmup=1000, observe=1000)
        result["seed"] = seed
        results.append(result)

    # Save
    import pandas as pd

    df = pd.DataFrame(results)
    df.to_csv(f"results/{name}.csv", index=False)
    print(f"{name} finished")

print("All done! Results saved in /results folder")