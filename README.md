# TAJ: A Platform for Integrating Tumor Detection and Depth Perception for Endoscopic Surgery

A software-based tool collection designed to enhance precision and efficiency in lung cancer surgery through real-time tumor detection and depth estimation.

## Overview

TAJ is a comprehensive platform that combines advanced computer vision techniques with an intuitive user interface to assist surgeons during endoscopic procedures. The system provides real-time tumor detection, depth estimation, and visual feedback to enhance surgical precision.

## Features

- **Real-time Tumor Detection**: Utilizes YOLOv5 object detection model with 95.5% precision and 85.3% recall
- **Advanced Depth Estimation**: Custom algorithm outperforming traditional MiDaS approaches
- **Live User Interface**: Built with Python Tkinter and Matplotlib for real-time data visualization
- **High Performance**: Custom depth algorithm is 1.48-4.33x faster than MiDaS variants
- **Real-time Processing**: Stores and displays information with minimal latency

## Technical Specifications

### Tumor Detection
- **Model**: YOLOv5 object detection
- **Confidence Threshold**: 0.75 (optimized for precision-recall balance)
- **Performance**: 95.5% precision, 85.3% recall

### Depth Estimation
- **Primary Method**: Custom algorithm using tumor frame size relative to camera feed dimensions
- **Normalization**: Modified sigmoid function
- **Alternative Methods**: MiDaS-Small, DPT-Hybrid, DPT-Large (for comparison)
- **Performance**: Superior correlation with real depth compared to MiDaS algorithms

### User Interface
- **Framework**: Python Tkinter
- **Visualization**: Matplotlib for live graphing
- **Display**: Real-time tumor detection overlays and depth information

## Installation

### Prerequisites
- Python 3.7+
- Required Python packages:
  ```
  torch
  torchvision
  opencv-python
  numpy
  matplotlib
  tkinter
  ultralytics
  ```

### Setup
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure YOLOv5 model weights are available in the project directory

## Usage

### Quick Start
Run the application with:
```bash
python endostart.py
```

### Operation
1. Connect your endoscopic camera
2. Launch the TAJ platform using the command above
3. The system will automatically begin:
   - Detecting tumors in real-time
   - Calculating depth estimations
   - Displaying results in the user interface
4. Monitor the live graphs and detection overlays during surgical procedures

## System Architecture

The TAJ platform integrates three main components:

1. **Detection Module**: YOLOv5-based tumor identification
2. **Depth Estimation Module**: Custom algorithm for relative depth calculation
3. **User Interface Module**: Real-time visualization and data management

## Performance Metrics

| Method | Speed Comparison | Depth Correlation |
|--------|------------------|-------------------|
| Custom Algorithm | Baseline | Strong positive trend |
| MiDaS-Small | 1.48x slower | Weaker correlation |
| DPT-Hybrid | 2.97x slower | Weaker correlation |
| DPT-Large | 4.33x slower | Weaker correlation |

## Research Background

This project addresses the limited availability of software-based tools for computer-aided lung cancer surgery. By combining state-of-the-art deep learning techniques with practical surgical requirements, TAJ provides a data-driven solution for enhancing surgical procedures.

## Authors

- Ali Fakhry
- Thaison Le - The Department of Computer Science, Flexible AI-enabled Mechatronics Systems Lab (FAMS), Tandon School of Engineering, New York University
- Junzhe Zhang
- Rui Li

## Publication

Published in: 2024 International Symposium on Medical Robotics (ISMR)  
Conference Date: June 3-5, 2024  
Location: Atlanta, GA, USA  
DOI: 10.1109/ISMR63436.2024.10585947

## License

Please refer to the paper and contact the authors for licensing information regarding the use of this software in medical applications.

## Contributing

This is a research project. For questions or collaboration opportunities, please contact the authors through their affiliated institutions.

## Disclaimer

This software is designed for research purposes. Any medical applications should undergo appropriate validation and regulatory approval before clinical use.

## Support

For technical questions or issues, please refer to the original paper or contact the research team at New York University's Flexible AI-enabled Mechatronics Systems Lab.
