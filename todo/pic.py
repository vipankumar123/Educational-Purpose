from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_digit_image(digit, path):
    # Create a blank image with white background
    image = Image.new('L', (28, 28), color=255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # Draw the digit in the center of the image
    draw.text((9, 1), str(digit), font=font, fill=0)

    # Save the image
    image.save(path)

# Create and save images for digits 0-9
for digit in range(10):
    create_digit_image(digit, f"digit_{digit}.png")
