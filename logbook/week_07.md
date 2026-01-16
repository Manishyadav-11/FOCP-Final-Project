# Introduction to Programming
## Lab Worksheet
### Week 7

Prior to attempting this lab tutorial ensure you have read the related lecture notes and/or viewed the lecture videos on MyBeckett. Once you have completed this lab you can attempt the associated exercises.

You can download this file in Word format if you want to make notes in it.

You can complete this work using the Python interpreter in interactive mode. This could be inside an IDE, or just a command prompt.

## Topics covered:

- Introducing Sets
- Set Comprehensions
- Mutable and immutable Sets
- Set Operators and Methods
- Introduction Dictionaries
- Creating Dictionaries
- Working with Dictionaries

---

For more information about the module delivery, assessment and feedback please refer to the module within the MyBeckett portal.

---

©2021 Mark Dixon  
Modified 2021 Tony Jenkins

---

## Introducing Sets

The Set data-type is in many ways similar to a List and Tuple, except the contained values are not ordered and no duplicates are allowed. Also a set can only contain immutable values, which means that, for example, a set cannot contain list type values. A regular set is itself mutable however, so it can be changed after it has been created.

Since sets are not ordered, they do not support indexing, slicing or any method based on an element's position. However, they do have support for traditional mathematical style set operations such as union, intersection and difference.

Sets are very efficient at performing membership testing type operations, and much faster than Lists at this type of operation, especially when there are a large number of stored values. These sorts of differences explain why there are several similar data types available; the trick is often to pick whichever is best suited for some application.

The Set type is built directly into the Python language hence there is a specific syntax associated with creation and manipulation. So to create a Set directly, braces (curley brackets) can be used -

```python
vowels = {"a", "e", "i", "o", "u"}
```

Remember ordering is not necessarily maintained and duplicate values are not allowed.

**TASK:** Try creating a set by entering the code below. Then use the `print()` function to display the contents of the set. Notice how the output varies from the entered values.

```python
names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
```

A set can also be created by calling the `set()` constructor. A constructor is similar to a function, but is used to initialise an object based on the named type. However this constructor takes only a single parameter, which is iterated to extract the contents of the set. So to create the above set using the `set()` constructor the following code could be used:

```python
names = set(["John", "Eric", "Terry", "Michael", "Graham", "Terry"])
```

Notice how a List was created (using `[ ]`) and then passed as a single parameter. If multiple parameters had been passed then an error would have been reported. Try entering the following and see the result -

```python
names = set("John", "Eric", "Terry", "Michael", "Graham", "Terry")
```

Creating a set using the constructor is convenient if the values already exist in some other iterable value, such as a List or Tuple. It is even possible to create a set of individual characters by passing a string type value. This means that the following statements both create the exactly the same set:

```python
hex_letters = {"a", "b", "c", "d", "e", "f"}

hex_letters = set("abcdef")
```

Finally an empty set must be created using the `set()` constructor rather than empty braces `{ }`, since the latter creates an empty dictionary (see later).

### Set Comprehensions

The contents of a set can be created using a set comprehension, in the same way that a list comprehension can be used to create a list. In fact they work in exactly the same way, but appear between braces `{ }` rather than square brackets `[ ]`.

As with list comprehensions, the contents are created by evaluating an expression usually while iterating over a loop. For example, by using a set comprehension it is fairly easy to create a set which contains all the letters that appear within a specific sentence at least once. This uses the "uniqueness" property of Sets.

**TASK:** Enter the code below, then make a call to the `print()` function to display the contents of the set.

```python
sentence = "this is a sentence containing some letters"
unique_letters = {x for x in sentence}
```

Remember that duplicates are not allowed, so each letter will appear in the set at most once. Also notice how a whitespace character has been included into the produced set.

Set comprehensions can also restrict the included values, by appending an `if` statement. So to create the same as the above, while excluding whitespaces the following variation could be used:

```python
unique_letters = {x for x in sentence if x != " "}
```

### Set Operations

One of the most common operations performed on a set is membership testing. This is done using either the `in` or `not in` operators. These check whether a specific element is either present, or not present, within a given set. For example:

```python
name = input("Enter your name: ")
if name in names:
    print("You are listed in the set of known names")
```

Even sets containing many thousands of elements can be checked almost instantly.

**TASK:** Rewrite the previous code so that it checks that the input name is NOT within the set of known names. Hint: use the `not in` operator.

Since a set type represents an existing well known concept, a mathematical set, there are certain operations that can be performed using both methods and operators. Since sets are mutable, both accessor and mutator type operations exist. It is also possible to perform special comparison type operations on sets.

The typical mathematical style operations that can be performed include union, intersection, difference, and symmetric difference.

The operators used to support these are as follows -

- `|` - union (the symbol is a "pipe", usually found to the left of the Z key)
- `&` - intersection
- `-` - difference
- `^` - symmetric difference

