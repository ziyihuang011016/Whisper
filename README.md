# Whisper

## Project Overview

This project is designed to detect sound categories from audio files and use those detected categories to generate images using a pre-trained Stable Diffusion model. The project is divided into two main parts: sound recognition and image generation.

1. **Sound Recognition**: Analyzes audio files to predict the most likely sound categories.
2. **Image Generation**: Uses the predicted sound categories to generate a descriptive prompt, which is then used to create an image.

## Prerequisites

### Hardware Requirements
- A machine with Python 3.x installed
- GPU (Optional but recommended for faster image generation)

### Software Requirements
- Python 3.x
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ziyihuang011016/whisper.git
   cd whisper
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment Variables** *(if required)*
   - You may need to configure specific environment variables depending on the models and scripts you're using.

## Usage

### 1. Structure

- `dataset/photo1/`: Contains the audio files for sound recognition.
- `sound_recognition.py`: Script for detecting sound categories from audio files.
- `stable_diffusion.py`: Script for generating images using Stable Diffusion based on the generated prompt.
- `photos`: Contains the generated images.

### 2. Running the Project

1. **Run the Main Script**
   ```bash
   python main-camera.py
   ```
   This script will process the audio files, detect the sound categories, generate a descriptive prompt, and finally create an image based on that prompt.

2. **Understanding the Output**
   - The detected sound categories will be logged in the console.
   - The final prompt used for image generation will also be displayed.
   - The generated image will be saved in the folder named `photos` (or as configured in your `stable_diffusion.py` script).

### 3. Customizing the Project

- **Audio Files**: Place your audio files in the `dataset/photo1/` directory. The script is currently set up to process six files named `1.wav`, `2.wav`, ..., `6.wav`.
- **Sound Recognition Script**: Modify `sound_recognition.py` if you wish to change how sound categories are detected.
- **Image Generation Script**: Modify `stable_diffusion.py` to adjust the image generation settings.

### Example Output

After running the project, an image will be generated based on the sound categories detected from your audio files. The prompt used to generate the image will be in a similar format:

```
"A 24K photo taken in 2024, in a scene where the sound of [detected_category_1] and [detected_category_2] appears, with [detected_category_3] and [detected_category_4] nearby. Captured in [The entered light information], with a focus on realism."
```

## Troubleshooting

- **Error Handling**: If you encounter any JSON parsing errors, it might be due to incorrect or malformed output from the sound recognition script. Check the console logs for more information.
- **Dependencies**: Make sure all required Python packages are installed, and the correct versions are used.

