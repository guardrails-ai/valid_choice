from guardrails import Guard
from pydantic import BaseModel, Field
from validator import ValidChoices


class ValidatorTestObject(BaseModel):
    test_val: str = Field(
        validators=[
            ValidChoices(choices=["choiceA", "choiceB"], on_fail="exception")
        ]
    )


TEST_OUTPUT = """
{
  "test_val": "choiceA"
}
"""


guard = Guard.from_pydantic(output_class=ValidatorTestObject)

raw_output, guarded_output, *rest = guard.parse(TEST_OUTPUT)

print("validated output: ", guarded_output)


TEST_FAIL_OUTPUT = """
{
"test_val": "b test value"
}
"""

try:
  guard.parse(TEST_FAIL_OUTPUT)
  print ("Failed to fail validation when it was supposed to")
except (Exception):
  print ('Successfully failed validation when it was supposed to')