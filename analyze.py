#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import sys

def main():
    data_path = Path('data')
    csv_files = list(data_path.glob('*.csv'))

    datasets = {}
    for csv_file in csv_files:
            df = pd.read_csv(csv_file)
            datasets[csv_file.stem] = df

    output_path = Path('output')
    output_path.mkdir(exist_ok=True)

    sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})
    plt.rcParams['figure.figsize'] = (12, 6)

    for name, df in datasets.items():
        
        stats = {
            'count': len(df),
            'mean': df["latency_ms"].mean(),
            'median': df["latency_ms"].median(),
            'std_dev': df["latency_ms"].std(),
            'min': df["latency_ms"].min(),
            'max': df["latency_ms"].max(),
            'p25': df["latency_ms"].quantile(0.25),
            'p75': df["latency_ms"].quantile(0.75),
            'p95': df["latency_ms"].quantile(0.95),
            'p99': df["latency_ms"].quantile(0.99),
        }
        
        print (f"statistics for {name}:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
            
        fig, ax = plt.subplots()

        ax.hist(df['latency_ms'], bins=30, edgecolor='black', alpha=0.7)
        ax.set_xlabel('Latency (ms)', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.set_title(f'{name}', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)

        ax.axvline(stats['mean'], color='red', linestyle='--', linewidth=2, label=f'Mean: {stats['mean']:.2f} ms')
        ax.axvline(stats['median'], color='green', linestyle='--', linewidth=2, label=f'Median: {stats['median']:.2f} ms')
        ax.axvline(stats['p25'], color='blue', linestyle='--', linewidth=1, label=f'P25: {stats['p25']:.2f} ms')
        ax.axvline(stats['p75'], color='orange', linestyle='--', linewidth=1, label=f'P75: {stats['p75']:.2f} ms')
        ax.axvline(stats['p95'], color='purple', linestyle='--', linewidth=1, label=f'P95: {stats['p95']:.2f} ms')
        ax.legend()

        plt.tight_layout()
        output_file = output_path / f'histogram_{name}.png'
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Graph saved: {output_file}")


if __name__ == '__main__':
    main()