Each of these can also be achieved by calling an equivalent method. Fortunately the method names closely reflect the mathematical operation, and the methods are called `union()`, `intersection()`, `difference()` and `symmetric_difference()`.

**TASK:** Use the built-in `help()` function to view all the methods available on the set type.

If we assume we have the following sets:

```python
staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}
```

We could use the union operator `|` to add to the members of a set:

```python
>>> staff = staff | {"Mark", "Ringo"}
>>> print(staff)

{'Kelly', 'Paul', 'Jon', 'Sally', 'Ringo', 'Pete', 'Mark', 'Sue'}
```

We could use the intersection operator `&` to find only common elements:

```python
>>> staff_directors = staff & directors
>>> print(staff_directors)

{'Kelly', 'Jon'}
```

We could use the difference operator `-` to find elements in one set, but not the other:

```python
>>> external = directors - staff
>>> print(external)

{'Cyril', 'Rupert'}
```

We could use the symmetric difference operator `^` to find elements in either set, but not in both:

```python
>>> staff_or_external = directors ^ staff
>>> print(staff_or_external)

{'Cyril', 'Paul', 'Sally', 'Pete', 'Rupert', 'Sue', 'Ringo', 'Mark'}
```

**TASK:** Create the two initial sets, `staff` and `directors` as shown in the first example above. Perform the four mathematical set operations shown, but use the equivalent method calls to achieve the same results. For example:

```python
staff = staff | {"Mark", "Ringo"}

# becomes …

staff = staff.union({"Mark", "Ringo"})
```

The set operations we have seen so far have all been accessor type methods; they do not directly change the set to which the operation was applied, hence the reason the above examples all assigned the result to a variable. However, the same set of mathematical operations can be applied as mutators, so they do directly change the contents of the set.

If the same operators we have seen are applied using the Augmented Assignment style, then they act as mutators. The following statement removes the given elements from the set directly, using an augmented difference operator.

```python
staff -= {"Mark", "Ringo"}
```

The same mutator type behaviour can also be achieved using the methods, however different versions of the methods need to be called. The mutator versions of the methods are called `update()`, `intersection_update()`, `difference_update()` and `symmetric_difference_update()`.

**TASK:** Create the set shown below then use the mutator version of the union method, which is `update()` to add the two missing vowels to the set.

```python
vowels = set({"a", "e", "i"})
```

### Set Comparison Operations

As well as the accessor and mutator type operations, there are also set specific comparisons available. Like the previous set of operations, these are based on well known mathematical style operations.

The comparison operations that can be performed are subset, proper subset, superset, and proper superset. These return a `True` or `False` result.

The operators used to support these are as follows -

- `<=` - subset
- `<` - proper subset
- `>=` - superset
- `>` - proper superset

If we assume we have the following sets -

```python
staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}
```

We could use the subset operator `<` to check whether all the elements of the managers set are also contained within the staff set.

```python
if managers < staff:
    print("All managers are staff members")
```

The proper subset operator `<=` does the same check, but also ensures that the sets are not exactly equal, in other words a set is strictly a subset of another set. The superset `>` and proper superset `>=` operators do the reverse checks. So the following is equivalent to the previous example:

```python
if staff > managers:
    print("All managers are staff members")
```

There are also methods available for performing the same type of comparisons, which are called `issubset()` and `issuperset()`.

**TASK:** Write code based on the previous two examples, but use the equivalent method calls to achieve the same results.

### Creating an Immutable Set

As we have already seen, when a set is constructed using the braces `{ }`, or via the `set()` constructor it is mutable. It is possible however to create an immutable set also. This is done by using the `frozenset()` constructor. It looks the same as the other constructor:

```python
suits = frozenset({"heart", "club", "spade", "diamond"})
```

If a set is created in this way then its contents cannot be changed. The operators and methods available generally remain the same as with a regular set, however anything that mutates the contents is not available. So for example, the `update()` method is not available on a frozenset. However all of the accessor and comparison operators work in exactly the same way as a regular set.

```python
>>> {"club", "diamond"} < suits
True
```

**TASK:** Use the built-in `help()` function to view all the methods available on the frozenset type.

---

## Introducing Dictionaries

The Dictionary data-type stores multiple values like the other collection types. However, what is distinct about a dictionary is that it stores elements as pairs, often called a key:value pair. Dictionaries are ordered and mutable and can have key:value pairs added and removed after initial creation.

Each key is unique and is associated with a single value. i.e. a key maps to a value just like a word in a conventional language dictionary maps to a definition. The set of keys must be unique - each key can appear at most once. However the values in the dictionary do not need to be unique, therefore different keys can be mapped to the same value.

Dictionaries are useful when a value needs to be located quickly given a known key. For example a dictionary may store a collection of customer records (values), and the key to these is the unique customer number.

Since the Dictionary type is built directly into the Python language there is a specific syntax associated with creation and manipulation. This is similar to what we have already seen with a Set. The main difference however is that operations involving Dictionaries usually involve pairs of values. To create a Dictionary directly, braces (curly brackets) can be used:

