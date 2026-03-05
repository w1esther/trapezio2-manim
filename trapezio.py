from manim import *
import numpy as np

class AreaTrapezio(MovingCameraScene):
    def construct(self):

        grupo_trapezio1 = VGroup()
        
        ponto1 = np.array([-1, 2, 0])
        ponto2 = np.array([2, 2, 0])
        ponto3 = np.array([-2, 0, 0])
        ponto4 = np.array([4, 0, 0])
        ponto5 = np.array([-1, 0, 0])

        label_trapezio = MathTex(r'Trapezio')
        label_trapezio.shift(3.2*UP + 0.5*RIGHT)

        trapezio = Polygon(ponto1, ponto2, ponto4, ponto3, color=PINK)
        trapezio.set_fill(color=PINK, opacity=0.4)

        base_maior = Line(ponto3, ponto4, color=RED)
        base_menor = Line(ponto1, ponto2, color=ORANGE)
        
        altura = Line(ponto1, ponto5)

        grupo_trapezio1.add(trapezio, base_maior, base_menor, altura)


        self.play(Create(grupo_trapezio1), FadeIn(label_trapezio))

        self.wait(2)

        label_base_maior = MathTex("B_{baseMaior}", color=RED)
        label_base_maior.shift(0.4*DOWN + 0.5*RIGHT).scale(0.8)

        label_base_menor = MathTex("b_{baseMenor}", color=ORANGE)
        label_base_menor.shift(2.4*UP + 0.5*RIGHT).scale(0.8)

        label_altura = MathTex("h_{altura}")
        label_altura.shift(1*UP + 0.2*LEFT).scale(0.8)

        self.play(Write(label_base_maior), Write(label_base_menor), Write(label_altura))

        self.wait(2)

        self.play(FadeOut(altura), FadeOut(label_altura))

        diagonal = Line(ponto3, ponto2)

        self.play(Create(diagonal))

        self.wait(2)

        triangulo1 = Polygon(ponto3, ponto1, ponto2, color=PURE_BLUE)
        triangulo1.set_fill(color=PURE_BLUE, opacity=0.4)

        triangulo2 = Polygon(ponto3, ponto2, ponto4, color=BLUE_A)
        triangulo2.set_fill(color=BLUE_A, opacity=0.4)

        t1 = MathTex(r'T1')
        t1.shift(1*UP + 1*LEFT)
        t2 = MathTex(r'T2')
        t2.shift(1*UP + 1.5*RIGHT)

        self.play(FadeIn(triangulo1), FadeIn(t1), FadeIn(triangulo2), FadeIn(t2))

        self.wait(2)

        self.play(self.camera.frame.animate.scale(1.5).shift(1.*DOWN))

        self.wait(2)

        area_trapezio = MathTex(r'AreaTrapezio')
        area_trapezio.shift(1.7*DOWN + 0.5*RIGHT)

        soma_areas = MathTex(r'A_{T1} + A_{T2}')
        soma_areas.shift(2.7*DOWN + 0.5*RIGHT)

        self.play(FadeIn(area_trapezio), FadeIn(soma_areas))

        self.wait(2)