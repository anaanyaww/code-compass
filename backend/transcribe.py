import Textsum as ps
import sys 
data="""
Basics of Loops in Python

Loops in Python are used to execute a block of code repeatedly. There are two main types of loops:

For Loop: Iterates over a sequence and executes a block of code for each item in the sequence.
Example:

python
Copy code
for item in sequence:
    # Code block to be executed for each item
While Loop: Repeats a block of code as long as a specified condition is true.
Example:

python
Copy code
while condition:
    # Code block to be executed as long as condition is true
Advanced Looping in Python

Python offers several advanced looping techniques for efficient iteration:

Enumerate: Adds a counter to an iterable object, allowing iteration over elements and their indices simultaneously.

Zip: Combines multiple iterables into tuples, allowing simultaneous iteration over corresponding elements.

List Comprehension: Provides a concise way to create lists using a single line of code.

Dictionary Comprehension: Creates dictionaries in a compact form.

Generator Expression: Creates a generator object that lazily generates values, saving memory compared to lists.

These looping techniques provide powerful tools for iterating over data efficiently in Python, enhancing code readability and reducing complexity.

"""
print(len(data))
#prompt=str(sys.argv[1])
final=ps.all_in_one.ytid(data)
 
print(final)