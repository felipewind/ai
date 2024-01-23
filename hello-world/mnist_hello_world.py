# Import TensorFlow and the MNIST dataset from keras
import tensorflow as tf
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset into training and testing sets
# x_train, y_train are the training images and labels
# x_test, y_test are the testing images and labels
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the image data from values between 0-255 to 0-1 to aid in training
x_train, x_test = x_train / 255.0, x_test / 255.0

# Define the model architecture
model = tf.keras.models.Sequential([
  # Flatten the 28x28 images into a 784 element vector
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  # Add a densely-connected neural layer with 128 units and ReLU activation
  tf.keras.layers.Dense(128, activation='relu'),
  # Add dropout to prevent overfitting with a rate of 0.2
  tf.keras.layers.Dropout(0.2),
  # Output layer with 10 units (one per class) using softmax activation for multi-class classification
  tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model specifying the optimizer, loss function, and metrics to monitor
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model on the training data
# x_train, y_train are the input features and labels respectively
# epochs=5 means the training process will iterate over the entire dataset 5 times
model.fit(x_train, y_train, epochs=5)

# Evaluate the model's performance on the test dataset
# x_test, y_test are the unseen features and labels used to evaluate the model
model.evaluate(x_test, y_test)
