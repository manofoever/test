from flask import Flask, jsonify
import boto3


app = Flask(__name__)

count = 0

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
@app.route('/ask_me', methods = ['POST'])
def get_json_data():
    data = {"message" : "Hello, what do you want?"}
    return jsonify(data)

@app.route('/ask_me_anything')
def get_data():
    global count
    data = {"message" : "Hello, what do you want?"}
    with open(f'test_{count}.txt','w') as f:
        f.write(str(data))
        count+=1

    upload_to_S3('mynewbucket-for-myapp', 'test.txt', f'input/test_{count}.txt')
    return jsonify(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)




