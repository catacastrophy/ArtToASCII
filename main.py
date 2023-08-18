from PIL import Image
import sys

# Define ASCII characters to represent different shades
ASCII_CHARS = "@B%8WM#*oahkbdpwmZO0QCJYXzcvnxrjft/\|()1{}[]-_+~<>i!lI;:,\"^`'. "
ASCII_CHARS_BRAILLE = "⠀⠁⠉⠙⠛⠟⠿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿"

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image, characters):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        index = int(pixel * (len(characters) - 1) / 255)
        ascii_str += characters[index]
    return ascii_str

def save_ascii_to_text(ascii_str, output_path):
    with open(output_path, "w") as f:
        f.write(ascii_str)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py input_image_path")
        return

    input_image_path = sys.argv[1]
    output_width = 100
    use_braille_characters = True

    try:
        image = Image.open(input_image_path)
    except Exception as e:
        print("Error:", e)
        return

    image = resize_image(image, output_width)
    gray_image = grayscale_image(image)

    if use_braille_characters:
        ascii_characters = ASCII_CHARS_BRAILLE
    else:
        ascii_characters = ASCII_CHARS

    ascii_str = map_pixels_to_ascii(gray_image, ascii_characters)

    output_path = "ascii_art.txt"
    save_ascii_to_text(ascii_str, output_path)
    print("ASCII art saved to:", output_path)

if __name__ == "__main__":
    main()
