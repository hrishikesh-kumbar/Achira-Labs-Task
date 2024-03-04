
#python3 gen_images.py --input input_images/ --out-dims 1024 1024 --nout 1000 --output output_images/


import os
import random
import argparse
from PIL import Image

def generate_images(input_folder, M, output_folder, nout):
    # Checking if the input folder exists
    if not os.path.isdir(input_folder):
        print(f"Input folder {input_folder} does not exist.")
        return

    # Creating output folder
    os.makedirs(output_folder, exist_ok=True)

    # Reading 4 images from the input folder
    input_images = [Image.open(os.path.join(input_folder, file)).convert('I') for file in os.listdir(input_folder) if file.endswith('.tif')]
    N = len(input_images)

    # Computing k based on the input image sizes and M
    k = M // max([max(img.size) for img in input_images])

    for i in range(nout):
        # Generating M x M pixel output images in I mode
        output_image = Image.new('I', (M, M))

        # List to store the positions and sizes of all images that have been placed
        placed_images = []

        for j in range(N):
            for _ in range(k):
                # Scaling each shape randomly by a factor of 1 to 0.75
                scale_factor = random.uniform(0.75, 1)
                img = input_images[j].resize((int(input_images[j].width * scale_factor), int(input_images[j].height * scale_factor)))

                # Rotating each shape randomly by 0 to 90 degrees
                img = img.rotate(random.uniform(0, 90))

                #Placing the shapes at random position without getting cut off at the boundary or overlap other shapes
                for _ in range(100):  # Try up to 100 times
                    max_x = M - img.width
                    max_y = M - img.height
                    pos_x = random.randint(0, max_x)
                    pos_y = random.randint(0, max_y)

                    # Checking if this position overlaps with any existing shapes
                    if any((pos_x < x + w and pos_x + img.width > x and pos_y < y + h and pos_y + img.height > y) for x, y, w, h in placed_images):
                        continue  # This position overlaps

                    # This position does not overlap, placing the shape here
                    output_image.paste(img, (pos_x, pos_y))
                    placed_images.append((pos_x, pos_y, img.width, img.height))
                    break
                else:
                    print(f"Could not place image {j} after 100 attempts. Skipping this image.")

        # Save the output image
        output_image.save(os.path.join(output_folder, f'output_{i}.png'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate images.')
    parser.add_argument('--input', type=str, required=True, help='Input folder')
    parser.add_argument('--out-dims', type=int, nargs=2, required=True, help='Output image dimensions')
    parser.add_argument('--nout', type=int, required=True, help='Number of output images')
    parser.add_argument('--output', type=str, default='./output/', help='Output folder')
    args = parser.parse_args()

    generate_images(args.input, args.out_dims[0], args.output, args.nout)
