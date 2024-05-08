import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import utils

train_dir = './dataset/train'
test_dir = './dataset/test'
valid_dir = './dataset/valid'
batch_size=20
nb_train_samples = 1000
nb_validation_samples = 100
nb_test_samples=100

def main():
    model = getModel()

    # Отображение изменения размеров карт признаков с каждым последующим слоем
    print(model.summary())
    train_generator = convertImagesToTensorsTrain()


    validation_generator = convertImagesToTensorsValidation()

    history = trainModel(model, train_generator, validation_generator)

    test_generator = convertImagedToTensorsTest()
    model.save('model.h5')
    plotLossAndAccuracy(history)

    scores = model.evaluate(test_generator,verbose =2 ,batch_size = nb_test_samples//batch_size)
    print("Точность на тестовых данных: %.2f%%"%(scores[1]*100))




    # Если при построении графиков наблюдается эффект переобучения
    # Выполнить одно из действий: 1.Прореживание и сокращений весов (L2-регуляризация) 2.Расширение данных


def getModel():
    model = models.Sequential()

    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(255, 255, 3)))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Conv2D(200, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(200, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Flatten())
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(18, activation='softmax'))

    model.compile(loss= categorical_crossentropy,
                  optimizer= 'adam',
                  metrics=['acc'])

    return model


def convertImagesToTensorsTrain():
    train_datagen = ImageDataGenerator(rescale=1. / 255)
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(255, 255),
        batch_size=batch_size,
        class_mode= 'categorical'
    )
    return train_generator

def convertImagedToTensorsTest():
    test_datagen = ImageDataGenerator(rescale=1./ 255)
    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(255,255),
        batch_size=batch_size,
        class_mode='categorical'
    )
    return test_generator

def convertImagesToTensorsValidation():
    validation_datagen = ImageDataGenerator(rescale=1. / 255)
    validation_generator = validation_datagen.flow_from_directory(
        valid_dir,
        target_size=(255, 255),
        batch_size=batch_size,
        class_mode='categorical'
    )
    return validation_generator


def trainModel(model, validation, train):

    return model.fit(
        train,
        steps_per_epoch=nb_train_samples//batch_size,
        epochs=40,
        validation_data=validation,
        validation_steps=nb_validation_samples//batch_size
    )


def plotLossAndAccuracy(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)
    plt.plot(epochs, acc, 'bo', label='Точность на этапе обучения')
    plt.plot(epochs, val_acc, 'b', label='Точность на этапе проверки')
    plt.title('Точность на этапе обучения и проверки')
    plt.xlabel('Эпохи')
    plt.ylabel('Точность')
    plt.legend()
    plt.savefig('one.png')
    plt.figure()

    epochs = range(1, len(loss) + 1)
    plt.plot(epochs, loss, 'bo', label='Потери на этапе обучения')
    plt.plot(epochs, val_loss, 'b', label='Потери на этапе проверки')
    plt.title('Потери на этапе обучения и проверки')
    plt.xlabel('Эпохи')
    plt.ylabel('Потери')
    plt.legend()
    plt.savefig('two.png')
    plt.figure()


main()

