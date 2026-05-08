# Train the model
history = model.fit(
    train_generator,
    epochs=15, # You can adjust the number of epochs
    validation_data=test_generator
)