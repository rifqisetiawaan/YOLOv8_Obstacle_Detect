from roboflow import Roboflow
rf = Roboflow(api_key="xi0d0TDopsbaUEGnmKe1")
project = rf.workspace("krsbipolmanws").project("krsbi-obstacle")
dataset = project.version(1).download("yolov8")
