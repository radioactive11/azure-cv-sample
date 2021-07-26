from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

from PIL import Image, ImageDraw


import secret


def draw_rectangle(object, draw):
    rect = object.rectangle
    left = rect.x
    top = rect.y
    right = left + rect.w
    bottom = top + rect.h

    coords = ((left, top), (right, bottom))
    draw.rectangle(coords, outline='green', width=30)


def get_objects(results, draw):
    if len(results.objects) == 0:
        print("No onj detected")
    
    else:
        print("Objects: ")
        for object in results.objects:
            left = object.rectangle.x
            right = left + object.rectangle.w
            top = object.rectangle.y
            bottom = top + object.rectangle.h
            print(f"{object.object_property} found at {left} {right} {top} {bottom}")
            draw_rectangle(object, draw)
    print()

def get_tags(results):
    print("Tags: ")
    if len(results.tags) == 0:
        print("No tags were found in the image")
    
    else:
        for tag in results.tags:
            print(f"{tag.name} with confidence {tag.confidence * 100}")
    print()


def local_image(img_path: str):
    cv_client = ComputerVisionClient(secret.ENDPOINT, CognitiveServicesCredentials(secret.SUBSCRIPTION_KEY))
    image_bytes = open(img_path, 'rb')
    image = Image.open(img_path)
    draw = ImageDraw.Draw(image)

    FEATURE = ['objects', 'tags']

    results = cv_client.analyze_image_in_stream(image_bytes, FEATURE)
    # get_tags(results)
    get_objects(results, draw)

    image.show()




if __name__ == '__main__':
    local_image("./images/traffic.jpg")