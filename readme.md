# Smart Traffic Pedestrian Analyzer

A project for detecting and analyzing pedestrian traffic using YOLOv8 and custom datasets. This repository provides code and instructions for training a YOLOv8 model on a smart traffic dataset and running inference on video files.

## Features
- Train a YOLOv8 model on custom pedestrian traffic data
- Use Roboflow for dataset management and downloading
- Run inference on video files to detect pedestrians
- Visualize training results and confusion matrix

## Project Structure
- `Smart_Traffic_Model_training_using_Yolov8.ipynb`: Jupyter notebook for training the YOLOv8 model
- `main.py`: Script for running inference on video files
- `best.pt`: Trained YOLOv8 model weights (generated after training)
- `requirements.txt`: List of required Python packages

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/rakeshdeep/smart-traffic-pedestrian-analyzer.git
cd smart-traffic-pedestrain-analyzer
```

### 2. Install Requirements
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Training the Model
- Open `Smart_Traffic_Model_training_using_Yolov8.ipynb` in Jupyter Notebook or VS Code.
- Replace `your-roboflow-api-key` with your actual Roboflow API key.
- Run all cells to download the dataset, train the model, and visualize results.
- The best model weights will be saved as `best.pt`.

### 4. Running Inference
- Update the `source` parameter in `main.py` to your video file path.
- Run the script:
```bash
python main.py
```
- The script will display and save the detection results.

## Requirements
- Python 3.8+
- [ultralytics](https://www.ultralytics.com/)
- [roboflow](https://app.roboflow.com/)

Install all requirements with:
```bash
pip install -r requirements.txt
```

## Notes
- You need a Roboflow account and API key to download datasets.
- The model can be retrained with your own data by updating the Roboflow project and version in the notebook.

