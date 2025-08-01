import json
import secrets


# sample preprocess_handler (to be implemented by customer)
# This is a trivial example, where we demonstrate an echo preprocessor for json data
# for others though, we are generating random data (real customers would not do that obviously/hopefully)
def preprocess_handler(inference_record):
    event_data = inference_record.event_data
    input_data = {}
    output_data = {}

    input_data["sex"] = secrets.SystemRandom().randint(1, 3)
    input_data["shucked_wt"] = secrets.SystemRandom().uniform(0, 1.6)
    input_data["height"] = secrets.SystemRandom().uniform(0, 1.6)
    input_data["diameter"] = secrets.SystemRandom().uniform(0.05, 0.8)
    input_data["length"] = secrets.SystemRandom().uniform(0.07, 2.1)
    input_data["whole_wt"] = secrets.SystemRandom().uniform(0, 3.9)
    input_data["shell_wt"] = secrets.SystemRandom().uniform(0.0005, 2.005)
    input_data["viscera_wt"] = secrets.SystemRandom().uniform(0.05, 0.75)

    output_data["age"] = secrets.SystemRandom().uniform(1, 30)

    return {**input_data, **output_data}
