# 3DFIT

Event-Based Vibration Measurement via 3D Spatiotemporal Surface Fitting

## Overview

3DFIT is an event-based vibration measurement framework designed for neuromorphic vision sensors.

Instead of converting events into image frames, 3DFIT directly models the spatiotemporal event cloud and estimates vibration frequency through implicit surface fitting.

This repository provides:

- 3DFIT (proposed method)
- ECT (Event Centroid Tracking)
- GPE (Gabor Phase Estimation)

for vibration frequency estimation and comparison.

---

## Repository Structure

```text
3dfit/

├── data/
│
├── configs/
│   ├── audio/
│   ├── ruler/
│   └── simulation/
│
├── datasets/
│   ├── loader.py
│   └── roi.py
│
├── methods/
│   ├── base.py
│   │
│   ├── three_dfit/
│   │   ├── __init__.py
│   │   ├── grouping.py
│   │   ├── fitting.py
│   │   └── estimator.py
│   │
│   ├── ect/
│   │   ├── __init__.py
│   │   ├── centroid.py
│   │   └── estimator.py
│   │
│   └── gpe/
│       ├── __init__.py
│       ├── gabor.py
│       ├── phase.py
│       └── estimator.py
│
├── metrics/
│   ├── __init__.py
│   ├── frequency.py
│   └── amplitude.py
│
├── experiments/
│   ├── simulation/
│   ├── audio_vibration/
│   └── ruler_vibration/
│
├── results/
│
├── run.py
├── requirements.txt
└── README.md
```

---

## Installation

### Create environment

```bash
conda create -n 3dfit python=3.10
conda activate 3dfit
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Dataset

Place all event datasets into:

```text
data/
```

Example:

```text
data/

├── 20hz-20.hdf5
├── 30hz-20.hdf5
├── 50hz-20.hdf5
├── 100hz-20.hdf5
├── 200hz-20.hdf5
└── zdbiaochi.hdf5
```

---

## Quick Start

### Run 3DFIT

```bash
python run.py \
    --method 3dfit \
    --config configs/audio/30hz.yaml
```

### Run ECT

```bash
python run.py \
    --method ect \
    --config configs/audio/30hz.yaml
```

### Run GPE

```bash
python run.py \
    --method gpe \
    --config configs/audio/30hz.yaml
```

---

## Configuration File

Example:

```yaml
dataset: data/30hz-20.hdf5

roi:
  x_min: 100
  x_max: 600
  y_min: 420
  y_max: 460

time:
  start: 0.0
  end: 1.0

ground_truth:
  frequency: 30
```

---

## Methods

### 3DFIT

The proposed method models the event cloud as an implicit spatiotemporal surface:

```math
Ax + By + C\sin(2\pi ft + \phi) + D = 0
```

The vibration frequency is estimated through nonlinear optimization.

### ECT

Event Centroid Tracking.

The vibration trajectory is extracted from event centroids over time and analyzed using FFT.

### GPE

Gabor Phase Estimation.

Events are accumulated into temporal frames and vibration frequency is estimated through phase variations of complex Gabor responses.

---

## Evaluation Metrics

Frequency Error

```math
E_f = |f_{est} - f_{gt}|
```

Relative Frequency Error

```math
RE_f =
\frac{|f_{est}-f_{gt}|}
{f_{gt}}
\times 100\%
```

Amplitude Error

```math
E_A = |A_{est} - A_{gt}|
```

Relative Amplitude Error

```math
RE_A =
\frac{|A_{est}-A_{gt}|}
{A_{gt}}
\times 100\%
```

---

## Experiments

Three experimental settings are included:

### Simulation

Synthetic vibrating rod events with controllable frequency and amplitude.

### Audio Vibration

Speaker-driven vibration experiments.

Frequencies:

- 20 Hz
- 30 Hz
- 50 Hz
- 100 Hz
- 200 Hz

### Ruler Vibration

Free vibration measurements of a cantilever ruler.

---

## Example Result

30 Hz audio vibration experiment:

| Method | Estimated Frequency (Hz) |
|----------|----------|
| 3DFIT | 30.000 |
| ECT | 30.272 |
| GPE | 30.364 |

---

## Citation

If you find this work useful, please cite:

```bibtex
@article{3dfit2026,
  title={3DFIT: Event-Based Vibration Measurement via 3D Spatiotemporal Surface Fitting},
  author={Author},
  journal={TBD},
  year={2026}
}
```

---

## License

This project is released under the MIT License.
