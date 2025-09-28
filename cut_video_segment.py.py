import cv2

# 输入视频路径
input_path = "videos/stick_swing_exmple.mp4"
output_path = "videos/stick_swing_20s.mp4"

# 打开视频文件
cap = cv2.VideoCapture(input_path)

# 获取视频的基本信息
fps = cap.get(cv2.CAP_PROP_FPS)              # 帧率 (frames per second)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # 视频宽度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 视频高度
fourcc = cv2.VideoWriter_fourcc(*'mp4v')     # 视频编码器 (mp4 常用 mp4v/avc1/H264)

# 输出视频写入器
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# 计算前 20 秒需要的帧数
max_frames = int(fps * 20)

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # 读取失败，可能是视频结束
    
    out.write(frame)   # 写入这一帧
    frame_count += 1

    if frame_count >= max_frames:
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
