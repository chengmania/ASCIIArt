# ASCII Art Generator Created by KC3SMW on a Tuesday.
# This program is open source and welcome for anyone to use, modify, enhance to your liking.
# Place this program in its own directory
# create a virtual environment with python3 -m vevn .
# activate environment with source ./bin/activate
# place any picture in your program's directory
# python3 asciiart.py to run.
# Number will be the "resolution"  The larger the number the clearer the image will be

# Import the required libraries
from PIL import Image  # Pillow library to process and manipulate images
import os              # To check if a file exists
import sys             # To handle program exits and system behavior

# Extended ASCII characters set for fine detail mapping
# Characters are arranged from darkest to lightest based on visual density
ASCII_CHARS = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def resize_image(image, new_width=100):
    """
    Resize the input image while maintaining the aspect ratio.
    - Resizing makes the ASCII conversion process manageable and reduces computational load.
    - new_width: Desired width for the ASCII output (default = 100).
    """
    # Get the original image dimensions
    width, height = image.size

    # Calculate the new height to maintain the aspect ratio
    # The multiplier 0.55 adjusts for the difference in aspect ratio between pixels and characters
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)

    # Resize the image to the new dimensions
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayscale(image):
    """
    Convert the input image to grayscale.
    - Grayscale simplifies the image by removing color and focusing on brightness values.
    - Each pixel will now have a value between 0 (black) and 255 (white).
    """
    return image.convert("L")  # "L" mode represents grayscale in Pillow


def pixels_to_ascii(image):
    """
    Convert each pixel of the grayscale image to an ASCII character.
    - Pixels range from 0 (black) to 255 (white).
    - Map pixel values to the ASCII_CHARS list, where darker pixels map to dense characters (like @)
      and lighter pixels map to sparse characters (like spaces).
    """
    # Extract pixel values from the image
    pixels = image.getdata()

    # Initialize an empty string to store ASCII characters
    ascii_str = ""

    # Map each pixel value to an ASCII character
    for pixel in pixels:
        # Scale pixel value (0-255) to the length of ASCII_CHARS dynamically
        ascii_str += ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255]

    return ascii_str


def image_to_ascii(image_path, new_width=100):
    """
    Convert an image file into ASCII art.
    - image_path: Path to the image file.
    - new_width: Desired width for the ASCII art (default = 100).
    """
    try:
        # Open the image file
        image = Image.open(image_path)
    except Exception as e:
        # Print an error message and exit if the file can't be opened
        print(f"Unable to open image file: {e}")
        return

    # Step 1: Resize the image
    image = resize_image(image, new_width)

    # Step 2: Convert the image to grayscale
    image = grayscale(image)

    # Step 3: Map each pixel to an ASCII character
    ascii_str = pixels_to_ascii(image)

    # Step 4: Format the ASCII string into lines
    # Each line corresponds to the width of the image
    img_width = image.width  # Width after resizing
    ascii_str_len = len(ascii_str)  # Total characters in the ASCII string

    # Split the ASCII string into multiple lines
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"

    return ascii_img


def main():
    """
    Main function to interact with the user and generate ASCII art.
    """
    # Prompt the user for an image file path
    image_path = input("Enter the image file path: ")

    # Check if the file exists
    if not os.path.exists(image_path):
        print("File not found. Please provide a valid file path.")
        sys.exit()  # Exit the program if the file doesn't exist

    # Prompt the user for the desired width of the ASCII art
    new_width = input("Enter the desired width for the ASCII art (default is 100): ")
    new_width = int(new_width) if new_width.isdigit() else 100  # Default to 100 if invalid input

    # Generate the ASCII art
    ascii_art = image_to_ascii(image_path, new_width)

    if ascii_art:
        # Display the ASCII art
        print("\nHere is your ASCII art:\n")
        print(ascii_art)

        # Save the ASCII art to a text file
        with open("ascii_image.txt", "w") as f:
            f.write(ascii_art)
        print("\nASCII art has been saved to 'ascii_image.txt'.")


# Entry point of the program
if __name__ == "__main__":
    main()
