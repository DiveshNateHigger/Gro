import os
import shutil
import pandas as pd
from app import app

# Create required directories
os.makedirs('static/uploads', exist_ok=True)
os.makedirs('data', exist_ok=True)
os.makedirs('models', exist_ok=True)

# Copy model file from the original project if it doesn't exist
model_src = '../Plant_Disease_Detection/plant_disease_model_1.pt'
model_dst = 'models/plant_disease_model_1.pt'

if not os.path.exists(model_dst) and os.path.exists(model_src):
    print(f"Copying model file from {model_src} to {model_dst}")
    shutil.copy2(model_src, model_dst)
else:
    print(f"Model file: {'Found' if os.path.exists(model_dst) else 'Not found'}")

# Copy CSV files from the original project if they don't exist
data_files = [
    ('disease_info.csv', '../Plant_Disease_Detection/disease_info.csv'),
    ('supplement_info.csv', '../Plant_Disease_Detection/supplement_info.csv')
]

for data_file, src_path in data_files:
    dst_path = f'data/{data_file}'
    if not os.path.exists(dst_path) and os.path.exists(src_path):
        print(f"Copying data file {data_file} from {src_path} to {dst_path}")
        shutil.copy2(src_path, dst_path)
    else:
        print(f"Data file {data_file}: {'Found' if os.path.exists(dst_path) else 'Not found'}")

# Print startup information
print("")
print("=" * 50)
print("Plant Disease Detection Application")
print("=" * 50)
print(f"Model loaded: {'Yes' if os.path.exists(model_dst) else 'No'}")
print(f"Data files available: {all(os.path.exists(f'data/{file}') for file, _ in data_files)}")
print("=" * 50)
print("")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 