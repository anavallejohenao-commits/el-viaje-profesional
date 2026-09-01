#!/usr/bin/env python3
"""
El Viaje Profesional - Video Generator
Genera un video noticiero basado en el script de EduConecta Aburrá Sur
"""

import os
import sys
from pathlib import Path
import json
from moviepy.editor import (
    VideoClip, TextClip, ImageClip, CompositeVideoClip,
    concatenate_videoclips, ColorClip, AudioFileClip, CompositeAudioClip
)
from utils import (
    load_config, load_estaciones, create_title_slide, 
    create_speaker_slide, create_estacion_title, ensure_dir, hex_to_rgb
)

# Configuración de rutas
PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_PATH = PROJECT_ROOT / 'config' / 'video_config.json'
ESTACIONES_PATH = PROJECT_ROOT / 'config' / 'estaciones.json'
OUTPUT_DIR = PROJECT_ROOT / 'video_final'

def create_color_clip(width, height, color, duration):
    """Crea un clip de color sólido."""
    return ColorClip(size=(width, height), color=hex_to_rgb(color)).set_duration(duration)

def create_text_clip(text, duration, fontsize=40, color='white', width=1920):
    """Crea un clip de texto."""
    txt_clip = TextClip(
        text,
        fontsize=fontsize,
        color=color,
        font='Arial',
        method='caption',
        size=(width - 100, None)
    ).set_duration(duration)
    return txt_clip.set_position('center')

def generate_intro(config, estaciones_data, width, height):
    """Genera la introducción."""
    clips = []
    
    # Fondo y título
    bg_clip = create_color_clip(width, height, config['colors']['background'], 4)
    
    title_text = f"{estaciones_data['proyecto']['titulo']}\n{estaciones_data['proyecto']['subtitulo']}"
    title_clip = create_text_clip(title_text, 4, fontsize=64, color='#22c55e', width=width)
    
    intro_clip = CompositeVideoClip(
        [bg_clip, title_clip],
        size=(width, height)
    )
    clips.append(intro_clip)
    
    # Presentación Ana Sofía
    bg_clip2 = create_color_clip(width, height, config['colors']['background'], 6)
    speaker_text = create_text_clip(
        f"ANA SOFÍA\n\n{estaciones_data['introduccion']['texto_ana']}",
        6, fontsize=32, color='white', width=width
    )
    ana_clip = CompositeVideoClip([bg_clip2, speaker_text], size=(width, height))
    clips.append(ana_clip)
    
    # Presentación Juan Diego
    bg_clip3 = create_color_clip(width, height, config['colors']['background'], 6)
    speaker_text2 = create_text_clip(
        f"JUAN DIEGO\n\n{estaciones_data['introduccion']['texto_juan']}",
        6, fontsize=32, color='white', width=width
    )
    juan_clip = CompositeVideoClip([bg_clip3, speaker_text2], size=(width, height))
    clips.append(juan_clip)
    
    return concatenate_videoclips(clips)

def generate_estaciones(config, estaciones_data, width, height):
    """Genera las 4 estaciones."""
    all_clips = []
    
    for estacion in estaciones_data['estaciones']:
        estacion_clips = []
        
        # Título de la estación
        bg_title = create_color_clip(width, height, config['colors']['background'], 2)
        title_text = create_text_clip(
            f"ESTACIÓN {estacion['numero']} - {estacion['titulo']}\n\n{estacion['pregunta']}",
            2, fontsize=48, color=estacion['color'], width=width
        )
        title_clip = CompositeVideoClip([bg_title, title_text], size=(width, height))
        estacion_clips.append(title_clip)
        
        # Contenido (simplificado para demostración)
        bg_content = create_color_clip(width, height, config['colors']['background'], 8)
        
        # Crear resumen de puntos clave
        if 'key_points' in estacion:
            content_text = "Puntos Clave:\n" + "\n".join([f"• {p}" for p in estacion['key_points'][:3]])
        elif 'competencias' in estacion:
            content_text = "Competencias:\n" + "\n".join([f"• {c}" for c in estacion['competencias'][:4]])
        elif 'grupos_investigacion' in estacion:
            content_text = "Recursos:\n" + "\n".join([f"• {g}" for g in estacion['grupos_investigacion']])
        else:
            content_text = "Responsabilidades:\n" + "\n".join([f"• {r}" for r in estacion['responsabilidades'][:4]])
        
        content_text_clip = create_text_clip(content_text, 8, fontsize=36, color='white', width=width)
        content_clip = CompositeVideoClip([bg_content, content_text_clip], size=(width, height))
        estacion_clips.append(content_clip)
        
        all_clips.append(concatenate_videoclips(estacion_clips))
    
    return concatenate_videoclips(all_clips)

