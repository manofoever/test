import boto3


def upload_to_S3(bucket_name, file_path, object_name):
    aws_access_key_id = ''
    aws_secret_access_key = ''
    aws_region = 'us-east-1'
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=aws_region
                      )

    try:
        s3.upload_file(file_path, bucket_name, object_name)

    except Exception as e:
        print(f"Error uploading to S3 :{e}")
        return False

    return True


if __name__ == "__main__":
    bucket_name = 'mynewbucket-for-myapp'
    file_path = 'requirements.txt'
    object_name = 'requirements.txt'

    upload_to_S3(bucket_name, file_path, object_name)
