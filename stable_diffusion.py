from diffusers import StableDiffusionPipeline, ControlNetModel
import torch
from accelerate import Accelerator
import argparse

def generate_image(prompt, output_path="photos/output.png"):
    model_id = "CompVis/stable-diffusion-v1-4"
    #model_id="stabilityai/stable-diffusion-2"
    accelerator = Accelerator()
    device = accelerator.device
    print(f"Using device: {device}")

    pipe = StableDiffusionPipeline.from_pretrained(model_id)
    pipe = pipe.to(device)
    
    width = 768
    height = 512

    image = pipe(prompt, width=width, height=height).images[0]
    image.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="prompts")
    parser.add_argument("--prompt", type=str, required=True)
    args = parser.parse_args()
    prompt = args.prompt
    #prompt = "A 24K photo taken in 2024, in a scene where the sound of rustling leaves appears, with the sound of birds singing and bike bell ringing near by.Captured in natural lighting in the morning, with a focus on realism.The overall composition is balanced and immersive, drawing the viewer into the landscape where all these elements coexist in harmony." 
    generate_image(prompt)
