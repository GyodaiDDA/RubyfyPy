# RubyfyPy

RubyfyPy is a Python package. Weird, right?

**While Python is amazing** and beats Ruby in many areas, cleanliness and readability is not of those. Therefore, **developers used to Ruby** will often miss its obsessively organized landscape.

To ease that transition, **this package provides Ruby-like methods** and behaviors for Python objects. It wraps Python's basic data structures with Ruby-inspired classes that implement familiar Ruby methods.

### Features and Ruby-like Methods

- `Rubyfy()` method that will transform
    - list > arrays
    - dict > hash
    - str > string

- `Array` class with the methods:
  - `first()`: Returns the first element
  - `last()`: Returns the last element
  - `each()`: Iterates through elements
  - `map()`: Transforms elements
  - `select()`: Filters elements

- `Hash` class with methods:
  - `keys()` and `values()` for Ruby-style handling
  - `get()` to access keys and values

- `String` class with methods:
  - `upcase()`: Converts to uppercase
  - `downcase()`: Converts to lowercase
  - `reverse()`: Reverses the string

### Installation
Package is not yet deployed to [PyPI](https://pypi.org/), but you can go with:

```
git clone https://github.com/your-username/RubyfyPy.git
cd RubyfyPy
pip install -e .
```

### Usage

```
from RubyfyPy import *

python_array = [1, 2, 3, 4, 5]
ruby_array = rubyfy(python_array)

ruby_array.len() # returns 5
ruby_array.first() # returns 1
ruby_array.each(lambda x: print(x)) # prints each element

# Works recursively
nested_list = [1, [2, [3]]]
ruby_nested = rubyfy(nested_list)
type(ruby_nested[1])  # <class 'RubyfyPy.core.Array'>

ruby_hash = rubyfy({'name': 'John', 'age': 30})
ruby_hash.values() # returns ['John', 30]

ruby_string = rubyfy("hello world")
ruby_string.upcase()  # "HELLO WORLD"
```

### Contributing

Contributions are super welcome! Feel free to jump in.

- Open a pull request
- Report issues via [GitHub Issues](https://github.com/your-username/RubyfyPy/issues)
- Or just e-mail me `rodrigo.gyodai@gmail.com`

## Project Status
Just started.

###
*This project is licensed under the MIT License - see the LICENSE file for details.*
