# Alzheimer's Detection Using MRI

## Overview

The Alzheimer's Detection Using MRI project aims to assist healthcare professionals and researchers in diagnosing Alzheimer's disease with greater speed and accuracy. By leveraging advanced image analysis techniques on MRI scans of the brain, this project provides insights into the stage of Alzheimer's disease and tracks its progression over time.

## Features

- **Automated MRI Analysis**: Utilizes machine learning algorithms to analyze brain MRI images and detect signs of Alzheimer's disease.
- **Disease Staging**: Determines the stage of Alzheimer's disease, offering valuable insights for treatment planning and research.

## Technology Stack

- **Flask**: Backend framework for developing the web application.
- **HTML/CSS/JavaScript**: Frontend technologies for building the user interface.

## Installation

To get started with the project, you need to install the following Python packages:

- `numpy`
- `flask`
- `tensorflow`
- `cv2`

You can install these packages using pip:

```bash
pip install numpy flask tensorflow opencv-python
```

Then you can run the application

```bash
python main.py
```

The application will be accessible at ```http://127.0.0.1:3000/.```

## Usage

1. **Upload an MRI Image**: Use the web interface to upload an MRI image of the brain.
2. **Analyze the Image**: The model will process the image and analyze it for signs of Alzheimer's disease.
3. **View Results**: The application will display the stage of Alzheimer's disease.

