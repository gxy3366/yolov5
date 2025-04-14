import torch

# 加载 YOLOv5 模型（选项：yolov5n, yolov5s, yolov5m, yolov5l, yolov5x）
model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # 默认：yolov5s

# 定义输入图像源（URL、本地文件、PIL 图像、OpenCV 帧、numpy 数组或列表）
img = "https://ultralytics.com/images/zidane.jpg"  # 示例图像

# 执行推理（自动处理批处理、调整大小、归一化）
results = model(img)

# 处理结果（选项：.print(), .show(), .save(), .crop(), .pandas()）
results.print()  # 将结果打印到控制台
results.show()  # 在窗口中显示结果
results.save()  # 将结果保存到 runs/detect/exp