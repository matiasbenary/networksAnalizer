# Transaction Latency Analytics

Analyze CSV files with transaction latency data and generate statistics and histograms.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install jupyter
   ```

2. Place your CSV files in `data/` folder (format: `tx_id,latency_ms`)

3. Launch Jupyter and open the notebook:
   ```bash
   jupyter notebook analyze.ipynb
   ```

Results will be saved in `output/` folder.
