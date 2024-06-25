from flask import Flask, jsonify, render_template, request
import boto3
import something

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

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ask_me', methods = ['POST'])
def get_json_data():

    if request.method == 'POST':
        name = request.form['name']
    with open(f'test_{name}.txt','w') as f:
        f.write(str(name))

    #upload_to_S3('mynewbucket-for-myapp', 'test.txt', f'input/test_{name}.txt')
    return 'f Thank you '
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
    app.run(host="0.0.0.0",port=5000)




