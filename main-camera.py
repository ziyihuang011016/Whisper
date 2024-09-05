import subprocess
import json

# List of your audio files
audio_files = [f'dataset/photo1/{i}.wav' for i in range(1, 7)]

# Paths to your scripts
sound_recognition_script = "sound_recognition.py"
image_generation_script = "stable_diffusion.py"


# Function to call the sound recognition script and get the prediction result
def detect_sound_categories(audio_file):
    command = ["python", sound_recognition_script, f"--audio_files={audio_file}"]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

# Function to extract the detected category from the output
def extract_category(output):
    try:
        data = json.loads(output)
        return data.get("predicted_class")
    except json.JSONDecodeError:
        return "Unknown"

# Dictionary to store the results
results = {}

# Loop through each audio file and get the category
for i, audio_file in enumerate(audio_files):
    print(f"Processing {audio_file}...")
    output = detect_sound_categories(audio_file)
    category = extract_category(output)
    results[i + 1] = category
    print(f"Finished processing {audio_file}: {category}.")

remaining1 = list({results[2], results[5]})
remaining2 = list({results[i] for i in [1, 3, 4, 6]})

# Format the output strings
# photo_statement = f"a photo of " + ' and '.join([f"{mainscene}" for mainscene in remaining1])
# nearby_statement = f"near by is " + ' and '.join([f"{nearby}" for nearby in remaining2])

photo_statement = f"A 24K photo taken in 2024, in a scene where the sound of " +  ' and '.join([f"{mainscene}" for mainscene in remaining1]) + "appears"
# photo_statement = f"a highly detailed photo of " + ' and '.join([f"{mainscene}" for mainscene in remaining1])
nearby_statement = f"with " + ' and '.join([f"{nearby}" for nearby in remaining2]) + " nearby"

# Combine statements into a single prompt
prompt = (
    "masterpiece, "
    "well-composed, "
    f"{photo_statement}, "
    f"{nearby_statement}, "
    "Captured in natural lighting, with a focus on realism."
    "The overall composition is balanced and immersive, drawing the viewer into the expansive landscape where all these elements coexist in perfect harmony."
)

# Function to generate the image using the prompt
def generate_image_with_prompt(prompt):
    command = ["python", image_generation_script, f"--prompt={prompt}"]
    subprocess.run(command)

# Print and run the final prompt
print(f"Final Prompt: {prompt}")
generate_image_with_prompt(prompt)
