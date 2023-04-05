from flask import Flask, jsonify, abort, request
import cv2
import os

app = Flask(__name__)

valid_formats = ['jpg', 'png', 'gif']

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        url = request.form['url']
        format_img = url.split(".")[-1]
        if not os.path.exists(url):
            return abort(400, "File does not exist")
        elif format_img not in valid_formats:
            return abort(400, "Invalid image format")
        else:
            image = cv2.imread(url)
            h, w = image.shape[:2]
            (B, G, R) = image[100, 100]
            data = {
                'Image format': format_img,
                'Image size': {'Height': h, 'Width': w},
                'Image RGB color': {'Red': int(R), 'Green': int(G), 'Blue': int(B)}
            }
            return jsonify(data)
    else:
        return '''
            <form method="post">
                <label for="Note">
                <p>The Image path should be save in same directory where you save image_processing api file.</p>
                <label for="url">
                Enter the image file path:</label>
                <input type="text" id="url" name="url">
                <input type="submit" value="Submit">
            </form>
        '''
if __name__ == '__main__':
    app.run(debug=True)
