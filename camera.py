import cv2  # import the opencv library


def main():
    vid = cv2.VideoCapture(0)

    stop = False
    while not stop:
        # Capture the video frame by frame
        ret, frame = vid.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # the 'q' button is set as the quitting button
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop = True

    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
