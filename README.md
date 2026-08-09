# Plant Disease Detection Application

A Flask-based web application for detecting plant diseases using deep learning. This application allows users to upload images of plant leaves and get instant predictions about potential diseases, along with treatment recommendations.

## Features

- **Real-time Disease Detection**: Upload plant leaf images and get instant disease predictions
- **Detailed Disease Information**: Comprehensive information about detected diseases
- **Treatment Recommendations**: Suggested treatments and preventive measures
- **Supplement Information**: Details about recommended supplements for treatment
- **User-friendly Interface**: Modern, responsive design with intuitive navigation
- **Error Handling**: Robust error handling and user feedback
- **Mobile Responsive**: Works seamlessly on both desktop and mobile devices

## Project Structure

```
PlantDiseaseApp_Final/
├── app/                    # Application package
│   ├── __init__.py        # Application initialization
│   ├── models.py          # Database models
│   └── routes.py          # Route handlers
├── data/                   # Data files
│   ├── disease_info.csv   # Disease information
│   └── supplement_info.csv # Supplement information
├── models/                 # ML models
│   ├── cnn_model.py       # CNN model architecture
│   ├── model_utils.py     # Model utility functions
│   └── plant_disease_model_1.pt  # Trained model
├── static/                 # Static files
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── uploads/           # User upload directory
├── templates/             # HTML templates
├── run.py                 # Application entry point
├── requirements.txt       # Project dependencies
└── verify_setup.py       # Environment verification script
```

## Prerequisites

- Python 3.8 or newer
- pip package manager
- Virtual environment (recommended)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/plant-disease-detection.git
   cd plant-disease-detection
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify the setup:**
   ```bash
   python verify_setup.py
   ```

## Usage

1. **Start the application:**
   ```bash
   python run.py
   ```

2. **Access the application:**
   Open your web browser and navigate to http://localhost:5000

3. **Using the application:**
   - Navigate to the "Predict" page
   - Upload a plant leaf image
   - View the prediction results and recommendations
   - Access detailed disease information and treatment suggestions

## Supported Plant Diseases

The application can detect various plant diseases, including:
- Apple Scab
- Black Rot
- Cedar Apple Rust
- Corn (maize) diseases
- Grape diseases
- Peach diseases
- Pepper diseases
- Potato diseases
- Strawberry diseases
- Tomato diseases

## Technical Details

### Model Architecture
- CNN-based deep learning model
- Pre-trained on a large dataset of plant disease images
- Optimized for real-time inference

### Key Technologies
- Flask: Web framework
- PyTorch: Deep learning framework
- SQLAlchemy: Database ORM
- Bootstrap: Frontend framework
- Pillow: Image processing

### API Endpoints

- `/`: Home page
- `/predict`: Disease prediction page
- `/result`: Prediction results page
- `/supplements`: Treatment supplements information
- `/about`: About page
- `/contact`: Contact page

## Troubleshooting

### Common Issues

1. **Model Loading Errors**
   - Ensure PyTorch is installed correctly
   - Check model file integrity
   - Verify Python version compatibility

2. **Image Upload Issues**
   - Check file permissions
   - Verify image format (JPG, PNG)
   - Ensure upload directory exists

3. **Database Errors**
   - Verify CSV files are present
   - Check database permissions
   - Ensure SQLAlchemy is configured correctly

### Getting Help

For additional support:
- Check the HELP.md file
- Review the troubleshooting section
- Contact support at support@plantdiseasedetection.com

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Dataset providers
- Open-source community
- Contributors and maintainers

## Contact

For questions and support:
- Email: support@plantdiseasedetection.com
- GitHub: https://github.com/yourusername/plant-disease-detection 