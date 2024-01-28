## Install Python and Pip
Within your Ubuntu terminal in WSL2, install Python and Pip (Python’s package installer) by running:
```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```

## Set Up a Python Virtual Environment
Create a directory for your AI project and set up a Python virtual environment within it:
```bash
mkdir ~/ai_hello_world
cd ~/ai_hello_world
python3 -m venv venv
source venv/bin/activate
```

For Windows run
```
source venv/Scripts/activate
```

### `python3 -m venv venv`

The command `python3 -m venv venv` is used to create a virtual environment in Python. Here's a breakdown of what each part of the command does:

- `python3`: This specifies that you are using Python 3 to run the command. It's the command used to invoke Python 3 specifically, ensuring that the virtual environment is created under Python 3 rather than any other installed version of Python.

- `-m venv`: The `-m` flag tells Python to run the library module `venv` as a script. The `venv` module is Python's standard library module used to create virtual environments. A virtual environment is an isolated environment that allows you to manage dependencies for a specific project without affecting other projects or the system-wide packages.

- `venv`: This is the name given to the directory where the virtual environment will be created. By convention, many developers name their virtual environment directory `venv` within their project directory, but you could name it anything you like. This directory will contain the Python executable files, and a copy of the `pip` library, which can be used to install other packages into the virtual environment.

When you run `python3 -m venv venv`, it performs the following actions:

1. Creates a directory named `venv` in your current working directory. This directory will serve as the root directory of the virtual environment.

2. Creates a subdirectory within `venv` named `lib` where it installs a local version of the Python library. This ensures that any Python packages you install while the virtual environment is active will be isolated from the system-wide Python library.

3. Adds a `bin` directory (or `Scripts` on Windows) inside `venv` that contains a local Python interpreter and a local version of `pip`. This allows you to install packages into the virtual environment using `pip` without affecting the system-wide Python environment.

4. Copies the Python executable to the virtual environment to ensure that the virtual environment can be activated without relying on the system-wide Python installation.

### `source venv/bin/activate`

To activate the virtual environment, you run a script located in the `venv/bin` directory (or `venv\Scripts` on Windows). On Unix or MacOS, you use `source venv/bin/activate`, and on Windows, you use `.\venv\Scripts\activate`. Once activated, any Python or pip commands you run will use the versions in the virtual environment, not the system-wide versions.

## Add venv folder to .gitignore

.gitignore
```
venv/
```

## Install TensorFlow or PyTorch
For a "Hello World" project in AI, you can use TensorFlow or PyTorch. These are two of the most popular frameworks for AI and machine learning. To install TensorFlow, run:
```bash
pip install tensorflow
```
Or for PyTorch, visit the PyTorch website to get the installation command specific to your setup.

## Write Your First AI Program
You can now create a simple AI program. For instance, you could write a Python script that uses TensorFlow or PyTorch to implement a basic neural network. A common "Hello World" equivalent in AI is training a model to recognize handwritten digits from the MNIST dataset.

Here’s an example to get you started, using TensorFlow to recognize handwritten digits. Create a file named `mnist_hello_world.py` and paste the following code:

```python
import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
```

## Run Your AI Program
Execute your script within your virtual environment:
```bash
python mnist_hello_world.py
```

This will train a basic neural network to classify handwritten digits using the MNIST dataset.
