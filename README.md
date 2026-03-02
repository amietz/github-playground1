# Medical Devices Data Science Project

A Python-based data science project for analysis, processing, and machine learning on medical device data.

## Project Structure

```
├── data/
│   ├── raw/          # Raw, immutable source data
│   └── processed/    # Cleaned and processed datasets
├── notebooks/        # Jupyter notebooks for exploration and analysis
├── src/
│   └── meddevice/    # Python package with reusable modules
│       ├── data/     # Data ingestion and preprocessing
│       ├── features/ # Feature engineering
│       ├── models/   # Machine learning models
│       └── visualization/ # Plotting and reporting utilities
├── tests/            # Unit and integration tests
├── requirements.txt  # Python dependencies
└── setup.cfg         # Package configuration
```

## Getting Started

### Prerequisites

- Python 3.9+
- [pip](https://pip.pypa.io/en/stable/) or [conda](https://docs.conda.io/en/latest/)

### Installation

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Install the package in editable mode
pip install -e .
```

### Running Notebooks

```bash
jupyter lab
```

### Running Tests

```bash
pytest tests/
```

## Key Libraries

| Library | Purpose |
|---------|---------|
| `numpy` / `pandas` | Numerical computing and data manipulation |
| `scikit-learn` | Machine learning algorithms |
| `scipy` | Signal processing and scientific computing |
| `matplotlib` / `seaborn` | Visualization |
| `pydicom` | Reading DICOM medical imaging files |
| `wfdb` | Reading PhysioNet waveform-database files (ECG, etc.) |
| `mne` | EEG / MEG biomedical signal processing |
| `jupyterlab` | Interactive notebooks |

## Regulatory Notes

When working with medical device data, ensure compliance with applicable regulations (e.g., FDA 21 CFR Part 11, EU MDR) regarding data integrity, audit trails, and validation of software used in quality-critical workflows.
