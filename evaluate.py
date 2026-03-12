import json
from analyzer import analyze_logs


def evaluate():

    with open("dataset.json") as f:
        dataset = json.load(f)

    correct = 0
    total = len(dataset)

    for item in dataset:

        log_path = f"logs/{item['log_file']}"

        with open(log_path) as f:
            logs = f.read()

        result = analyze_logs(logs)

        predicted = result["failure_type"]
        expected = item["expected_failure_type"]
        synonyms = {
            "dependency conflict": "dependency_error",
            "image_pull_failure": "registry_error"
        }
        predicted = synonyms.get(predicted, predicted)
        print("Log:", item["log_file"])
        print("Expected:", expected)
        print("Predicted:", predicted)
        print()

        if predicted == expected:
            correct += 1

    accuracy = correct / total

    print("Model Accuracy:", accuracy)


if __name__ == "__main__":
    evaluate()