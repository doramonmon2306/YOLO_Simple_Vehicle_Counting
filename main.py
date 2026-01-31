import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("traffic.mp4")
assert cap.isOpened(), "Error reading video file"

region_points = [[340, 418], [930, 422]]

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

counter = solutions.ObjectCounter(
    show=True, 
    region=region_points, 
    model="yolo26n.pt",  
)

while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Done")
        break

    results = counter(im0)
    video_writer.write(im0) 

cap.release()
video_writer.release()
cv2.destroyAllWindows()