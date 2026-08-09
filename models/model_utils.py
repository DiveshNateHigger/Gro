import os
import torch
import numpy as np
from PIL import Image
from models.cnn_model import CNN, idx_to_classes

# Initialize model
def load_model(model_path):
    """Load the plant disease detection model."""
    model = CNN(39)  # 39 classes
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

def preprocess_image(image_path):
    """Manually preprocess the image for model input."""
    # Open and resize the image
    image = Image.open(image_path).convert('RGB')
    image = image.resize((224, 224))
    
    # Convert to numpy array
    np_image = np.array(image)
    
    # Normalize to [0, 1]
    np_image = np_image / 255.0
    
    # Convert to tensor format: [C, H, W]
    np_image = np_image.transpose((2, 0, 1))
    
    # Convert to PyTorch tensor
    tensor = torch.from_numpy(np_image).float()
    
    # Add batch dimension
    tensor = tensor.unsqueeze(0)
    
    return tensor

def predict_disease(model, image_path):
    """Predict disease from image."""
    # Check if file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    # Preprocess image
    try:
        image_tensor = preprocess_image(image_path)
    except Exception as e:
        raise ValueError(f"Error processing image: {str(e)}")
    
    # Make prediction
    with torch.no_grad():
        try:
            output = model(image_tensor)
            _, predicted = torch.max(output, 1)
            predicted_idx = predicted.item()
            
            # Get class name
            if predicted_idx in idx_to_classes:
                return predicted_idx, idx_to_classes[predicted_idx]
            else:
                raise ValueError(f"Unknown class index: {predicted_idx}")
        except Exception as e:
            raise RuntimeError(f"Error during prediction: {str(e)}") 