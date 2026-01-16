
## Working with Variables
- **Variables** store values for later use and are created using the assignment operator `=`.
- Variable names (identifiers) are case-sensitive and may contain letters, digits, and underscores, but cannot start with a digit.
- **Augmented assignment** (e.g. `+=`, `-=`, `*=`, `/=`) is a shorthand for updating a variable using its current value.

## Data Types
- Common Python data types:
  - **int** – whole numbers (e.g. `10`)
  - **float** – decimal numbers (e.g. `10.5`)
  - **bool** – `True` or `False`
  - **str** – text values (e.g. `"Hello"`)
- Python uses **dynamic typing**, meaning a variable’s type can change depending on the value assigned.
- The `type()` function shows the data type of a value or variable.
- Operators behave differently depending on data type (e.g. `+` adds numbers but concatenates strings).

## Built-in Functions
- **Functions** are pre-written pieces of code that perform common tasks.
- Examples:
  - `print()` – displays output
  - `type()` – returns the data type
  - `len()` – returns the length of a string or list
  - `input()` – gets user input (always returns a string)
- Use type conversion functions like `int()` to convert input strings to numbers.

## Quotes and Strings
- Strings can use **single** (`'`), **double** (`"`), or **triple** (`"""`) quotes.
- **Escape sequences** allow special characters in strings (e.g. `\n`, `\t`, `\\`).
- **Triple-quoted strings** are useful for multi-line text without escape sequences.

## Indexing and Slicing
- **Indexing** accesses a single character/value using square brackets (e.g. `name[0]`).
- Indexing starts at `0`; negative indices count from the end.
- **Slicing** accesses a range of values using `[start:end]`.
  - Start index is inclusive, end index is exclusive.
  - Omitting start or end uses default values.

## Lists
- **Lists** store ordered collections of values inside square brackets `[]`.
- Lists can contain multiple values and support indexing, slicing, `+`, and `*`.
- Lists are **mutable**, meaning their contents can be changed after creation.
- Values can be added using slicing, `append()`, or `+=`.

## Mutable vs Immutable
- **Mutable**: Can be changed after creation (e.g. lists).
- **Immutable**: Cannot be changed after creation (e.g. strings).

## Key Terminology (Quick Definitions)
- **Assignment**: Storing a value in a variable using `=`.
- **Data-type**: The kind of value stored (e.g. int, float, string).
- **Argument**: A value passed into a function.
- **Indexing**: Accessing a single element in a sequence.
- **Slicing**: Accessing a range of elements in a sequence.
- **Mutable**: Can be modified after creation.
- **Immutable**: Cannot be modified after creation.
