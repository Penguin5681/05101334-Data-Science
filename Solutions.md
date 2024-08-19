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
