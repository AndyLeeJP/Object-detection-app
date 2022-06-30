from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import json

with open ('secret.json') as f:
    secret = json.load(f)

KEY = secret['KEY']
ENDPOINT = secret['ENDPOINT']

computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))  #Authenticate the client

remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"  #Analyze image


print("===== Describe an image - remote =====")
# Call API with remote image
description_results = computervision_client.describe_image(remote_image_url )

# Print results with confidence score
print("Description of the remote image: ")
if (len(description_results.captions) == 0):
    print("No description detected.")
else:
    for caption in description_results.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))

print("===== Categorize an image - remote =====")
# Select the visual feature(s) you want
remote_image_feathures = ["categories"]
# Call API with URL and features
categories_results_remote = computervision_client.analyze_image(remote_image_url, remote_image_feathures)

# Print results with confidence score
print("Categorize from remote image: ")
if (len(categories_results_remote.categories) == 0):
    print("No categories detected.")
else:
    for category in categories_results_remote.categories:
        print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))

print("===== Tag an image - remote =====")
# Call API with remote image
tags_result_remote = computervision_client.tag_image(remote_image_url )

# Print results with confidence score
print("Tags in the remote image: ")
if (len(tags_result_remote.tags) == 0):
    print("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
print()


print("===== Detect Object - remote =====")
# Call URL image with defferent objects
remote_image_url_objects = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

# Call API with URL
detect_objects_results_remote = computervision_client.detect_objects(remote_image_url_objects )

# Print detected objects results with bounding boxes
print("Detecting objects in remote image: ")
if (len(detect_objects_results_remote.objects) == 0):
    print("No objects detected.")
else:
    for object in detect_objects_results_remote.objects:
        print("object at location {}, {}, {}, {}".format( \
        object.rectanhle.x, object.rectangle.x + object.rectangle.w, \
        object.rectanhle.y, object.rectanhle.y, object.rectanhle.h))
print()
