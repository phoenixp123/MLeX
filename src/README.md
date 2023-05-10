# How to use MLeX

## Installation
To install, open your terminal and input the following:

``pip install mlex-python``

## Usage
MLeX is used to record and save a Keras model's metadata and
performance after training.

First, train your model:

```
history = model.fit(X_train_tr, y_train_tr, epochs=50,
                    validation_data=(X_valid_tr, y_valid_tr),
                    callbacks=[checkpoint_cb, early_stopping_cb, tensorboard_cb])
```

Then, declare a `Trial` object
TBD
