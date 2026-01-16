
## Lists and List Methods
- **List**: Ordered, mutable, iterable collection: `squares = [4,9,16,25]`
- **Mutator methods** (change list):
  - `append(value)` → add single item
  - `extend([values])` → add multiple items
  - `insert(index, value)` → insert at position
  - `remove(value)` → remove first occurrence
  - `pop([index])` → remove and return element (default last)
  - `clear()` → empty the list
  - `sort(key=None, reverse=False)` → sort in-place
  - `reverse()` → reverse order
- **Accessor methods** (do not change list):
  - `index(value, start=0, end=len(list))` → find element index
  - `count(value)` → count occurrences
  - `copy()` → shallow copy of list

- **Built-in functions**:
  - `len(list)` → list length
  - `sorted(list, key=None, reverse=False)` → returns sorted copy

- **Notes**:
  - `del list[index]` → delete element or slice
  - `del list` → delete entire list variable

---

## List Comprehensions
- Concise way to create lists:
  ```python
  squares = [x*x for x in range(10)]
  cubes = [x**3 for x in range(2, 21)]
  even_nums = [n for n in range(100,201) if n%2==0]
