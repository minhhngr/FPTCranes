# Day1

## Importance of NumPy in Python Data Analysis

- What?
- Why
  - Less memory
  - Mathematical siginicantly faster
  - element-wise
  - efficiency > large datasets
- Role of NumPy in the Data Science Ecosystem
  - NumPy acts as the backbone
  - Pandas DataFrames internally use NumPy arrays for storing and processing data
  - Machine learning
  - Learning NumPy
- Libraries for DS
  - SciPy
  - Scikit-learn
  - Numpy
  - Pandas
  - ..

## Creating 1D, 2D and Multidimensional arrays

    - 1D arrays 
        - Represnts a simple seq of values
        - 
    - 2D arrays
        - A 2D represents data in form of rows and columns
        - It is similar to a matrix or a table
        - Each row can be considered as a data point and each column as a feature
    
    - 3D arrays
        - Commonly used to represent data with multiple channels, such as RGB images

Comparing 1D, 2D and multidimensional arrays

| Feature                 | 1D Array                          | 2D Array                                  | Multidimensional Array                 |
|-----------------------  |-----------------------            |-----------------------                    |-----------------------                 |
| Structure               | Linear sequence of elements       | Grid-like structure with rows and columns | Higher dimensions (3D, 4D, etc.)       |
| Representation          | Single row or column              | Matrix or table-like format               | Tensors or multi-layered structures    |
| Indexing                | Single index                      | Two indices (row, column)                 | Multiple indices for each dimension    |
| Use Cases               | Time series, lists                | Images, tabular data                      | Videos, volumetric data                |
| Memory Layout           | Contiguous block of memory        | Contiguous block of memory                | Contiguous block of memory             |
| Mathematical Operations | Element-wise operations           | Matrix operations (dot product, etc.)     | Complex operations across dimensions   |
| Visualization           | Line plots, scatter plots         | Heatmaps, matrices                        | 3D plots, volumetric visualizations    |
| Libraries Support       | NumPy, Pandas                     | NumPy, Pandas, Matplotlib                 | NumPy, TensorFlow, PyTorch             |
| Performance             | Fast for simple operations        | Efficient for matrix computations         | Optimized for high-dimensional data    |
| Shape                   | (n,)                              | (m, n)                                    | (d1, d2, d3, ...)                      |
| Examples                | [1, 2, 3, 4, 5]                   | [[1, 2, 3], [4, 5, 6]]                    | [[[1], [2]], [[3], [4]]]               |

## Introducing to NumPy Arrays Attributes

Arra attributes

- Shape
  - The shape attribute returns a tuple that represents the number of elements in each dimension.
  - It helps identify how many rows and columns (or higher dimensions) an array has.
  - Shape is especially important when working with matrices and datasets.
- Size
  - The size attribute returns the total number of elements in the array.
  - It is calculated by multiplying the sizes of all dimensions together.
  - Size is useful for understanding the overall data volume contained within an array.
- dtype
  - The dtype attribute indicates the data type of the elements stored in the array.
  - It provides information about whether the elements are integers, floats, booleans, etc.
  - Understanding dtype is crucial for ensuring compatibility in mathematical operations and data processing.
- ndim
  - The ndim attribute returns the number of dimensions (axes) of the array.
  - It helps identify whether the array is 1D, 2D, or higher-dimensional.
  - Knowing the number of dimensions is essential for performing appropriate operations and manipulations on the array.

## Basic Arithmetic Operations on NumPy Arrays

Introduce to Arithmetic operations on NumPy arrays

- Direct Arithmetic Operations
- element by element
- Broadcasting
- Scalar Operations
- Mathematical Functions
- Aggregation Functions

Addition and Subtraction of Arrays

- When two arrays have the same shape, Numpy performs element-wise addition or subtraction.
- Corresponding elements from each array are added or subtracted together to produce a new array of the same shape.

Muliplication and Division of Arrays

- MUltiplication and division are also performed element-wise when the arrays have the same shape.
- Each element in the first array is multiplied or divided by the corresponding element in the second array.

Arithmetic Operations with Scalars

- Numpy allows arithmetic operations between arrays and a single value (scalar).
- The scalar value is applied to each element of the array automatically.

## Vetorized Operations for Faster Computations

What are Vectorized Operations?

- Entire arrays at once
- Applies operations to all elements simultaneously
- C-level implementation
- Vectorization is one of the main reasons why NumPy is widely used in data analysis and scientific computing.

Loop-Based vs Vectorized Operations

- Vectorized code is shorter and easier to read
- It avoids Python-level loops, reducing execution time
- Performance improvement is significant for large datasets

Common Vectorized Operations in NumPy

NumPy support many built-in vectorized operations, including: (universal functions or ufuncs)

Vectorization and Broadcasting

-

Why Vectorization is Matter?

- Operation drastically reduces computation time
- More efficient memory usage
- Enables handling of larger datasets

## Indexing and Slicing of 1D & Multidimensional NumPy Arrays

### Indexing and Slicing 1D Arrays

### Indexing and Slicing 2D and Multidimensional Arrays

## Fancy Indexing and Boolean Masking in NumPy Arrays

### Fancy Indexing

- Fancy Indexing and boolean masking are powerful techniques in NumPy that allow for advanced data selection and manipulation within arrays.
- Selected elements based on specific conditions can be non-continuous and in any order.
- It is useful when specific elements need to be extracted or modified based on certain criteria.
- Fancy indexing always return a copy of the data, whereas boolean masking returns a view when possible.

### Boolean Masking

- Boolean masking involves creating a boolean array (mask) that indicates which elements of the original array meet certain conditions.
- The mask is then used to filter the original array, returning only the elements where the mask is True.

### Reshaping, Stacking and Splitting Arrays

- Reshaping
  - Changing the shape of an array without changing its data
  - The total number of elements must remain the same before and after reshaping

- Stacking
  - Used to combine multiple arrays along a new axis (single array)
  - Horizontal stacking (side by side) and vertical stacking (top to bottom)

- Splitting
  - Dividing a single array into multiple sub-arrays
  - Can be done along different axes depending on the array's dimensions

### Introducing to Aggeration in Numpy

- Aggregation functions perform calculations on an array and return a single value.
- Common aggregation functions include sum, mean, median, min, max, std (standard deviation), and var (variance).
- These functions can be applied to the entire array or along specific axes

### Combining Arrays using Concatenation