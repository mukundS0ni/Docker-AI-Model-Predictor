# Use the official TensorFlow image as a base image
FROM tensorflow/tensorflow:latest

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install required Python packages
RUN pip install --ignore-installed Flask-WTF
RUN pip install --ignore-installed Flask
RUN pip install --ignore-installed Pillow Flask
RUN pip install --ignore-installed flask_sqlalchemy

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
