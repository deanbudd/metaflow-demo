from metaflow import FlowSpec, step, namespace


class TrainingDataFlow(FlowSpec):

    @step
    def start(self):

        print("TrainingDataFlow is starting.")
        self.next(self.make_training_data)

    @step
    def make_training_data(self):
        namespace('xyz_features')
        print("TrainingDataFlow is making training data...")
        self.training_data = "latest latest dataset"
        self.next(self.end)

    @step
    def end(self):
        print("TrainingDataFlow is all done.")


if __name__ == '__main__':
    TrainingDataFlow()
