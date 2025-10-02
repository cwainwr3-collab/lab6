from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(textstr: str, starti: int, endi: int, scorei: float):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text, 
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        ##text=input("text: "),
        text = textstr,
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=starti, end=endi, score=scorei)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    return (result)

if __name__ == "__main__": 
    anonymizer_ex = sample_run_anonymizer("My name is Bond.", 11, 15, .8)
    print(anonymizer_ex)
