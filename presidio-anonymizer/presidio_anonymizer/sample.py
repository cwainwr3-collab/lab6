from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(textstr: str, starti: int, endi: int):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text, 
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        ##text=input("text: "),
        text = textstr,
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=starti, end=endi, score=0.8)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    # this print is being changed to return a proper testable value
    # print(result)

    # input should be:
    # text: My name is Bond.
    # start: 11
    # end: 15
    # 
    # output should be:
    # text: My name is BIP.
    # items:
    # [
    #     {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
    # ]

    return (result)

if __name__ == "__main__": 
    anonymizer_ex = sample_run_anonymizer("My name is Bond.", 11, 15)
    print(anonymizer_ex)
