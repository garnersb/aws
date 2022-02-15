# List Objects in Bucket using the Client API
# Return type: dict / additional API calls needed to get objects

import boto3

# TODO: provide BUCKET_NAME

bucketname = "BUCKET_NAME"

def listClient():
    s3client = boto3.client('s3')
    response = s3client.list_objects_v2(Bucket=bucketname)
    print("\nUsing Client API: ")
    print()
    # print (response)
    # print ("Unformatted Contents:\n",response['Contents'],"\n\n")
    for content in response['Contents']:
        print("Object/Filename:  "+content['Key'],content['LastModified'])

listClient()

# List Objects in Bucket using the Resource API
# Resources represent an object-oriented interface to Amazon Web Services (AWS).
# They provide a higher-level abstraction than the raw, low-level calls made by service clients


def listResource():
    s3resource = boto3.resource('s3')
    bucket = s3resource.Bucket(bucketname)
    print("\n\nUsing Resource API: \n")
    for object in bucket.objects.all():
        print("Object/Filename:  "+object.key, object.last_modified)

listResource()
