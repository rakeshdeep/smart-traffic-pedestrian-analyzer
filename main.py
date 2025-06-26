from ultralytics import YOLO

model = YOLO("/smart-traffic-pedestrain-analyzer/best.pt")  # Adjust the path to your model file

results = model(source="source/of/your/video/file", conf = 0.25, show=True, save=True)
