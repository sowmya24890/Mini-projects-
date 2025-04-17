# meme_generator.py

from PIL import Image, ImageDraw, ImageFont

def generate_meme(image_path, top_text, bottom_text, output_path):
    # Load image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Load a default font
    try:
        font = ImageFont.truetype("arial.ttf", size=36)
    except:
        font = ImageFont.load_default()

    # Get image dimensions
    width, height = img.size

    # Add top text
    top_text = top_text.upper()
    top_width, top_height = draw.textsize(top_text, font=font)
    top_position = ((width - top_width) // 2, 10)
    draw.text(top_position, top_text, fill="white", font=font, stroke_width=2, stroke_fill="black")

    # Add bottom text
    bottom_text = bottom_text.upper()
    bottom_width, bottom_height = draw.textsize(bottom_text, font=font)
    bottom_position = ((width - bottom_width) // 2, height - bottom_height - 10)
    draw.text(bottom_position, bottom_text, fill="white", font=font, stroke_width=2, stroke_fill="black")

    # Save output
    img.save(output_path)
    print(f"Meme saved as {output_path}")

if __name__ == "__main__":
    image_path = "sample.jpg"  # Use your own image
    output_path = "meme_output.jpg"
    top_text = input("Enter top text: ")
    bottom_text = input("Enter bottom text: ")
    generate_meme(image_path, top_text, bottom_text, output_path)