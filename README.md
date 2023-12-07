**README for Dog-Cat Image Classifier**

**Dataset: https://www.kaggle.com/datasets/chetankv/dogs-cats-images** 

**Step 1: Model Building:**

**Vanilla Model Architecture:**

```plaintext
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 224, 224, 16)      448       
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 224, 224, 16)      2320      
...
dropout_2 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 2)                 1026      
=================================================================
Total params: 7,602,834
Trainable params: 7,602,834
Non-trainable params: 0
_________________________________________________________________
```

**Training:**

Training on Vanilla CNN has started ...

```plaintext
Model Accuracy: Approx-91%
Epoch 1/15
150/150 [==============================] - 172s 1s/step - loss: 2.2711 - accuracy: 0.5029 - val_loss: 0.6572 - val_accuracy: 0.6077
...
Epoch 15/15
150/150 [==============================] - 160s 1s/step - loss: 0.2479 - accuracy: 0.8966 - val_loss: 0.2940 - val_accuracy: 0.8739
```

**Step 2: Python Code:**

**Requirements:**
```bash
RUN pip install --ignore-installed Flask-WTF
RUN pip install --ignore-installed Flask
RUN pip install --ignore-installed Pillow Flask
RUN pip install --ignore-installed flask_sqlalchemy
```

**RUN:**
1. Clone the entire codebase.
2. Run `python app.py`.
3. Local run at http://127.0.0.1:5000/predict.
4. Upload an image of a Dog or Cat to get predictions on the page.
![Dog or Cat Image](https://github.com/mukuRepo/Docker-AI-Model/assets/60322472/bd791d1e-688a-4bb6-9e4d-4c16173731ff)
5. Prediction database can be found in the `instance` folder.

**Docker Implementation:**

1. Build the Docker image:
   ```bash
   docker build -t mukunddocker/dog_cat_image_classifier:1.1 .
   ```

2. Tag the Docker image:
   ```bash
   docker tag mukunddocker/dog_cat_image_classifier:1.1 mukunddocker/dog_cat_image_classifier:latest
   ```

3. Push the Docker image to Docker Hub:
   ```bash
   docker push mukunddocker/dog_cat_image_classifier:latest
   ```

4. Apply Kubernetes deployment:
   ```bash
   kubectl apply -f deployment.yaml
   ```

5. Apply Kubernetes service:
   ```bash
   kubectl apply -f service.yaml
   ```

6. Get the list of pods:
   ```bash
   kubectl get pods -l app=dog-cat-classifier
   ```

7. Get the service details:
   ```bash
   kubectl get services dog-cat-classifier-service
   ```

8. Visit http://localhost:8000/predict to make predictions.
   
![Docker Prediction](https://github.com/mukuRepo/Docker-AI-Model/assets/60322472/1d0ca42a-a167-4b52-bbe6-7c82b2934e9a)
