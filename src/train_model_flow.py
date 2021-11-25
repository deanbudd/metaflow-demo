from metaflow import FlowSpec, step


class TrainModelFlow(FlowSpec):
    @step
    def start(self):
        print("TrainModelFlow is starting.")
        self.next(self.train_model)

    @step
    def train_model(self):
        from metaflow import Flow, Run, get_metadata

        run = Run('TrainingDataFlow/1637880995054996')
        train_model_with(run.data.training_data)

        run = Flow('TrainingDataFlow').latest_successful_run
        self.model = train_model_with(run.data.training_data)

        self.next(self.end)

    @step
    def end(self):
        print("TrainModelFlow is all done.")


def train_model_with(training_data):
    print("TrainModelFlow is training with..." + training_data)
    return "model"


if __name__ == '__main__':
    TrainModelFlow()
