from flask import Flask, jsonify
import boto3

app = Flask(__name__)

@app.route('/ask_me', methods = ['POST'])
def get_json_data():
    data = {"message" : "Hello, what do you want?"}
    return jsonify(data)

@app.route('/ask_me_anything')
def get_data():
    data = {"message" : "Hello, what do you want?"}
    with open('test.txt','w') as f:
        f.write(data)

    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

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