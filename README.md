# Surgery Simulation Project

A straightforward simulation of a hospital surgery unit where patients go through:  
**Waiting → Preparation → Surgery → Recovery**

There is **only 1 operating room** and **no waiting space** between surgery and recovery.  
If all recovery beds are full when a surgery ends, the operating room gets **blocked** until a bed becomes free.

## Completed tasks (project requirements)

- 3 configurations tested: **3p4r**, **3p5r**, **4p5r**
- Exponential times: arrival (25), prep (40), surgery (20), recovery (40)
- 20 independent runs per configuration
- 1000 time units warm-up + 1000 time units observation
- Same random seeds across configurations (for fair comparison)
- Measured: queue before prep, blocking probability, and "all recovery busy"

## Project structure

```
workshop_3_simulation/
│
├── surgery_simulation.py      # Core simulation logic (clean & original)
├── run_analysis.py            # Runs 20 replications for all configurations
├── analyze_results.py         # Complete statistical analysis + answers
├── results/                   # Auto-generated folder with CSV results
│   ├── 3p4r.csv
│   ├── 3p5r.csv
│   └── 4p5r.csv
└── README.md                  # This file – you're reading it!
```

### Configurations tested

| Name  | Prep Rooms | Recovery Rooms | Goal                            |
|-------|------------|----------------|----------------------------------|
| 3p4r  | 3          | 4              | Baseline (higher blocking)       |
| 3p5r  | 3          | 5              | +1 recovery room                 |
| 4p5r  | 4          | 5              | +1 preparation room              |

All service times ~ Exponential:  
Arrival = 25 | Prep = 40 | Surgery = 20 | Recovery = 40

---

## How to run

```bash
# Install required packages (once)
pip install simpy pandas numpy scipy

# Run all simulations
python run_analysis.py

# See full results with confidence intervals
python analyze_results.py
```

## Quick results summary (point estimates)

| Configuration | Avg Queue Length | Blocking Probability | Notes           |
|---------------:|------------------:|---------------------:|-----------------|
| 3p4r           |             ~0.31 |                ~4.0% | High blocking   |
| 3p5r           |             ~0.31 |                ~0.9% | Much better!    |
| 4p5r           |             ~0.05 |                ~0.8% | Shortest queue  |

## Answers to the questions

- Point estimates & 95% confidence intervals → shown clearly in analyze_results.py  
- Significant differences? → Yes. Both adding a recovery bed and adding a prep room make a statistically significant improvement.  
- Paired comparison (same seeds) → Makes differences even clearer and more significant.  
- "All recovery beds busy" vs actual blocking → Easier and more reliable to measure (smaller confidence interval), especially when blocking is rare.
