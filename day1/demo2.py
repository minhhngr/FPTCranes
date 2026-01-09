import numpy as np

tmp_a = np.array([1, 2, 3])
tmp_b = np.array([4, 5, 6])

print("a+b:", tmp_a + tmp_b)  # Output: [5 7 9]
print("a-b:", tmp_a - tmp_b)  # Output: [-3 -3 -3]
print("a*b:", tmp_a * tmp_b)  # Output: [ 4 10 18]
print("a/b:", tmp_a / tmp_b)  # Output: [0.25 0.4  0.5 ]
print("a**b:", tmp_a**tmp_b)  # Output: [  1  32 729]
print("a%b:", tmp_a % tmp_b)  # Output: [1 2 3]
print("a//b:", tmp_a // tmp_b) # Output: [0 0 0]
print("a.dot(b):", tmp_a.dot(tmp_b)) # Output: 32
print("np.dot(a, b):", np.dot(tmp_a, tmp_b)) # Output: 32
print("a.sum():", tmp_a.sum()) # Output: 6
print("b.sum():", tmp_b.sum()) # Output: 15
print("a.mean():", tmp_a.mean()) 
print("b.mean():", tmp_b.mean())
print("a.std():", tmp_a.std())
print("b.std():", tmp_b.std())
print("a.min():", tmp_a.min())
print("b.min():", tmp_b.min())
print("a.max():", tmp_a.max())
print("b.max():", tmp_b.max())
print("a.argmin():", tmp_a.argmin())
print("b.argmax():", tmp_b.argmax())
print("a.argsort():", tmp_a.argsort())
print("b.argsort():", tmp_b.argsort())
print("np.sqrt(a):", np.sqrt(tmp_a))
print("np.exp(b):", np.exp(tmp_b))
print("np.log(a):", np.log(tmp_a))
print("np.sin(a):", np.sin(tmp_a))
print("np.cos(b):", np.cos(tmp_b))
print("np.tan(a):", np.tan(tmp_a))
print("np.arcsin(a/3):", np.arcsin(tmp_a / 3))
print("np.arccos(b/6):", np.arccos(tmp_b / 6))
print("np.arctan(a):", np.arctan(tmp_a))
print("np.sinh(a):", np.sinh(tmp_a))
print("np.cosh(b):", np.cosh(tmp_b))
print("np.tanh(a):", np.tanh(tmp_a))
print("np.arcsinh(a):", np.arcsinh(tmp_a))
print("np.arccosh(b+1):", np.arccosh(tmp_b + 1))
print("np.arctanh(a/3):", np.arctanh(tmp_a / 3))
print("np.logical_and(a<3, b>4):", np.logical_and(tmp_a < 3, tmp_b > 4))
print("np.logical_or(a<2, b>5):", np.logical_or(tmp_a < 2, tmp_b > 5))

# Broadcasting examples

tmp_c = np.array([[4, 5, 6], [7, 8, 9]])

print("Broadcasting")
print("c + x:", tmp_c + 10)              # Output: [[14 15 16] [17 18 19]]
print("tmp_b + tmp_c:", tmp_b + tmp_c)   # Output: [[ 8 10 12] [11 13 15]]
