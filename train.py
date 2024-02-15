from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='/home/krsbi/YOLOv8_Obstacle_Detect/KRSBI-Obstacle-1/data.yaml', 
   imgsz=640,
   epochs=10,
   batch=5,
   name='yolov8n_se'
)