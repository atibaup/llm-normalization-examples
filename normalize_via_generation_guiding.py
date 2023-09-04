import os

from pydantic import BaseModel, Field
from jsonformer import Jsonformer
from transformers import AutoModelForCausalLM, AutoTokenizer

class NormalizedData(BaseModel):
    name: str = Field(..., description="The name of the person")
    age: int = Field(..., description="The age of the person")
    address: str = Field(..., description="The address of the person")


def normalize(input: str) -> NormalizedData:
    normalized_data_fields = NormalizedData.model_fields.keys()
    model_id = "databricks/dolly-v2-3b"
    model = AutoModelForCausalLM.from_pretrained(model_id)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    schema = NormalizedData.model_json_schema(by_alias=False)
    prompt = "Generate a person's information based on the following schema:"
    jsonformer = Jsonformer(model, tokenizer, schema, prompt)
    generated_data = jsonformer()
    print(generated_data)
    normalized_parameters = NormalizedData.model_validate_json(generated_data)
    return normalized_parameters


if __name__ == '__main__':
    #
    # Example usage
    # > python normalize_via_function_call.py "I was born 25 years ago in Kingston Ave, Brooklyn, NY, where I still live. My name is Patrick"
    import sys
    normalized = normalize(sys.argv[0])
    print(normalized)

