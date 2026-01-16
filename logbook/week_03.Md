S## Boolean Expressions
- Evaluate to `True` or `False`.
- Use **relational operators**: `<, >, <=, >=, ==, !=`.
- Can compare numbers, strings (alphabetically), and lists.
- Data types must be compatible; mismatched types may cause errors or unexpected results.
- **Logical operators**:
  - `and` → True if both conditions True
  - `or` → True if either condition True
  - `not` → Inverts Boolean value
- **Chaining operators** allows compact expressions, e.g., `18 < age <= 65`.

## Membership Testing
- `in` → True if value exists in list or string.
- `not in` → True if value does not exist.
- Useful for sequences and substring checks.

## If Statements
- Syntax:
  ```python
  if condition:
      # code block
  elif condition2:
      # code block
  else:
      # code block
