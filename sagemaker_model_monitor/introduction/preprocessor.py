import json
import secrets


# sample preprocess_handler (to be implemented by customer)
# This is a trivial example, where we simply generate random values
# But customers can read the data from inference_record and trasnform it into
# a flattened json structure
def preprocess_handler(inference_record):
    event_data = inference_record.event_data
    input_data = {}
    output_data = {}

    input_data["feature0"] = secrets.SystemRandom().randint(1, 3)
    input_data["feature1"] = secrets.SystemRandom().uniform(0, 1.6)
    input_data["feature2"] = secrets.SystemRandom().uniform(0, 1.6)

    output_data["prediction0"] = secrets.SystemRandom().uniform(1, 30)

    return {**input_data, **output_data}
