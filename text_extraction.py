from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import secret


cv_client = ComputerVisionClient(secret.ENDPOINT, CognitiveServicesCredentials(secret.SUBSCRIPTION_KEY))


def read_text(img_path: str):
    image = open(img_path, 'rb')
    result = cv_client.recognize_printed_text_in_stream(image)

    for region in result.regions:
        for line in region.lines:
            for word in line.words:
                print("Text found was")
                print(word.text)

    print()


if __name__ == '__main__':
    read_text("./images/cert.jpeg")

