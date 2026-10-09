"""Create simple monochrome PNG pictograms; development-only Pillow dependency.

Print a JSON mapping of names to data URLs for embedding in index.html.
The shipped page needs no build step or image requests.
"""
import base64
import io
import json
from PIL import Image, ImageDraw, ImageFont


def icons():
    result = {}
    for name in ['count', 'shapes', 'letters', 'rabbit', 'home', 'next', 'done', 'retry', 'garden', 'pond']:
        image = Image.new('RGB', (160, 160), 'white')
        d = ImageDraw.Draw(image)
        if name == 'count':
            for x, y in [(32, 94), (92, 94), (62, 34)]:
                d.rectangle((x, y, x + 40, y + 40), fill='black')
        elif name == 'shapes':
            d.ellipse((14, 20, 80, 86), outline='black', width=7)
            d.rectangle((88, 80, 144, 136), outline='black', width=7)
        elif name == 'letters':
            # Draw an A as geometry rather than relying on a font.
            d.line([(30, 133), (80, 25), (130, 133)], fill='black', width=14)
            d.line([(50, 92), (110, 92)], fill='black', width=12)
        elif name == 'rabbit':
            d.ellipse((41, 13, 70, 89), fill='white', outline='black', width=6)
            d.ellipse((88, 13, 117, 89), fill='white', outline='black', width=6)
            d.ellipse((30, 65, 130, 148), fill='white', outline='black', width=6)
            d.ellipse((56, 95, 66, 105), fill='black')
            d.ellipse((94, 95, 104, 105), fill='black')
            d.polygon([(74, 115), (86, 115), (80, 123)], fill='black')
            d.line([(80, 123), (80, 132), (69, 132)], fill='black', width=3)
            d.line([(80, 132), (91, 132)], fill='black', width=3)
        elif name == 'home':
            d.polygon([(16, 75), (80, 20), (144, 75)], fill='black')
            d.rectangle((34, 69, 126, 140), fill='black')
            d.rectangle((68, 97, 92, 141), fill='white')
        elif name == 'next':
            d.rectangle((21, 67, 103, 93), fill='black')
            d.polygon([(91, 30), (145, 80), (91, 130)], fill='black')
        elif name == 'done':
            d.line([(27, 83), (65, 121), (136, 39)], fill='black', width=18)
        elif name == 'retry':
            d.arc((27, 31, 133, 137), 25, 285, fill='black', width=12)
            d.polygon([(84, 15), (121, 37), (84, 59)], fill='black')
        elif name == 'garden':
            d.polygon([(47, 56), (119, 73), (57, 139)], fill='white', outline='black', width=6)
            d.line([(70, 57), (53, 19)], fill='black', width=8)
            d.line([(77, 58), (83, 13)], fill='black', width=8)
            d.line([(84, 61), (110, 28)], fill='black', width=8)
            d.line([(56, 77), (76, 84)], fill='black', width=4)
            d.line([(61, 103), (78, 109)], fill='black', width=4)
        elif name == 'pond':
            d.ellipse((42, 68, 130, 112), fill='white', outline='black', width=6)
            d.ellipse((37, 34, 84, 82), fill='white', outline='black', width=6)
            d.polygon([(42, 56), (16, 65), (42, 72)], fill='black')
            d.ellipse((52, 49, 60, 57), fill='black')
            d.arc((74, 78, 115, 101), 0, 180, fill='black', width=4)
            for y in [127, 142]:
                d.line([(19, y), (45, y + 4), (73, y), (102, y + 4), (141, y)], fill='black', width=5)
        buffer = io.BytesIO()
        image.save(buffer, format='PNG', optimize=True)
        result[name] = 'data:image/png;base64,' + base64.b64encode(buffer.getvalue()).decode('ascii')
    return result


if __name__ == '__main__':
    print(json.dumps(icons()))
