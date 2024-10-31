import boto3
s3 = boto3.client(
    's3',
    region_name='us-east-1',  # Replace with your desired region

)
# Upload a file to S3
result = s3.put_object(
    Bucket='arjastarkbucket',  # Replace with your bucket name
    Key='testfrompython2.txt',  # Name of the file in S3
    Body='This is a test upload from Python WITHOUT CREDENTIALS'  # Content of the file
)
print("Uploading to S3.....")
print(result)
