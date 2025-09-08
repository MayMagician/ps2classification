import cv2
import random
import os
from tqdm import tqdm

#initial configuration
video_path = "longplayGT4.mp4" #path to the video - in this example it's a Gran Turismo 4 gameplay video
output_dir = "gt4" #folder in which the screenshots will be saved - in this example it's Gran Turismo 4
num_screenshots = 1000 #number of screenshots to take - in this example, 1000
min_gap_sec = 1.5 #minimum time distance between screenshots - in this example, 1.5

#size of the dataset - in this example, 700/150/150
num_train = 700
num_test = 150
num_val = 150

#creating train, test and val folders inside output_dir
train_dir = os.path.join(output_dir, "train")
test_dir = os.path.join(output_dir, "test")
val_dir = os.path.join(output_dir, "val")
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

#uploading the video
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS) or 30
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count / fps

#selecting casual times to extract the screenshots
selected_times = []
attempts = 0
while len(selected_times) < num_screenshots:
    t = random.uniform(0, duration)
    if all(abs(t - st) > min_gap_sec for st in selected_times):
        selected_times.append(t)
    attempts += 1
    if attempts > num_screenshots*10:  #break to avoid infinite looping for shorter videos
        break

#extracting screenshots from the video with a progress bar
for idx, t in enumerate(tqdm(selected_times, desc="Extracting screenshots...")):
    frame_id = int(t * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = cap.read()
    if ret:
        #save it to the corresponding folder
        if idx < num_train:
            folder = train_dir
        elif idx < num_train + num_test:
            folder = test_dir
        else:
            folder = val_dir

        filename = os.path.join(folder, f"{folder.split(os.sep)[-1]}_{idx+1}.png")
        cv2.imwrite(filename, frame)

cap.release()
print(f"\nSaved {len(selected_times)} screenshots in {output_dir}, divided into train/test/val folders.")
