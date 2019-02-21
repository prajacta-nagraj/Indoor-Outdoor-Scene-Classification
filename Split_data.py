#use python 3.6+
#pip install split_folders
#python module to split image folder to train,test and split data
import split_folders
split_folders.ratio('/home/prajacta/yt8m/youtube-8m-videos-frames/input/', output='/home/prajacta/yt8m/youtube-8m-videos-frames/', seed=1337, ratio=(.8, .1, .1))
