# Drills

1. Write a pure function `normalize_numbers(xs: list[int]) -> list[int]` that:
   - Removes negative numbers
   - Sorts the remaining values
   - Returns a new list (no mutation)

2. Write a second operator `summarize(xs: list[int]) -> dict[str, int]` returning:
   - count
   - min
   - max
   - sum

3. Verify purity:
   - Call the functions twice with the same input
   - Assert the outputs are identical
   - Confirm the input list is unchanged
