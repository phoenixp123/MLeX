# How to use MLeX

## Installation
To install, open your terminal and input the following:

``pip install mlex-python``

Then import the library to your project:

```
from MLeX.trial import Trial
from MLeX.experiment import Experiment
```

## Usage
MLeX is used to record and save a Keras model's metadata and
performance after training.

First, train your model:

```
history = model.fit(X_train_tr, y_train_tr, epochs=50,
                    validation_data=(X_valid_tr, y_valid_tr),
                    callbacks=[checkpoint_cb, early_stopping_cb, tensorboard_cb])
```

Then, declare an `Experiment` object:

```
experiment_1 = Experiment(id=0)
```

This will be used to store subsequent `Trial` objects and their
associated data.

Next, declare your first `Trial`:
```
trial_0 = Trial(history=history)
```

The `Trial` takes a Keras `History` object as its argument,
which is returned by calling `model.fit(....)`.

You can save an individual `Trial` via the following:
```
trial_0.save(path={optional path to directory, defaults to current directory})
```

Also, you can add `Trial`(s) to the `Experiment`:
```
# Add two Trials to the Experiment

experiment_1.add_trial(trial_0)
experiment_1.add_trial(trial_1)
```

From there you can save them as a batch:
```
experiment_1.save_trials()
```


