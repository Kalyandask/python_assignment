from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/transform', methods=['POST'])
def transform():
    time.sleep(10)  # Simulate a 10-second delay
    data = request.json
    print(f"Received Transform Data: {data}")
    return jsonify({"status": "success"}), 200

@app.route('/translation', methods=['POST'])
def translation():
    time.sleep(10)
    data = request.json
    print(f"Received Translation Data: {data}")
    return jsonify({"status": "success"}), 200

@app.route('/rotation', methods=['POST'])
def rotation():
    time.sleep(10)
    data = request.json
    print(f"Received Rotation Data: {data}")
    return jsonify({"status": "success"}), 200

@app.route('/scale', methods=['POST'])
def scale():
    time.sleep(10)
    data = request.json
    print(f"Received Scale Data: {data}")
    return jsonify({"status": "success"}), 200

@app.route('/file-path', methods=['GET'])
def file_path():
    project_path = request.args.get('projectpath')
    path = "/path/to/file" if not project_path else "/path/to/project"
    return jsonify({"path": path}), 200

if __name__ == '__main__':
    app.run(debug=True)