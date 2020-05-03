################################################################
# Variable definitions required for CNN graph
################################################################
#Interpolation type and up scaling factor
#L: make this 1, same was that JB interpolates
interp_val=1 # 0 - bilinear interpolation; 1- nearest neighbour interpolation; 2- Bicubic Interpolation
################################################################

################################################################
# data dimensions, num of classes and resolution
################################################################
# Image Dimensions
img_size_x = 16 
img_size_y = 16
# Images are stored in one-dimensional arrays of this length.
img_size_flat = img_size_x * img_size_y
# Number of colour channels for the images: 1 channel for gray-scale image.
#L: set to 16
num_channels = 16
# Number of classes : # 0-background, 1-rv, 2-myo, 3-lv
num_classes=2 
size=(img_size_x,img_size_y)
target_resolution=(1.36719,1.36719)
################################################################
# data paths
################################################################
#validation_update_step to save values
val_step_update=10
#base dir of network
base_dir='data_aug_seg'
#data path tr
data_path_tr='data/gan_processed_data'
#cropped imgs data_path
data_path_tr_cropped='data/gan_processed_data'
################################################################

################################################################
#network optimization parameters
################################################################
# P: disable data augmentation
aug_en=0
#batch_size
batch_size=20
#L: only have one structure, tree/no tree, changed accordingly
struct_name=['tree']

#check