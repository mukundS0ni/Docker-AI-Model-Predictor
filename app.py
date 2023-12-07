from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Load the trained model
model = load_model('vani_model.h5')

# Create Flask application
app = Flask(__name__)

# Configure SQLAlchemy for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define PredictionLog model for the database
class PredictionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    prediction = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Define endpoint for predictions
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html', prediction=None, error=None)

    try:
        # Get image file from the request
        file = request.files['file']

        # Save the image to a temporary location
        image_path = f'temp_images/{datetime.now().strftime("%Y%m%d%H%M%S%f")}.jpg'
        file.save(image_path)

        # Load and preprocess the image
        test_image = image.load_img(image_path, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Make a prediction
        result = model.predict(test_image)

        # Process the prediction result
        prediction = 'Cat' if result[0][0] >= 0.5 else 'Dog'

        # Log the prediction to the database
        log_entry = PredictionLog(filename=image_path, prediction=prediction)
        db.session.add(log_entry)
        db.session.commit()

        # Return the prediction and render the HTML template
        return render_template('index.html', prediction=prediction, error=None)

    except Exception as e:
        return render_template('index.html', prediction=None, error=str(e))

# Run the Flask application
if __name__ == '__main__':
    with app.app_context():
        # Create the 'temp_images' directory if it doesn't exist
        os.makedirs('temp_images', exist_ok=True)

        # Create the database tables before running the app
        db.create_all()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
