# Indoor-Outdoor-Scene-Classification
One of the application of image classification is to cclassify scenes and recognize them according to category.
It's use can be ranged from autonomous vehicle navigation to video games.

## Dependencies
- ffmpeg
- Python
- Keras(Tensorflow Backend)

## Data Handling
To start with the challenge first thing to do is prepare a neat data library with the given classes as outdoor and indoor. 
Data was taken from Youtube-8m dataset, at first videos were parsed categorically (Ref-https://github.com/gsssrao/youtube-8m-videos-frames)
then frames were extracted using ffmpeg.Finally the data was split into train, test and validation sets.

### Usage
- Save the videos categorically in folders indoor and outdoor respectively. Go to each folder and run the Frames bash file with first argument as path and second as number of frames per second.
- Use Split_data.py file with path to input and output folders.

## Training
After the data is prepared, I used CNN to classify images and train the model. 
Using Image data generator to augment the data and convert image size to 64*64. It neatly takes in the data according to classes. Following model is used to train and validate the images:

![Alt text](https://github.com/prajacta-nagraj/Indoor-Outdoor-Scene-Classification/blob/master/modelcnn.png?raw=true "Model")


After trial/error and using early stopping method overfitting was reduced and the model showed accuracy of 80% for test data.

![Alt text](https://github.com/prajacta-nagraj/Indoor-Outdoor-Scene-Classification/blob/master/Graphs.png?raw=true "Accuracy")


## Image Classification 
To finally test the image run Scene-Classification.py file and provide the test image name when prompted.( test image should be in the current directory with othe saved model).


