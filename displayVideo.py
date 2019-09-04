# 9/4 동영상 출력

import cv2

# 프레임 받아오기
capture = cv2.VideoCapture("Image/Star.mp4")

while True:
    # 현재 프래임 개수가 총 프래임 개수와 같을 때 (마지막 프레임)
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        # 다시 재생
        capture.open("SampleVideo.mp4")

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    # 33ms 마다 프레임 재생 / 어떤 키라도 누르면 break 종료.
    if cv2.waitKey(33) > 0: break

capture. release()
cv2.destroyAllWindows()