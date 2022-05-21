# For extracting files from Amazon S3 Buckets
import boto3
from botocore import UNSIGNED
from botocore.client import Config

# Working with images
from PIL import Image
import io
import base64

s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
bucket = s3.Bucket("airborne-obj-detection-challenge-training")

def download_images(image_name):
    img_s3 = bucket.Object(image_name)
    img_content = img_s3.get()['Body'].read()
    img_PIL = Image.open(io.BytesIO(img_content))
    img_smaller = img_PIL.convert('RGB').resize((224,224))
    temp_img = io.BytesIO()
    img_smaller.save(temp_img, format = "png")
    png_encoded = base64.b64encode(temp_img.getvalue())
    
    return str(png_encoded)
