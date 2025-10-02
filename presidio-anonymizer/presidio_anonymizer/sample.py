from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text : str, start : int, end : int):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text, 
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        ##text=input("text: "),
        text = text,
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=start, end=end)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    return (result)

if __name__ == "__main__": 
    anonymizer_ex = sample_run_anonymizer("My name is Bond.", 11, 15)
    print(anonymizer_ex)