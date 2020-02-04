def cd_model():
  
  model = Sequential()
  model.add(Conv2D(32, (3,3),padding = 'same', input_shape=(200,200,3), activation='relu'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D(pool_size=(3, 3), strides=(2,2)))
    
  model.add(Conv2D(32, (3,3), padding = 'same', activation='relu'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D(pool_size=(3, 3), strides=(2,2)))
    
  model.add(Conv2D(64, (3,3),padding = 'same', activation='relu'))
  model.add(BatchNormalization())
  model.add(MaxPooling2D(pool_size=(3, 3), strides=(2,2)))
  model.add(Flatten())
  model.add(Dropout(0.5))

  model.add(Dense(128, activation = 'relu'))
  model.add(Dropout(0.5))
  model.add(Dense(1, activation = 'sigmoid'))

  return model