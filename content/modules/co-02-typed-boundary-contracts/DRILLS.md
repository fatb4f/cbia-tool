# Drills

1. Define a `TypedDict` representing a configuration object with:
   - input_path: str
   - output_path: str
   - strict: bool

2. Write a boundary function that:
   - Accepts `dict[str, object]`
   - Validates required keys and types
   - Returns the typed configuration

3. Write one test that proves invalid input is rejected.
