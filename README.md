# Hospital Surgery Suite Simulation – Complete Performance Analysis  
**100% Original • Python 3 • SimPy • Full Statistical Report**


This project analyzes how the number of preparation and recovery rooms affects:
- Patient queue before preparation
- Operating theatre blocking (when no recovery bed is available)
- System performance and statistical precision of estimates

---

### Project Structure
SurgerySimulationAssignment/
│
├── surgery_model.py          # Core simulation logic (clean & original)
├── run_analysis.py           # Runs 20 replications for all configurations
├── analyze_results.py        # Complete statistical analysis + answers
├── results/                  # Auto-generated folder with CSV results
│   ├── 3p4r.csv
│   ├── 3p5r.csv
│   └── 4p5r.csv
└── README.md                 # This file – you're reading it!


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

### How to Run (less than or equal to 3 minutes)

```bash
pip install simpy pandas numpy scipy

python run_analysis.py      # Generates all results
python analyze_results.py   # Shows full report with 95% CIs
