import os
import matplotlib.pyplot as plt

# Define a directory in Google Drive to save outputs
save_dir = os.path.join(train_data_path.split('MRI SCAN DATASET')[0], 'Model_Outputs')
os.makedirs(save_dir, exist_ok=True)

# 1. Save the trained Keras model
# Using the recommended native Keras format (.keras) instead of HDF5 (.h5)
model_save_path = os.path.join(save_dir, 'cnn_cancer_prediction_model.keras')
model.save(model_save_path)
print(f"Model saved to: {model_save_path}")

# 2. Save the plots (accuracy and loss) generated previously
# Re-generating plots to save them individually

# Plot training and validation accuracy
plt.figure(figsize=(8, 6))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
accuracy_plot_path = os.path.join(save_dir, 'accuracy_plot.png')
plt.savefig(accuracy_plot_path)
plt.close() # Close the plot to prevent it from displaying twice
print(f"Accuracy plot saved to: {accuracy_plot_path}")

# Plot training and validation loss
plt.figure(figsize=(8, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
loss_plot_path = os.path.join(save_dir, 'loss_plot.png')
plt.savefig(loss_plot_path)
plt.close() # Close the plot
print(f"Loss plot saved to: {loss_plot_path}")