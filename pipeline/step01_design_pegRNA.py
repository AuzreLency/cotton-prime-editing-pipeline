import pandas as pd

targets = ["GhALS1", "GhEPSPS", "GhPDS"]

results = []

for gene in targets:
    results.append({
        "target": gene,
        "PBS_length": 13,
        "RTT_length": 16
    })

df = pd.DataFrame(results)

df.to_csv("results/tables/pegRNA_design.csv", index=False)

print("pegRNA design completed.")
