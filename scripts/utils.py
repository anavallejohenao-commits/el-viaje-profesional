import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def load_config(config_path):
    """Load JSON configuration file."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_estaciones(estaciones_path):
    """Load estaciones data."""
    with open(estaciones_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_background(width, height, color='#1a1a1a'):
    """Create a solid color background image."""
    img = Image.new('RGB', (width, height), hex_to_rgb(color))
    return np.array(img)

def create_title_slide(width, height, title, subtitle, bg_color='#1a1a1a', 
                       title_color='#ffffff', accent_color='#22c55e'):
    """Create a title slide with background and text."""
    img = Image.new('RGB', (width, height), hex_to_rgb(bg_color))
    draw = ImageDraw.Draw(img)
    
    # Try to use available fonts, fallback to default
    try:
        title_font = ImageFont.truetype("arial.ttf", 80)
        subtitle_font = ImageFont.truetype("arial.ttf", 48)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Draw title
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    draw.text((title_x, height // 3), title, fill=hex_to_rgb(accent_color), font=title_font)
    
    # Draw subtitle
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    draw.text((subtitle_x, height // 2 + 100), subtitle, fill=hex_to_rgb(title_color), font=subtitle_font)
    
    return np.array(img)

def create_speaker_slide(width, height, speaker_name, text, color='#22c55e', bg_color='#1a1a1a'):
    """Create a slide with speaker name and text."""
    img = Image.new('RGB', (width, height), hex_to_rgb(bg_color))
    draw = ImageDraw.Draw(img)
    
    try:
        speaker_font = ImageFont.truetype("arial.ttf", 48)
        text_font = ImageFont.truetype("arial.ttf", 32)
    except:
        speaker_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
    
    # Draw speaker name
    draw.text((100, 100), speaker_name, fill=hex_to_rgb(color), font=speaker_font)
    
    # Draw text (with word wrapping)
    words = text.split()
    lines = []
    current_line = []
    max_width = width - 200
    
    for word in words:
        current_line.append(word)
        test_text = ' '.join(current_line)
        bbox = draw.textbbox((0, 0), test_text, font=text_font)
        if bbox[2] - bbox[0] > max_width:
            lines.append(' '.join(current_line[:-1]))
            current_line = [word]
    lines.append(' '.join(current_line))
    
    # Draw wrapped text
    y_offset = 250
    for line in lines:
        draw.text((100, y_offset), line, fill=hex_to_rgb('#ffffff'), font=text_font)
        y_offset += 80
    
    return np.array(img)

def create_estacion_title(width, height, numero, titulo, color, bg_color='#1a1a1a'):
    """Create an estacion title slide."""
    img = Image.new('RGB', (width, height), hex_to_rgb(bg_color))
    draw = ImageDraw.Draw(img)
    
    try:
        title_font = ImageFont.truetype("arial.ttf", 96)
        subtitle_font = ImageFont.truetype("arial.ttf", 56)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Draw estacion number and title
    estacion_text = f"ESTACIÓN {numero}"
    draw.text((100, 200), estacion_text, fill=hex_to_rgb(color), font=title_font)
    draw.text((100, 350), titulo, fill=hex_to_rgb('#ffffff'), font=subtitle_font)
    
    return np.array(img)

def ensure_dir(path):
    """Ensure directory exists."""
    Path(path).mkdir(parents=True, exist_ok=True)
