import torch
import cv2  # import the opencv library

# TODO : reprendre le modèle d'autoencoder de CIFAR10 et l'importer
# TODO : passer nos visage dans l'autoencoder


# on prends l'autoencoder
# on passe nos tronche dans la moulinette
# on a une liste de vecteur de "référence"
# on extrait les visages de la frame avec MTCNN
# on compare avec nos vecteur de référence
#si ça dépasse un certain seuil, on considère que c'est la personne

def main():
    # define a video capture object
    vid = cv2.VideoCapture(0)

    model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)

    stop = False
    while not stop:
        # Capture the video frame by frame
        ret, frame = vid.read()

        results = model(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        r_img = results.render()

        im_rgb = cv2.cvtColor(r_img[0], cv2.COLOR_RGB2BGR)  # Because of OpenCV reading images as BGR
        # Display the resulting frame
        cv2.imshow('frame', im_rgb)

        # the 'q' button is set as the quitting button
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop = True

    vid.release()
    cv2.destroyAllWindows()

    # # Model
    # model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, trust_repo=False)
    #
    # # Images
    # imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images
    #
    # # Inference
    # results = model(imgs)
    #
    # # Results
    # print("results")
    # results.print()
    # results.save()  # or .show()
    #
    # results.xyxy[0]  # img1 predictions (tensor)
    # results.pandas().xyxy[0]


if __name__ == "__main__":
    main()
