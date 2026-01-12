import pandas as pd
import numpy as np


orders = pd.DataFrame(
    {
        "OrderID": [1001, 1002, 1003, 1004, 1005, 1006, 1007],
        "CustomerID": [1, 2, 1, 3, 2, 4, 3],
        "ProductID": [101, 102, 103, 101, 104, 102, 103],
        "Quantity": [2, 1, 3, 1, 2, 1, 2],
        "Price": [500, 800, 300, 500, 1200, 800, 300],
        "OrderDate": pd.to_datetime(
            [
                "2024-01-05",
                "2024-01-06",
                "2024-01-10",
                "2024-01-15",
                "2024-01-20",
                "2024-01-22",
                "2024-01-25",
            ]
        ),
    }
)

customers = pd.DataFrame(
    {
        "CustomerID": [1, 2, 3, 4],
        "CustomerName": ["An", "Bình", "Chi", "Dũng"],
        "City": ["Hà Nội", "HCM", "Hà Nội", "Đà Nẵng"],
        "Age": [25, 30, np.nan, 28],
    }
)

products = pd.DataFrame(
    {
        "ProductID": [101, 102, 103, 104],
        "ProductName": ["Laptop", "Phone", "Mouse", "Tablet"],
        "Category": ["Electronics", "Electronics", "Accessory", "Electronics"],
    }
)

# xử lý dữ liệu thiếu
# thêm cột doanh thu, tính tổng doanh thu toàn hệ thống
# doanh thu theo City, doanh thu theo Category
# với mỗi customer: tổng doanh thu, số đơn hàng, doanh thu trung bình/đơn
# merge order, customer => sau đó merge kết quả với product
# top 2 khách hàng chi tiêu nhiều nhất, top 1 sản phẩm bán chạy nhất
# report: tổng doanh thu theo tháng, top khách hàng mỗi thành phố,
# top sản phẩm mỗi Category

