from flask import Flask, request, jsonify
from sftp_api import *
app = Flask(__name__)

# ***************************   SFTP service ***********************************
@app.route('/SFTP', methods=['POST'])
def download_txt_files_route():
        data = request.json
        response_message = request_data(data)
        #download_txt_files(host, username, password)
        return jsonify({'message': response_message})
# *************************       END      **************************************
if __name__ == '__main__':
    app.run(host='10.10.30.37',port='5000',debug=True)
