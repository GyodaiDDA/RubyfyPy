# RubyfyPy
`Ruby methods for Python objects` (Weird, right?)

**While Python is amazing** and beats Ruby in many areas, cleanliness and readability are not among those. 

As it happened to me, **developers used to Ruby** will often miss its obsessively organized landscape.

So, to make the new place cosier, **this package provides Ruby-like methods** for Python objects.

Most of them will be perfectly useless once you get accustomed to Python, but, with some luck, they will help you understand how to do in Python everything you used to do in Ruby.


## Methods and Features

- **Array Utilities for Lists**
  - `flatten`: Recursively flattens nested lists.
  - `first`: Returns the first element of a list.
  - `last`: Returns the last element of a list.
  - `uniq`: Removes duplicate elements from a list while preserving order.

- **Integer Utilities**
  - `is_prime`: Determines if an integer is prime.
  - `is_even`: Checks if an integer is even.
  - `is_odd`: Checks if an integer is odd.

- **Functional Utilities**
  - `is_hashable` in .core.py checks if an object is hashable.

>`flatten` and `uniq` have a `bang` parameter, which defaults to `False`. When set to `True`, the methods will modify the original list in place. See [Usage Examples](#usage-examples) for more details.

## Installation

Package is not yet deployed to [PyPI](https://pypi.org/), but you can install it manually:

To develop locally, clone the repository and run:

```bash
git clone https://github.com/GyodaiDDA/RubyfyPy.git
cd RubyfyPy
pip install -e .[dev]
```

To use it in a project (and I'm not sure why you would want to do that):

```bash
pip install git+https://github.com/GyodaiDDA/RubyfyPy.git
```

## Usage Examples

Include RubyfyPy in your Python code to get access to the methods:

```python
from RubyfyPy import *

# Flatten a nested list
nested = [1, [2, 3], [4, [5, 6]]]
print(flatten(nested))  # Output: [1, 2, 3, 4, 5, 6]
flatten(nested, bang=True)  # nested is now [1, 2, 3, 4, 5, 6]

# Get the first and the last element of a list
print(first([1, 2, 3]))  # Output: 1
print(last([1, 2, 3]))   # Output: 3

# Remove duplicate elements from a list
numbers = [1, 2, 2, 3, 3, 3]
print(uniq(numbers))  # Output: [1, 2, 3]
uniq(numbers, bang=True)  # numbers is now [1, 2, 3]

# Working with integers
print(is_prime(7))  # Output: True
print(is_even(4))   # Output: True
print(is_odd(3))    # Output: True

# Check if an object is hashable
print(is_hashable("string"))  # Output: True
```

## Running Tests

RubyfyPy uses [pytest](https://docs.pytest.org/) for testing. To run the test suite, first make sure RubyfyPy is installed (preferably in editable mode) and then execute:

```bash
pytest
```

## Contributing

Contributions are super welcome! Feel free to jump in.

- Open a pull request
- Report issues via [GitHub Issues](https://github.com/your-username/RubyfyPy/issues)
- Or just e-mail me `rodrigo.gyodai@gmail.com`

This project is licensed under the MIT License.
