#!/usr/bin/env python3
"""
El Viaje Profesional - Generador de Video (12 minutos máximo)
Genera un video noticiero basado en el script de EduConecta Aburrá Sur
COMPLETAMENTE EN ESPAÑOL
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
    """Genera la introducción - 90 segundos"""
    clips = []
    
    # Título (1 segundo)
    bg_clip = create_color_clip(width, height, config['colors']['background'], 1)
    title_text = f"{estaciones_data['proyecto']['titulo']}\n{estaciones_data['proyecto']['subtitulo']}"
    title_clip = create_text_clip(title_text, 1, fontsize=64, color='#22c55e', width=width)
    intro_clip = CompositeVideoClip([bg_clip, title_clip], size=(width, height))
    clips.append(intro_clip)
    
    # Presentación Ana (20 segundos)
    bg_clip2 = create_color_clip(width, height, config['colors']['background'], 20)
    speaker_text = create_text_clip(
        f"ANA SOFÍA\n\n{estaciones_data['introduccion']['texto_ana'][:150]}...",
        20, fontsize=32, color='white', width=width
    )
    ana_clip = CompositeVideoClip([bg_clip2, speaker_text], size=(width, height))
    clips.append(ana_clip)
    
    # Presentación Juan Diego (20 segundos)
    bg_clip3 = create_color_clip(width, height, config['colors']['background'], 20)
    speaker_text2 = create_text_clip(
        f"JUAN DIEGO\n\n{estaciones_data['introduccion']['texto_juan'][:150]}...",
        20, fontsize=32, color='white', width=width
    )
    juan_clip = CompositeVideoClip([bg_clip3, speaker_text2], size=(width, height))
    clips.append(juan_clip)
    
    # Problema y Solución (49 segundos)
    bg_clip4 = create_color_clip(width, height, config['colors']['background'], 49)
    problem_text = create_text_clip(
        f"PROBLEMA:\n{estaciones_data['introduccion']['problema']}\n\nSOLUCIÓN:\n{estaciones_data['introduccion']['solucion']}",
        49, fontsize=28, color='#fbbf24', width=width
    )
    problem_clip = CompositeVideoClip([bg_clip4, problem_text], size=(width, height))
    clips.append(problem_clip)
    
    return concatenate_videoclips(clips)

def generate_estaciones(config, estaciones_data, width, height):
    """Genera las 4 estaciones - 8 minutos (2 min cada una)"""
    all_clips = []
    
    for estacion in estaciones_data['estaciones']:
        estacion_clips = []
        
        # Título y pregunta (25 segundos)
        bg_title = create_color_clip(width, height, config['colors']['background'], 25)
        title_text = create_text_clip(
            f"🔴 ESTACIÓN {estacion['numero']}\n\n{estacion['titulo']}\n\n{estacion['pregunta']}",
            25, fontsize=36, color=estacion['color'], width=width
        )
        title_clip = CompositeVideoClip([bg_title, title_text], size=(width, height))
        estacion_clips.append(title_clip)
        
        # Contenido principal (75 segundos)
        bg_content = create_color_clip(width, height, config['colors']['background'], 75)
        
        # Crear contenido específico por estación
        if estacion['numero'] == 1:
            content_text = "FORMACIÓN INTEGRAL\n\n• Conocimientos técnicos\n• Pensamiento crítico\n• Comunicación efectiva\n• Trabajo en equipo\n• Responsabilidad social"
        elif estacion['numero'] == 2:
            content_text = "COMPETENCIAS CLAVE\n\n• Trabajo en equipo\n• Comunicación asertiva\n• Lectura crítica\n• Responsabilidad ciudadana\n• Razonamiento cuantitativo"
        elif estacion['numero'] == 3:
            content_text = "RUTA ACADÉMICA\n\n• Técnica Profesional en Sistemas\n• Grupo GIISTA\n• Semillero SEIS\n• Proyecto con impacto social"
        else:
            content_text = "IMPACTO SOCIAL\n\n• Proteger datos personales\n• Garantizar inclusión\n• Pensar en medioambiente\n• Escuchar a comunidad\n• Enfoque Offline-First"
        
        content_text_clip = create_text_clip(content_text, 75, fontsize=32, color='white', width=width)
        content_clip = CompositeVideoClip([bg_content, content_text_clip], size=(width, height))
        estacion_clips.append(content_clip)
        
        all_clips.append(concatenate_videoclips(estacion_clips))
    
    return concatenate_videoclips(all_clips)

def generate_solution(config, estaciones_data, width, height):
    """Genera la sección de solución - 90 segundos"""
    clips = []
    
    solucion = estaciones_data['solucion_final']
    
    # Título (15 segundos)
    bg_clip = create_color_clip(width, height, config['colors']['background'], 15)
    title_text = create_text_clip(
        f"💻 PRESENTACIÓN DE LA SOLUCIÓN\n\n{solucion['nombre']}",
        15, fontsize=52, color='#fbbf24', width=width
    )
    title_clip = CompositeVideoClip([bg_clip, title_text], size=(width, height))
    clips.append(title_clip)
    
    # Descripción (75 segundos)
    bg_desc = create_color_clip(width, height, config['colors']['background'], 75)
    desc_text = create_text_clip(
        f"{solucion['descripcion']}\n\nCARACTERÍSTICAS:\n✓ Contenidos educativos con conexión limitada\n✓ Interfaz sencilla e inclusiva\n✓ Tecnología como herramienta de oportunidades",
        75, fontsize=28, color='white', width=width
    )
    desc_clip = CompositeVideoClip([bg_desc, desc_text], size=(width, height))
    clips.append(desc_clip)
    
    return concatenate_videoclips(clips)

def generate_closing(config, estaciones_data, width, height):
    """Genera el cierre - 30 segundos"""
    clips = []
    cierre = estaciones_data['cierre']
    
    # Mensaje final (30 segundos)
    bg_clip = create_color_clip(width, height, config['colors']['background'], 30)
    text = create_text_clip(
        f"{cierre['mensaje_final']}\n\n¡Gracias por acompañarnos\nen nuestro viaje profesional!",
        30, fontsize=40, color='#fbbf24', width=width
    )
    clip = CompositeVideoClip([bg_clip, text], size=(width, height))
    clips.append(clip)
    
    return concatenate_videoclips(clips)

def main():
    """Función principal."""
    print("🎬 El Viaje Profesional - Generador de Video")
    print("=" * 70)
    print("📺 Video Noticiero en ESPAÑOL - 12 MINUTOS MÁXIMO")
    print("=" * 70)
    
    # Cargar configuración
    print("\n📋 Cargando configuración...")
    config = load_config(CONFIG_PATH)
    estaciones_data = load_estaciones(ESTACIONES_PATH)
    
    width = config['video']['width']
    height = config['video']['height']
    fps = config['video']['fps']
    
    print(f"✓ Resolución: {width}x{height} @ {fps}fps")
    print(f"✓ Duración máxima: 12 minutos")
    print(f"✓ Formato: MP4 (H.264)")
    
    # Crear directorio de salida
    ensure_dir(OUTPUT_DIR)
    
    # Generar partes del video
    print("\n🎨 Generando secciones del video...")
    
    print("  ✓ Introducción (90 segundos)...")
    intro = generate_intro(config, estaciones_data, width, height)
    
    print("  ✓ Estación 1 - Formación Integral (100 seg)...")
    print("  ✓ Estación 2 - Competencias en Acción (100 seg)...")
    print("  ✓ Estación 3 - Ruta Académica (100 seg)...")
    print("  ✓ Estación 4 - Impacto Social (100 seg)...")
    estaciones = generate_estaciones(config, estaciones_data, width, height)
    
    print("  ✓ Solución (90 segundos)...")
    solucion = generate_solution(config, estaciones_data, width, height)
    
    print("  ✓ Cierre (30 segundos)...")
    cierre = generate_closing(config, estaciones_data, width, height)
    
    # Combinar todas las secciones
    print("\n🔗 Combinando video...")
    video_final = concatenate_videoclips([intro, estaciones, solucion, cierre])
    
    # Verificar duración
    duracion_total = video_final.duration
    minutos = int(duracion_total // 60)
    segundos = int(duracion_total % 60)
    print(f"\n⏱️  Duración total: {minutos}:{segundos:02d} ({duracion_total:.1f} segundos)")
    
    if duracion_total > 720:
        print("⚠️  ADVERTENCIA: El video excede 12 minutos")
    else:
        print("✅ El video está dentro del límite de 12 minutos")
    
    # Guardar video
    output_path = OUTPUT_DIR / 'el_viaje_profesional_completo.mp4'
    print(f"\n💾 Guardando video en:")
    print(f"   {output_path}")
    print("\n⏳ Procesando... (esto puede tardar 3-10 minutos)")
    
    video_final.write_videofile(
        str(output_path),
        fps=fps,
        codec=config['output']['codec'],
        audio_codec='aac',
        verbose=False,
        logger=None
    )
    
    print("\n" + "=" * 70)
    print("✅ ¡VIDEO GENERADO EXITOSAMENTE!")
    print("=" * 70)
    print(f"📍 Ubicación: {output_path}")
    print(f"⏱️  Duración: {minutos}:{segundos:02d}")
    print(f"📺 Resolución: {width}x{height}")
    print(f"🎬 Fps: {fps}")
    print("=" * 70)
    
    return str(output_path)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
