import os

# from Lab6.MLeX.trial import Trial

class Experiment:
    def __init__(self, id):
        """
        Initializes an Experiment object which tracks a series of Trials and provides
        additional functionality by allowing for operations on multiple Trials.

        :param id: Integer that is used to track each experiment.
        """
        self.id = id
        self.trials = {}

    def add_trial(self, trial):
        """
        Appends a Trial object to the list of Trials

        :param trial: A Trial object
        :return: None
        """
        trial.id = len(self.trials)
        trial.experiment = self.id
        self.trials[trial.id] = trial

    def delete_trials(self):
        self.trials = {}

    # TODO: Summarize trials results
    def get_trials(self, print_trials=False):
        """
        Returns a list of Trials contained in the Experiment. If print_trials is set to True then
        each Trial is printed in the order they were added.

        :param print_trials: A boolean which if set to true, prints a summary of each trial
                            contained in the experiment.
        :return: list of Trials
        """
        if print_trials:
            for id in self.trials.keys(): print(self.trials[id])

        return self.trials

    # TODO: Support rapid search for best trial results
    def get_trial_by_id(self,trial_id):
        """
        Returns a specific trial based on its ID.

        :param trial_id: the name of the trial to be found.
        :return: Trial object
        """
        for id in self.trials.keys():
            if id == trial_id:
                return self.trials[id]
        return None

    def save_trials(self):
        """
        Saves all Trials in an Experiment into a separate directory.

        :return: None
        """
        current_directory = f"experiment-{self.id}-trials"
        try:
            os.makedirs(current_directory, exist_ok = True)
        except:
            print(f"An error occurred while trying to save experiment: {self.id} in {current_directory}")

        for id in self.trials.keys():
            trial = self.trials[id]
            path_var = "trial:" + str(trial.id) + "_experiment:" + str(self.id)
            trial.save(path =current_directory + "/" + path_var)

    def __str__(self):
        return "Experiment(name={})".format(self.id)

if __name__ == "__main__":
    pass
