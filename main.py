from PIL import Image

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


def main(image_path, output_width, use_braille=False):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, output_width)
    gray_image = grayscale_image(image)

    if use_braille:
        ascii_characters = ASCII_CHARS_BRAILLE
    else:
        ascii_characters = ASCII_CHARS

    ascii_str = map_pixels_to_ascii(gray_image, ascii_characters)

    for i in range(0, len(ascii_str), output_width):
        print(ascii_str[i:i+output_width])

if __name__ == "__main__":
    input_image_path = "input_image.jpg"  # Replace with your input image path
    output_width = 100  # Adjust the width to your preference
    use_braille_characters = False  # Set to False for regular ASCII characters

    main(input_image_path, output_width, use_braille_characters)
