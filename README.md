# Red or Blue

A super simple Neural Network which performs binary prediction in order to predict if a dot on a plot chart is a blue dot or at red cross.

## Prerequisites

[Anaconda](https://www.anaconda.com/distribution/)


## How to run

Since this neural network is so simple and will only run 50 epochs everything is located in index.py (training, testing, and result) simply run it with:

`python index.py`

To view the testing data (random generated) you can run the script with the option -showTrainingData true

`python index.py -showTrainingData true`

![training data](https://raw.githubusercontent.com/JohanG2012/red-or-blue/master/meta/images/training_data.png)

The script will generate a full grid of data points as testing data. To view the testing data run the script with the option -showTestingData true

`python index.py -showTestingData true`

![testing data](https://raw.githubusercontent.com/JohanG2012/red-or-blue/master/meta/images/test_data.png)

To visualize the test result the dots will change size according to their probability to be a red cross. To view this run the script with the option -showTestingResult true

`python index.py -showTestingResult true`

![testing result](https://raw.githubusercontent.com/JohanG2012/red-or-blue/master/meta/images/test_result.png)

To visulaize the result the original plot chart is divided into two areas to show where dots would be classified as a red cross. To show this run the script with the option -showResult true

`python index.py -showResult true`

![result](https://raw.githubusercontent.com/JohanG2012/red-or-blue/master/meta/images/result.png)

