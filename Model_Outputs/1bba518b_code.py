import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define image dimensions and batch size
IMG_WIDTH = 224
IMG_HEIGHT = 224
BATCH_SIZE = 32
NUM_CLASSES = 4 # Based on the folder names: notumor, meningioma, pituitary, glioma

# Data Augmentation and Rescaling for Training Data
train_datagen = ImageDataGenerator(
    rescale=1./255, # Normalize pixel values to [0, 1]
    rotation_range=20, # Rotate images by up to 20 degrees
    width_shift_range=0.2, # Shift images horizontally by up to 20% of the width
    height_shift_range=0.2, # Shift images vertically by up to 20% of the height
    shear_range=0.2, # Apply shear transformations
    zoom_range=0.2, # Zoom into images
    horizontal_flip=True, # Flip images horizontally
    fill_mode='nearest' # Fill new pixels created by transformations
)

# Rescaling only for Validation/Testing Data (no augmentation)
test_datagen = ImageDataGenerator(rescale=1./255)

# Create data generators
train_generator = train_datagen.flow_from_directory(
    train_data_path,
    target_size=(IMG_WIDTH, IMG_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode='categorical' # For multi-class classification
)

test_generator = test_datagen.flow_from_directory(
    test_data_path,
    target_size=(IMG_WIDTH, IMG_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode='categorical' # For multi-class classification
)

print(f"Found {train_generator.num_classes} classes: {train_generator.class_indices}")
print(f"Number of training samples: {train_generator.samples}")
print(f"Number of testing samples: {test_generator.samples}")