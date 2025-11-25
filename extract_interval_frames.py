import cv2
import os

# 输入视频
input_path = "videos/stick_swing_exmple.mp4"
output_dir = "images"

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 打开视频
cap = cv2.VideoCapture(input_path)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 总帧数

# 想要保存的帧数
N = 500
N = min(N, frame_count)  # 防止视频帧数不足

# 计算步长
step = frame_count // N

saved = 0
for i in range(frame_count):
    ret, frame = cap.read()
    if not ret:
        break

    # 每隔 step 帧保存一张
    if i % step == 0 and saved < N:
        filename = os.path.join(output_dir, f"frame_{i:06d}.jpg")
        cv2.imwrite(filename, frame)
        saved += 1

    if saved >= N:
        break

cap.release()
print(f"✅ 已均匀抽取 {saved} 张图片到 {output_dir}/")