def generate_solution(config, estaciones_data, width, height):
    """Genera la sección de solución."""
    clips = []
    
    solucion = estaciones_data['solucion_final']
    
    # Título de la solución
    bg_clip = create_color_clip(width, height, config['colors']['background'], 3)
    title_text = create_text_clip(
        f"PRESENTACIÓN DE LA SOLUCIÓN\n\n{solucion['nombre']}",
        3, fontsize=56, color='#fbbf24', width=width
    )
    title_clip = CompositeVideoClip([bg_clip, title_text], size=(width, height))
    clips.append(title_clip)
    
    # Descripción
    bg_desc = create_color_clip(width, height, config['colors']['background'], 6)
    desc_text = create_text_clip(
        solucion['descripcion'] + "\n\nCaracterísticas:\n" + 
        "\n".join([f"✓ {c}" for c in solucion['caracteristicas'][:3]]),
        6, fontsize=32, color='white', width=width
    )
    desc_clip = CompositeVideoClip([bg_desc, desc_text], size=(width, height))
    clips.append(desc_clip)
    
    return concatenate_videoclips(clips)

def generate_closing(config, estaciones_data, width, height):
    """Genera el cierre."""
    clips = []
    cierre = estaciones_data['cierre']
    
    # Reflexión 1
    bg_clip1 = create_color_clip(width, height, config['colors']['background'], 5)
    text1 = create_text_clip(cierre['reflexion_1'], 5, fontsize=40, color='#22c55e', width=width)
    clip1 = CompositeVideoClip([bg_clip1, text1], size=(width, height))
    clips.append(clip1)
    
    # Reflexión 2
    bg_clip2 = create_color_clip(width, height, config['colors']['background'], 5)
    text2 = create_text_clip(cierre['reflexion_2'], 5, fontsize=40, color='#3b82f6', width=width)
    clip2 = CompositeVideoClip([bg_clip2, text2], size=(width, height))
    clips.append(clip2)
    
    # Mensaje final
    bg_clip3 = create_color_clip(width, height, config['colors']['background'], 5)
    text3 = create_text_clip(cierre['mensaje_final'], 5, fontsize=44, color='#fbbf24', width=width)
    clip3 = CompositeVideoClip([bg_clip3, text3], size=(width, height))
    clips.append(clip3)
    
    # Agradecimiento
    bg_clip4 = create_color_clip(width, height, config['colors']['background'], 3)
    text4 = create_text_clip("¡Gracias por acompañarnos\nen nuestro viaje profesional!", 3, fontsize=48, color='white', width=width)
    clip4 = CompositeVideoClip([bg_clip4, text4], size=(width, height))
    clips.append(clip4)
    
    return concatenate_videoclips(clips)

def main():
    """Función principal."""
    print("🎬 El Viaje Profesional - Video Generator")
    print("=" * 60)
    
    # Cargar configuración
    print("\n📋 Cargando configuración...")
    config = load_config(CONFIG_PATH)
    estaciones_data = load_estaciones(ESTACIONES_PATH)
    
    width = config['video']['width']
    height = config['video']['height']
    fps = config['video']['fps']
    
    print(f"✓ Resolución: {width}x{height} @ {fps}fps")
    
    # Crear directorio de salida
    ensure_dir(OUTPUT_DIR)
    
    # Generar partes del video
    print("\n🎨 Generando secciones del video...")
    
    print("  → Introducción...")
    intro = generate_intro(config, estaciones_data, width, height)
    
    print("  → Estaciones...")
    estaciones = generate_estaciones(config, estaciones_data, width, height)
    
    print("  → Solución...")
    solucion = generate_solution(config, estaciones_data, width, height)
    
    print("  → Cierre...")
    cierre = generate_closing(config, estaciones_data, width, height)
    
    # Combinar todas las secciones
    print("\n🔗 Combinando video...")
    video_final = concatenate_videoclips([intro, estaciones, solucion, cierre])
    
    # Guardar video
    output_path = OUTPUT_DIR / 'el_viaje_profesional.mp4'
    print(f"\n💾 Guardando video en: {output_path}")
    print("   (Esto puede tardar varios minutos...)")
    
    video_final.write_videofile(
        str(output_path),
        fps=fps,
        codec=config['output']['codec'],
        audio_codec='aac',
        verbose=False,
        logger=None
    )
    
    print("\n✅ ¡Video generado exitosamente!")
    print(f"📍 Ubicación: {output_path}")
    print(f"⏱️  Duración total: {video_final.duration:.0f} segundos ({video_final.duration/60:.1f} minutos)")
    
    return str(output_path)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
