from PIL import Image

ASCII_CHARS = ["@", "#", "$", "%", "*", "+", ";", ":", ",", ".", "?"]

def resize_img(image, new_width=100):
	width, height = image.size
	ratio = height / width
	new_height = int(new_width * ratio)
	resized_img = image.resize((new_width, new_height))
	return(resized_img)

def grayscale(image):
	grayscale_image = image.convert("L")
	return(grayscale_image)

def pixels_to_ASCII(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return(characters)

def main(new_width=100):
	path = input("Enter a pathname to an image:\n")
	try:
		image = Image.open(path)
	except:
		print(path, "is not a valid pathname.")
		return

	new_image_data = pixels_to_ASCII(grayscale(resize_img(image)))

	pixel_count = len(new_image_data)
	ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

	print(ascii_image)

	with open("ascii_image.txt", "w") as f:
		f.write(ascii_image)


main()