import boto3
import json

# Create an S3 resource object using the Boto3 library
s3 = boto3.resource('s3')

# Define the Lambda function
def lambda_handler(event, context):
    
    bucket = s3.Bucket('rawbucket122')
    dest_bucket = s3.Bucket('destbucket122')

    # Print the source and destination buckets (for debugging purposes)
    print(bucket)
    print(dest_bucket)

    # Process each object individually from the source bucket ('rawbucket122')
    for obj in bucket.objects.all():
        # Get the key (object name) of the current object
        dest_key = obj.key
        print(dest_key)
        
        # Copy the object from the source bucket to the destination bucket
        s3.Object(dest_bucket.name, dest_key).copy_from(CopySource={'Bucket': obj.bucket_name, 'Key': obj.key})
