from manim import *
from gtts import gTTS
import os
import numpy as np

# ---------- AI Voice ----------
voice_text = """
Atoms are made of a nucleus and electrons.
The nucleus contains protons and neutrons.
Electrons move around the nucleus in energy levels called shells.
Each shell has a fixed energy.
Electrons can jump between levels by gaining or losing energy.
This structure explains many properties of matter.
"""

audio_file = "atomic_voice.mp3"
if not os.path.exists(audio_file):
    gTTS(text=voice_text).save(audio_file)

# ---------- Scene ----------
class AtomicStructure(Scene):
    def construct(self):
        self.camera.background_color = "#0f172a"  # dark cinematic

        self.add_sound(audio_file)

        # ---------- Title ----------
        title = Text("Atomic Structure", font_size=42, color=BLUE)
        self.play(FadeIn(title, shift=UP), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(title))

        # ---------- Nucleus ----------
        nucleus = VGroup()
        for i in range(8):
            p = Dot(radius=0.08, color=RED).shift(np.random.uniform(-0.2,0.2,3))
            n = Dot(radius=0.08, color=GRAY).shift(np.random.uniform(-0.2,0.2,3))
            nucleus.add(p, n)

        nucleus.move_to(ORIGIN)
        self.play(FadeIn(nucleus), run_time=2)

        # ---------- Shells ----------
        shell1 = Circle(radius=1.2, color=BLUE)
        shell2 = Circle(radius=2.0, color=BLUE_A)
        shell3 = Circle(radius=2.8, color=BLUE_D)

        self.play(Create(shell1), Create(shell2), Create(shell3), run_time=2)

        # ---------- Electrons ----------
        e1 = Dot(color=YELLOW).move_to(shell1.point_at_angle(0))
        e2 = Dot(color=YELLOW).move_to(shell1.point_at_angle(PI))
        e3 = Dot(color=YELLOW).move_to(shell2.point_at_angle(PI/2))
        e4 = Dot(color=YELLOW).move_to(shell3.point_at_angle(PI/3))

        electrons = VGroup(e1, e2, e3, e4)
        self.play(FadeIn(electrons), run_time=2)

        # ---------- Orbit Animation ----------
        self.play(
            Rotate(e1, angle=TAU, about_point=ORIGIN),
            Rotate(e2, angle=TAU, about_point=ORIGIN),
            Rotate(e3, angle=TAU, about_point=ORIGIN),
            Rotate(e4, angle=TAU, about_point=ORIGIN),
            run_time=6
        )

        # ---------- Energy Level Jump ----------
        jump_arrow = Arrow(e1.get_center(), shell2.point_at_angle(0), color=GREEN)
        self.play(GrowArrow(jump_arrow), run_time=1)

        self.play(e1.animate.move_to(shell2.point_at_angle(0)), run_time=2)
        self.play(FadeOut(jump_arrow))

        # Glow effect (energy absorption)
        glow = Circle(radius=0.2, color=YELLOW).move_to(e1)
        self.play(FadeIn(glow), run_time=0.5)
        self.play(FadeOut(glow), run_time=0.5)

        # ---------- Labels ----------
        label = Text("Electrons occupy energy levels (shells)", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(label))
        self.wait(3)

        # ---------- Ending ----------
        self.play(FadeOut(label))
        final = Text("Atomic Structure Defines Matter", font_size=36, color=BLUE)
        self.play(FadeIn(final))
        self.wait(3)

# ---------- Render ----------
if __name__ == "__main__":
    os.system("manim -pqh atomic.py AtomicStructure")
