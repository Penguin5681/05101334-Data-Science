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
