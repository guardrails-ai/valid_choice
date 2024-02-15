# ValidChoice

# Overview

| Developed by | Guardrails AI |
| --- | --- |
| Date of development | Feb 15, 2024 |
| Validator type | Format |
| Blog |  |
| License | Apache 2 |
| Input/Output | Output |

# Description

This validator enforces that an LLM generated output belongs to a subset of acceptable choices.

# Installation

```bash
$ guardrails hub install hub://guardrails/valid-choice
```

# Usage Examples

## Validating string output via Python

In this example, we’ll use the validator to check if the output belongs to a a list of allowed pet types: `cat, dog, bird`.

```python
# Import Guard and Validator
from guardrails.hub import ValidChoices
from guardrails import Guard

# Initialize Validator
val = ValidChoices(
		choices=['cat', 'dog', 'bird'],
		on_fail="fix"
)

# Setup Guard
guard = Guard.from_string(
    validators=[val, ...],
)

guard.parse("dog")  # Validator passes
guard.parse("horse")  # Validator fails
```

## Validating JSON output via Python

We can use the same validator to confirm that a field in a JSON output belongs to a set of categories. Same as before, we will use the validator to check for allowed pet types: `cat, dog, bird`.

```python
# Import Guard and Validator
from pydantic import BaseModel
from guardrails.hub import ValidChoices
from guardrails import Guard

val = ValidChoices(
		choices=['cat', 'dog', 'bird'],
		on_fail="fix"
)

# Create Pydantic BaseModel
class PetInfo(BaseModel):
		pet_name: str
		pet_type: str = Field(
				description="Type of pet", validators=[val]
		)

# Create a Guard to check for valid Pydantic output
guard = Guard.from_pydantic(output_class=PetInfo)

# Run LLM output generating JSON through guard
guard.parse("""
{
		"pet_name": "Caesar",
		"pet_type": "dog"
}
""")
```

## Validating string output via RAIL

tbd

## Validating JSON output via RAIL

tbd

# API Reference

`__init__`

- `choices`: List of items that depict valid set of choices
- `on_fail`: The policy to enact when a validator fails.