import boto3
from PIL import Image
import os
import io

# ✅ Initialize S3 client globally
s3 = boto3.client('s3')

# ✅ Read environment variables
output_bucket = os.environ['OUTPUT_BUCKET']
THUMB_W = int(os.environ.get('THUMB_W', '300'))
THUMB_H = int(os.environ.get('THUMB_H', '300'))

def lambda_handler(event, context):
    try:
        print("Event received:", event)

        source_bucket = event['bucket']
        source_key = event['key']
        print(f"Source: {source_bucket}/{source_key}")

        obj = s3.get_object(Bucket=source_bucket, Key=source_key)
        img_data = obj['Body'].read()
        print("Image downloaded")

        image = Image.open(io.BytesIO(img_data))
        print("Image opened")

        image.thumbnail((THUMB_W, THUMB_H))
        print("Image resized")

        buffer = io.BytesIO()
        fmt = image.format or 'JPEG'
        image.save(buffer, format=fmt)
        buffer.seek(0)
        print("Image saved to buffer")

        base = source_key.rsplit('/', 1)[-1]
        name, ext = os.path.splitext(base)
        output_key = f"{name}_thumb{ext or '.jpg'}"
        print(f"Output key: {output_key}")

        s3.put_object(
            Bucket=output_bucket,
            Key=output_key,
            Body=buffer.getvalue(),
            ContentType=f"image/{fmt.lower()}"
        )
        print("Image uploaded")

        return {
            "status": "success",
            "file": output_key
        }

    except Exception as e:
        print("Error occurred:", str(e))
        return {
            "status": "error",
            "message": str(e)
        }