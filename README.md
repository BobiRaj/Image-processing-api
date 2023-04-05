# Image-processing-api
In this file take as user input image path and then written the image description like RGB color height width.

The first thing we need to do is install the required dependencies. This code requires Flask and OpenCV.

from flask import Flask, jsonify, abort, request
import cv2

app = Flask(__name__)

valid_formats = ['jpg', 'png', 'gif']

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        url = request.form['url']
        format_img = url.split(".")[-1]
        if format_img in valid_formats :
            image = cv2.imread(url)
            if image is None:
                return abort(400, "Invalid image path")
            h, w = image.shape[:2]
            (B, G, R) = image[100, 100]
            data = {
                'Image format': format_img,
                'Image size': {'Height': h, 'Width': w},
                'Image RGB color': {'Red': int(R), 'Green': int(G), 'Blue': int(B)}
            }
            return jsonify(data)
        else:
            return abort(400, "Invalid image format")
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
This code defines a Flask application with a single endpoint (/). The endpoint can handle both GET and POST requests.

If the request method is POST, the application reads the value of the url parameter from the form data submitted by the client. It then checks if the image format is valid by checking if the file extension is one of jpg, png, or gif.

If the image format is valid, the application reads the image using OpenCV and extracts the image size and RGB color at the pixel location (100, 100). It then returns a JSON object containing the image format, size, and RGB color.

If the request method is GET, the application displays an HTML form that allows the user to enter the image file path.

The if __name__ == '__main__': block runs the application when the file is executed.

To run the application, navigate to the directory containing app.py in your terminal and execute the command python app.py.

Once the application is running, you can access it in your web browser by navigating to http://127.0.0.1:5000/. If you submitted the image file path through the HTML form, the application will display a JSON object containing the image information. If you submitted the image file path using a tool like curl or Postman, the application will return the JSON object directly.
