# Surgery Simulation Workshop 3 

A straightforward simulation of a hospital surgery unit where patients go through:  
**Waiting → Preparation → Surgery → Recovery**

There is **only 1 operating room** and **no waiting space** between surgery and recovery.  
If all recovery beds are full when a surgery ends, the operating room gets **blocked** until a bed becomes free.

## Completed Tasks based on Project requirement
- 3 configurations tested: **3p4r**, **3p5r**, **4p5r**
- Exponential times: arrival (25), prep (40), surgery (20), recovery (40)
- 20 independent runs per configuration
- 1000 time units warm-up + 1000 time units observation
- Same random seeds across configurations (for fair comparison)
- Measured: queue before prep, blocking probability, and "all recovery busy"

## Project Structure

workshop_3_imulation/
│
├── surgery_simulation.py      # Core simulation logic (clean & original)
├── run_analysis.py       # Runs 20 replications for all configurations
├── analyze_results.py    # Complete statistical analysis + answers
├── results/              # Auto-generated folder with CSV results
│   ├── 3p4r.csv
│   ├── 3p5r.csv
│   └── 4p5r.csv
└── README.md             # This file – you're reading it!


---

### Configurations Tested

| Name   | Prep Rooms | Recovery Rooms | Goal                          |
|--------|------------|----------------|----------------|-------------------------------|
| 3p4r  | 3          | 4              | Baseline (higher blocking)     |
| 3p5r  | 3          | 5              | +1 recovery room              |
| 4p5r  | 4          | 5              | +1 preparation room            |

All service times ~ Exponential:  
Arrival = 25 | Prep = 40 | Surgery = 20 | Recovery = 40

---


## How to Run (Takes ~2–3 minutes)

```bash
# Install required packages (once)
pip install simpy pandas numpy scipy

# Run all simulations
python run_analysis.py

# See full results with confidence intervals
python analyze_results.py
```

