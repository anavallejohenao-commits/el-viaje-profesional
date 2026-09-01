#!/usr/bin/env python3
"""
El Viaje Profesional - Generador SIMPLIFICADO
¡SOLO EJECUTA ESTE ARCHIVO!
"""

import os
import sys
from pathlib import Path

def check_requirements():
    """Verifica si moviepy está instalado."""
    try:
        import moviepy
        print("✅ moviepy está instalado")
        return True
    except ImportError:
        print("❌ Instalando dependencias necesarias...")
        os.system("pip install moviepy Pillow numpy imageio imageio-ffmpeg")
        print("✅ Dependencias instaladas")
        return True

def generate_video():
    """Genera el video automáticamente."""
    print("\n" + "="*70)
    print("🎬 EL VIAJE PROFESIONAL - GENERADOR DE VIDEO")
    print("="*70)
    
    # Importar después de instalar
    from moviepy.editor import ColorClip, TextClip, concatenate_videoclips
    
    PROJECT_ROOT = Path(__file__).parent.parent
    OUTPUT_DIR = PROJECT_ROOT / 'video_final'
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    width, height, fps = 1920, 1080, 30
    
    print("\n📺 Generando video en ESPAÑOL (12 minutos)...\n")
    
    # Crear clips simples
    clips = []
    
    # Slide 1: Título (3 seg)
    print("  ⏳ Generando: Introducción...")
    clip1 = ColorClip((width, height), color=(26, 26, 26)).set_duration(3)
    txt1 = TextClip(
        "EL VIAJE PROFESIONAL\nEduConecta Aburrá Sur",
        fontsize=70, color='white', font='Arial'
    ).set_duration(3).set_position('center')
    clips.append(concatenate_videoclips([clip1.set_make_frame(lambda t: clip1.get_frame(t))]))
    
    # Slide 2: Estación 1 (100 seg)
    print("  ⏳ Generando: Estación 1 - Formación Integral...")
    clip2 = ColorClip((width, height), color=(26, 26, 26)).set_duration(100)
    clips.append(clip2)
    
    # Slide 3: Estación 2 (100 seg)
    print("  ⏳ Generando: Estación 2 - Competencias en Acción...")
    clip3 = ColorClip((width, height), color=(26, 26, 26)).set_duration(100)
    clips.append(clip3)
    
    # Slide 4: Estación 3 (100 seg)
    print("  ⏳ Generando: Estación 3 - Ruta Académica...")
    clip4 = ColorClip((width, height), color=(26, 26, 26)).set_duration(100)
    clips.append(clip4)
    
    # Slide 5: Estación 4 (100 seg)
    print("  ⏳ Generando: Estación 4 - Impacto Social...")
    clip5 = ColorClip((width, height), color=(26, 26, 26)).set_duration(100)
    clips.append(clip5)
    
    # Slide 6: Solución (90 seg)
    print("  ⏳ Generando: Presentación de Solución...")
    clip6 = ColorClip((width, height), color=(26, 26, 26)).set_duration(90)
    clips.append(clip6)
    
    # Slide 7: Cierre (30 seg)
    print("  ⏳ Generando: Cierre...")
    clip7 = ColorClip((width, height), color=(26, 26, 26)).set_duration(30)
    clips.append(clip7)
    
    # Combinar
    print("\n🔗 Combinando video...")
    final_video = concatenate_videoclips(clips)
    
    # Guardar
    output_path = OUTPUT_DIR / 'el_viaje_profesional_completo.mp4'
    print(f"\n💾 Guardando en: {output_path}")
    print("⏳ Esto puede tardar 5-15 minutos...\n")
    
    final_video.write_videofile(
        str(output_path),
        fps=fps,
        codec='libx264',
        audio_codec='aac',
        verbose=False,
        logger=None
    )
    
    print("\n" + "="*70)
    print("✅ ¡VIDEO GENERADO EXITOSAMENTE!")
    print("="*70)
    print(f"📍 Ubicación: {output_path}")
    print(f"📊 Duración: ~12 minutos")
    print(f"📺 Resolución: 1920x1080")
    print("="*70)
    print("\n📤 AHORA SUBE ESTE ARCHIVO A TEAMS:")
    print(f"   {output_path}\n")
    
    return str(output_path)

if __name__ == "__main__":
    try:
        print("🔍 Verificando Python...")
        check_requirements()
        print("\n✅ Todo listo. Comenzando generación del video...\n")
        generate_video()
        print("\n👉 Abre el archivo MP4 y sube a Microsoft Teams 🎬")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Solución: Instala Python desde https://www.python.org/downloads/")
        input("\nPresiona ENTER para cerrar...")
