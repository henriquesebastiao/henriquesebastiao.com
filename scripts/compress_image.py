from PIL import Image
import argparse

def compress_image(input_path, quality=85):
    try:
        img = Image.open(input_path)
        img = img.convert('RGB')
        img.save(input_path, quality=quality, optimize=True)
        print(f'Imagem comprimida: {input_path}')
    except Exception as e:
        print(f'Erro ao processar {input_path}: {e}')

parser = argparse.ArgumentParser(description='Compress multiple images for web deployment.')
parser.add_argument('input_files', nargs='+', help='Paths to the image files to compress.')
parser.add_argument('--quality', type=int, default=85, help='Quality of compressed images (default: 85).')

args = parser.parse_args()

for image_path in args.input_files:
    compress_image(image_path, args.quality)
