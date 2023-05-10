import matplotlib.pyplot as plt
from datetime import datetime
import json

def get_trial_time():
    """
    If the `trial` param is left empty in the Trial class,
    then the current date and time are used as a stand-in.

    :return: String in the format YYYY-MM-DD_Hour:Min:Sec
    """
    temp = str(datetime.now()) \
        .split(" ")
    temp1 = temp[0]
    temp2 = temp[1] \
        .split(".")[0]

    time = temp1 + "_" + temp2

    return time

def get_model_history(model_history):
    """
    Helper function to parse out

    :param model_history: Keras History object
    :return: four float values
    """
    loss = model_history['loss']
    acc = model_history['accuracy']
    val_loss = model_history['val_loss']
    val_accuracy = model_history['val_accuracy']

    return loss, acc, val_loss, val_accuracy

class Trial:
    framework = "keras"

    def __init__(self,id=None,experiment=None,history=None):
        """
        An object that tracks the performance metrics and model configuration during a
        training run of a Keras model.

        :param trial: A string representing the label of the model's trial run,
                      default value is current date and time.
        :param experiment: The string of the trial's experiment stack,
                            default value is None.
        :param history: A History object. Its History.history attribute is a record of training loss
                        values and metrics values at successive epochs.
        """

        self.id = id
        self.experiment = experiment
        self.history = history



    # TODO: Set up configurable files - for example, only save metrics or only save configuration
    def save(self, path=None):
        """
        This method will save a .json file that represents a training run of a Keras model.

        :param path: A string which is the path to which trial data is saved.
        :return: None, saves .json file
        """
        # Here are attributes that should be saved
        # history.history
        # history.params
        # history.model.get_config()
        # model.to_json()

        trial_data = {
            "trial_id": str(self.id),
            "experiment_id": str(self.experiment),
            "configuration": self.history.model.get_config(),
            "history": self.history.history,
            "params": self.history.params,
            "summary": {
                "loss": self.history.history["loss"][-1],
                "accuracy": self.history.history["accuracy"][-1],
                "val_loss": self.history.history["val_loss"][-1],
                "val_accuracy": self.history.history["val_accuracy"][-1],
            }
        }


        if not path:
            path = "trial:" + str(self.id) + "_experiment:"  + str(self.experiment)


        print(f"Saving file as {path}.json...")

        try:
            with open(f"{path}.json", "w") as outfile:
                json.dump(trial_data, outfile, indent = 4)
            print("Saved Successfully.")
        except:
            print("An error occurred, try again.")


    def plot(self, save=False, path=None):
        """
        Displays two plots of loss and accuracy metrics (including validation) values,
        the plots can optionally be saved to a .png file.

        :param save: Optional parameter that will save the plot of loss/accuracy to a .png file
        :param path: Path to save .png of file to. Default value is Trial and Experiment labels separated by underscore
        :return:
        """
        loss, acc, val_loss, val_accuracy = get_model_history(self.history.history)

        epochs = range(1, len(acc) + 1)
        plt.plot(epochs,acc,'bo',label = 'Training acc')
        plt.plot(epochs,val_accuracy,'b',label = 'Validation acc')
        plt.title('Training and validation accuracy')
        plt.legend()

        plt.figure()

        plt.plot(epochs,loss,'bo',label = 'Training loss')
        plt.plot(epochs,val_loss,'b',label = 'Validation loss')
        plt.title('Training and validation loss')
        plt.legend()

        plt.show()

        if save:
            if path:
                plt.savefig(path)
            else:
                plt.savefig(self.id + "_" + self.experiment)



    # TODO: Add more detailed toString - for example, include Trial config info
    def __str__(self):
        """
        Prints out a very simple representation of the Trial - Experiment pair for a given trial.

        :return: String in the format `trial: %d, experiment: %d`
        """
        model_summary = str({
            "trial": str(self.id),
            "experiment": str(self.experiment),
            "summary": {
                    "loss": self.history.history["loss"][-1],
                    "accuracy": self.history.history["accuracy"][-1],
                    "val_loss": self.history.history["val_loss"][-1],
                    "val_accuracy": self.history.history["val_accuracy"][-1],
            }
        })

        return model_summary


if __name__ == "__main__":
    trial_0 = Trial()

    print(trial_0)
    print(trial_0.experiment, trial_0.id)
   #  print("_".join(str(datetime.now()).split(" ")))