from PIL import Image, ImageDraw, ImageFont

def get_fonts(density):
    # Define fonts for regular text and heading
    header_font = ImageFont.truetype("assets/fonts/rajdhani-semibold.ttf", 28*density)
    subline_font = ImageFont.truetype("assets/fonts/rajdhani-medium.ttf", 14*density)
    bolderline_font = ImageFont.truetype("assets/fonts/rajdhani-bold.ttf", 11*density)
    footer_font = ImageFont.truetype("assets/fonts/rajdhani-semibold.ttf", 18*density)
    return header_font, subline_font, bolderline_font, footer_font

def card_render(header='', subline='', bolderline='', balanceline='', density=3):
    # Define fonts for regular text and heading
    header_font, subline_font, bolderline_font, footer_font = get_fonts(density)

    # Load background image
    img = Image.open("assets/imgs/card_background@3x.png")

    # Added triangle icon overlay
    icon_overlay = Image.open("assets/imgs/triangle_icon.png")
    img.paste(icon_overlay, (93*density, 89*density), icon_overlay)

    # Build a surface
    surface = ImageDraw.Draw(img)

    # Write heading
    surface.text((47*density, 11*density), header, font=header_font)
    surface.text((70*density, 46*density), subline, font=subline_font)
    surface.text((97*density, 65*density), bolderline, font=bolderline_font)
    surface.text((103*density, 80*density), balanceline, font=footer_font, fill='#A9EAB0')

    return img

def test_render():
    img = card_render(
        header="$ 12,041.81", 
        subline="sales yestarday", 
        bolderline="monday", 
        balanceline="19%", 
        density=3
    )
    img.save(open("rendered/temp_card.png", "wb"), "PNG")