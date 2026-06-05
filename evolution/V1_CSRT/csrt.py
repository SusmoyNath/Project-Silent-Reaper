import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found")
    exit()

tracker = None
tracking = False

drawing = False
start_point = None
end_point = None
bbox = None
frame = None


def mouse_draw(event, x, y, flags, param):
    global drawing, start_point, end_point, tracker, tracking, bbox, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        end_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)

        x1 = min(start_point[0], end_point[0])
        y1 = min(start_point[1], end_point[1])
        w = abs(start_point[0] - end_point[0])
        h = abs(start_point[1] - end_point[1])

        if w > 20 and h > 20:
            bbox = (x1, y1, w, h)

            tracker = cv2.legacy.TrackerCSRT_create()
            tracker.init(frame, bbox)

            tracking = True


cv2.namedWindow("Drone Camera")
cv2.setMouseCallback("Drone Camera", mouse_draw)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    display_frame = frame.copy()

    # Draw selection box while dragging
    if drawing and start_point and end_point:
        cv2.rectangle(display_frame, start_point, end_point, (0,255,255), 2)

    # Tracking
    if tracking and tracker is not None:

        success, bbox = tracker.update(frame)

        if success:
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(display_frame, (x,y), (x+w,y+h), (0,0,255), 3)
        else:
            cv2.putText(display_frame, "Tracking Lost", (20,40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Drone Camera", display_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
