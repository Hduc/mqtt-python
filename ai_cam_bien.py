import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dữ liệu mẫu: Độ ẩm đất, nhiệt độ, ánh sáng mặt trời, lượng nước tưới
data = pd.read_csv('sensor_data.csv')

X = data[['soil_moisture', 'temperature', 'sunlight']]  # Đầu vào cảm biến
y = data['water_amount']  # Lượng nước tưới

# Tách dữ liệu huấn luyện và kiểm thử
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Huấn luyện mô hình
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán lượng nước tưới
predicted_water = model.predict(X_test)

# In kết quả
print(predicted_water)

