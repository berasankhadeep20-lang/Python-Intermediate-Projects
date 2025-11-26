#to bulid a programme that identifies how many fingers are being pointed up in the laptop camera using mediapipe and opencv
import cv2
import mediapipe as mp
class FingerCounter:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=2,
                                         min_detection_confidence=0.5,
                                         min_tracking_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils

    def count_fingers(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image_rgb)
        finger_count = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_count += self._count_fingers_in_hand(hand_landmarks, image.shape)

                self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        return finger_count

    def _count_fingers_in_hand(self, hand_landmarks, image_shape):
        finger_tips_ids = [4, 8, 12, 16, 20]
        fingers_up = 0

        for tip_id in finger_tips_ids:
            tip_y = hand_landmarks.landmark[tip_id].y * image_shape[0]
            pip_y = hand_landmarks.landmark[tip_id - 2].y * image_shape[0]

            if tip_y < pip_y:
                fingers_up += 1

        return fingers_up
def main():
    cap = cv2.VideoCapture(0)
    finger_counter = FingerCounter()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        finger_count = finger_counter.count_fingers(frame)

        cv2.putText(frame, f'Fingers Up: {finger_count}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Finger Counter', frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
