# cho các điểm (1,2) (2,4), (3,6), (4,8)
# in ra DS x,y
# nhận xét quan hệ 

points = [(1, 2), (2, 4), (3, 6), (4, 8)]

xs, ys = zip(*points)

print("xs:", xs)
print("ys:", ys)