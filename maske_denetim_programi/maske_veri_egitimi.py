import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import keras_tuner as kt
import os


img_height, img_width = 128, 128
batch_size = 32
data_dir = r"C:\Users\acer\Desktop\maske_kontrol"

image_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    horizontal_flip=True,
    zoom_range=0.1,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
)

train_generator = image_datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    class_mode="categorical",
    subset="training",
    shuffle=True
)
val_generator = image_datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    class_mode="categorical",
    subset="validation",
    shuffle=False
)
num_class = len(train_generator.class_indices)

def build_model(hp):
    inputs = Input(shape=(img_height, img_width, 3))


    x = inputs
    for i in range(hp.Int("conv_blocks", 2, 4, step=1)):
        x = Conv2D(
            filters=hp.Choice(f"filters_{i}", [32, 64, 128, 256]),
            kernel_size=(3, 3),
            activation="relu"
        )(x)
        x = MaxPooling2D(pool_size=(2, 2))(x)

    x = Flatten()(x)


    x = Dense(hp.Choice("dense_units", [64, 128, 256]), activation="relu")(x)


    x = Dropout(hp.Float("dropout", 0.3, 0.7, step=0.1))(x)

    outputs = Dense(num_class, activation="softmax")(x)

    model = Model(inputs=inputs, outputs=outputs)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=hp.Choice("lr", [1e-2, 1e-3, 1e-4])
        ),
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

tuner = kt.RandomSearch(
    build_model,
    objective="val_accuracy",
    max_trials=10,  # Toplam deneme sayısı
    executions_per_trial=1,
    directory="keras_tuner_results",
    project_name="cnn_tuning"
)

callbacks = [
    EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),
    ModelCheckpoint("best_model.keras", monitor='val_loss', save_best_only=True)
]

tuner.search(
    train_generator,
    validation_data=val_generator,
    epochs=15,
    callbacks=callbacks
)

best_model = tuner.get_best_models(num_models=1)[0]
best_model.save(r"C:\Users\acer\Desktop\maske_kontrol\best_model_maske.keras")
best_hp = tuner.get_best_hyperparameters(1)[0]
print("En iyi hiperparametreler:", best_hp.values)
