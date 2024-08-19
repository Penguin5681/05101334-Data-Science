## 1. WAP to multiply 2 Numpy Matrices

```python 
import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = np.dot(matrix1, matrix2)

print(result)
```

## 2. How will you check that an given array is empty?

```python
import numpy as np

array = np.array([])
is_empty = array.size == 0

print(is_empty) 
```

## 3. Diff: np.mean v/s np.average
| Feature           | `np.mean`                                | `np.average`                                    |
|-------------------|------------------------------------------|-------------------------------------------------|
| **Purpose**       | Calculates the arithmetic mean of the elements | Calculates the weighted average of the elements |
| **Syntax**        | `np.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>)` | `np.average(a, axis=None, weights=None, returned=False)` |
| **Weighting**     | Does not consider weights               | Can take a `weights` parameter to compute weighted average |
| **Default Behavior** | Computes a simple average             | Behaves like `np.mean` if no weights are provided |
| **Use Case**      | Use when you need a simple average       | Use when you need to compute a weighted average  |

## 4. How will you check the datatype of elements stored in NumPy array?

```python
import numpy as np

array = np.array([1, 2, 3, 4, 5])
datatype = array.dtype

print(datatype)
```

## 5. What are Nd arrays?

```python
# Multidimensional arrays
import numpy as np

arr_1d = np.array([1, 2, 3, 4])

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

arr_4d = np.random.rand(2, 3, 4, 5)  # Random 4D array with shape (2, 3, 4, 5)

```

## 6. Diff: Python List v/s NumPy Array

| Feature                 | Python Lists                         | NumPy Arrays                          |
|-------------------------|--------------------------------------|---------------------------------------|
| **Data Type**           | Can hold elements of different types | Homogeneous elements (same type)      |
| **Performance**         | Slower for numerical operations      | Faster due to vectorization and C implementation |
| **Memory Usage**        | Higher memory overhead               | More memory efficient                 |
| **Flexibility**         | Highly flexible, allows mixed types  | Less flexible, requires same data type |
| **Mathematical Operations** | Limited, requires loops or list comprehensions | Extensive support, direct operations possible |
| **Use Cases**           | General-purpose, small datasets      | Large-scale numerical computation, scientific computing |

## 7. Explain head and tail with diff params
### The head() function is used to display the first few rows of a DataFrame or series. By default, it shows the first 5 rows, but you can specify how many rows you want to see.
### The tail() function is used to display the last few rows of a DataFrame or series. By default, it shows the last 5 rows, but you can specify how many rows you want to see.

```python
import pandas as pd

df = pd.read_csv('')
print("First 2 rows:\n", df.head(2))
print("\nLast 2 rows:\n", df.tail(2))

```

## 8. Diff: drop v/s dropna

| Feature               | `drop()`                                      | `dropna()`                                  |
|-----------------------|-----------------------------------------------|---------------------------------------------|
| **Purpose**           | Removes rows or columns based on labels       | Removes rows or columns containing `NaN`    |
| **Main Parameter**    | `labels`, `axis`, `index`, `columns`          | `axis`, `how`, `thresh`, `subset`           |
| **Usage**             | Used to drop specific rows/columns by name    | Used to clean data by removing `NaN` values |
| **Handling Missing Data** | Does not handle `NaN` values             | Specifically designed to handle `NaN` values |
| **Example Use Case**  | Dropping the "City" column or row with index 1 | Dropping rows with missing values in the "Age" column |

## 9. Discuss built-in data types available in python

| Data Type    | Description                                              | Example                          |
|--------------|----------------------------------------------------------|----------------------------------|
| **`int`**    | Whole numbers, positive or negative                      | `x = 10`                         |
| **`float`**  | Real numbers with decimal points                         | `y = 10.5`                       |
| **`complex`**| Complex numbers with real and imaginary parts            | `z = 2 + 3j`                     |
| **`str`**    | Sequence of characters (text)                            | `s = "Hello, World!"`            |
| **`list`**   | Ordered, mutable collection of elements                  | `l = [1, "two", 3.0]`            |
| **`tuple`**  | Ordered, immutable collection of elements                | `t = (1, "two", 3.0)`            |
| **`range`**  | Immutable sequence of numbers, often used in loops       | `r = range(1, 10)`               |
| **`dict`**   | Unordered collection of key-value pairs                  | `d = {"name": "Alice", "age": 25}` |
| **`set`**    | Unordered collection of unique elements                  | `s = {1, 2, 3, 4}`               |
| **`frozenset`**| Immutable set                                          | `fs = frozenset([1, 2, 3])`      |
| **`bool`**   | Boolean values `True` or `False`                         | `is_true = True`                 |
| **`bytes`**  | Immutable sequence of bytes                              | `b = b'hello'`                   |
| **`bytearray`** | Mutable sequence of bytes                             | `ba = bytearray(b'hello')`       |
| **`memoryview`**| Memory view of a buffer                               | `mv = memoryview(bytearray(b'hello'))` |
| **`NoneType`**| Represents the absence of a value (`None`)              | `x = None`                       |

## 10. WAP using python to show inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal is making a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

animal.speak()
dog.speak()
cat.speak()
print(dog.name)  # Access inherited attribute
```