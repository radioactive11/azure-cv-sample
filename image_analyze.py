from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import secret


cv_client = ComputerVisionClient(secret.ENDPOINT, CognitiveServicesCredentials(secret.SUBSCRIPTION_KEY))


def describe_image(img_path: str):
    local_image = open(img_path, 'rb')
    result = cv_client.describe_image_in_stream(local_image)

    if len(result.captions) == 0:
        print("There is no desc availble")

    else:
        for caption in result.captions:
            print(f"Captions: {caption.text} with confidence {caption.confidence * 100}")
    print()


def detect_face(img_path: str):
    local_image = open(img_path, 'rb')
    image_features = ['faces']

    result = cv_client.analyze_image_in_stream(local_image, image_features)

    if len(result.faces) == 0:
        print("No faces were found :(")
    
    else:
        for face in result.faces:
            print(f"{face.gender} found of age {face.age}")
    print()


def celeb(img_path: str):
    local_image = open(img_path, 'rb')
    response = cv_client.analyze_image_by_domain_in_stream("celebrities", local_image)

    if len(response.result['celebrities']) == 0:
        print("No celeb was found")
    
    else:
        for celeb in response.result['celebrities']:
            print(celeb)

def landmarks(img_path: str):
    local_image = open(img_path, 'rb')
    response = cv_client.analyze_image_by_domain_in_stream("landmarks", local_image)

    if len(response.result['landmarks']) == 0:
        print("No landmark was found")
    
    else:
        for landmark in response.result['landmarks']:
            print(landmark)



if __name__ == '__main__':
    landmarks("./images/delhi.jpg")