```python
stock = {"apple":10, "banana":15, "orange":11}
```

This is similar to the notation for a Set, but the contents of the brackets show that it is a dictionary being created. Notice that a pair is specified for each entry separated by a colon ':', in the form key:value.

The key of the first element within the example is the string "apple", and the value associated with this is the number 10. Unlike a set the insertion ordering of the elements is maintained (from Python version 3.7 at least).

A dictionary can also be created by calling the `dict()` constructor. This can be called with various types of arguments and is somewhat more flexible than the `set()` constructor. To create the above dictionary, any of the following variations could be used:

```python
# create by passing a dictionary
stock = dict({"apple":10, "banana":15, "orange":11})

# create by passing keywords (only possible if keys are strings)
stock = dict(apple=10, banana=15, orange=11)

# create by passing list of tuples
stock = dict([("apple",10), ("banana",15), ("orange",11)])
```

Finally an empty dictionary can be created using either empty braces `{ }` or the `dict()` constructor with no arguments. This explains why, as mentioned earlier, an empty Set can ONLY be created using the `set()` constructor with no arguments.

### Dictionary Comprehensions

As with sets and lists, it is also possible to create a dictionary using a comprehension. A very slightly different expression syntax is required, since a pair of values need to be provided for each generated entry. This is handled by the inclusion of a ':' to separate the key from the value.

**TASK:** Enter the code below, then make a call to the `print()` function to display the contents of the dictionary.

```python
import math

roots = {n : math.sqrt(n) for n in range(1,26)}
```

This produces a dictionary that maps a numeric value (in the range 1..25), to its square root.

Hence, the created dictionary will have a total of 25 entries. In which each key is an integer type that maps to a float type.

### Manipulating Dictionaries

Once a dictionary has been created there are several mechanisms available to access and mutate its content. Remember, most operations rely on the key being specified. For example, it is possible to access a value from the dictionary by providing its key as an index:

```python
print("Apple stock level is", stock["apple"])
```

Notice how the provided `[ index ]` value is not necessarily an integer, as with lists, strings or tuples. The provided index value MUST match the data-type of the dictionaries key set, in this case a string.

Since dictionaries are mutable, it is also possible to add or update existing key:value pairs using the indexing notation:

```python
stock["pear"] = 50        	# add new key:value pair
stock["apple"] += 1        	# increase apple stock level
```

**TASK:** Write some code which adds a new fruit called "kiwi" to the stock dictionary, with an initial stock level of 10.

As with sets a common operation performed on dictionaries is membership testing. This can be done using exactly the same syntax as sets, but only the key needs providing, e.g.

```python
if "apple" in stock:
    print("Apples have a stock level")
```

### Dictionary Methods

Many of the methods which are available on the other collection data-types, such as lists, are also available on dictionaries. These include `clear()`, `copy()`, `get()`, `pop()` and `update()`.

These all typically perform in the same away as with the other data-types, but in some cases take slightly different parameters involving a key and value.

```python
# pop the "orange" returning its stock level
stock.pop("orange")

# update the stock to include two new fruits
stock.update(lemmon=15, strawberry=99)
```

**TASK:** Use the built-in `help()` function to view all the methods available on the dict type. Then write some code that uses the `popitem()` method to remove some key:value pairs from the stock dictionary.

### Iterating over Dictionaries

It is very common to iterate over the contents of a dictionary, using a `for...in` type loop.

If just the name of the dictionary is provided, then only the key is extracted during each iteration. So the following would print the keys of the dictionary only:

```python
for item in stock:
    print(item)

apple
banana
orange
```

It is possible to iterate over the values only by calling the `values()` method, e.g.

```python
for level in stock.values():
    print(level)

10
15
11
```

Finally it is possible to iterate over each key:value pair. To do this the `items()` method can be used. This allows access to each key and value as a Tuple, hence each pair can be extracted using sequence unpacking. The code is:

```python
for item,level in stock.items():
    print(item, "has a stock level of", level)

apple has a stock level of 10
banana has a stock level of 15
orange has a stock level of 11
```

**TASK:** Write some code that iterates over the contents of the roots dictionary created within an earlier task. For each entry, print the message -

"The square root of <num> is <sqrt>"

Where `<num>` shows the number, and `<sqrt>` shows the square root of that number.

---

## Key Terminology

Understanding key terminology is important not only when programming but for understanding computer science in general. Certain terms, technologies and phrases will often re-occur when reading or learning about many computer science topics. Having an awareness of these is important, as it makes learning about the various subjects and communication with others in the field easier.

**TASK:** Look at each of the phrases below and ensure you understand what each of these means. For any that you do not understand, do a little research to find a definition of each term. This research may involve looking back over these notes, or the associated lecture notes. It may also involve searching for these terms on the Internet.

- Set
- Set operations
- Set comprehension
- Dictionary
- key:value pair
