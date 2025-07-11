"""

manim -pql example.py ManimTest

"""


import math
from manim import *
import numpy as np


taylor_func = []    #接收函数表达式
taylor_label = []   #接收对应表达式的标签

#用循环
for degree in range(1, 12, 2):
    #泰勒degree阶的展开式
    def taylor_function(x, d=degree):
        result = 0    #对应阶数的泰勒展开式
        for n in range(0, (d + 1) // 2):
            sign = (-1) ** n    #添加项的正负
            term = sign * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)    #添加项的结束
            result += term
        return result
    taylor_func.append(taylor_function)
    #对应展开式的标签
    terms = []
    for n in range(0, (degree + 1) // 2):
        power = 2 * n + 1   #对应的阶数
        if n == 0:
            term = "x"    #初始项
        else:
            sign = "-" if n % 2 else "+"    #正负
            term = f"{sign}\\frac{{x^{{{power}}}}}{{{power}!}}"
        terms.append(term)
    formula = f"T_{{{degree}}}(x) = " + "".join(terms)      #函数的文字表示
    label = MathTex(formula,font_size=40,color=BLUE)
    label.shift(RIGHT*2)
    label.shift(UP*3)
    taylor_label.append(label)

#视频呈现
class ManimTest(Scene):
    def construct(self):
        #标题及其绘制
        first_title=Text("Taylor formula",color=BLUE)
        little_title=Text("Animation show",font_size=30,color=BLUE).shift(DOWN*0.7)
        second_title=Text("sinx",font_size=100,color=BLUE)

        self.play(Write(first_title),run_time=1.8)
        self.wait(1)
        self.play(Write(little_title),run_time=1.8)
        self.wait(1)
        self.play(FadeOut(first_title),FadeOut(little_title),font_size=90,run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(second_title),run_time=1.5)
        self.wait(1)
        self.play(FadeOut(second_title),run_time=1.5)
        self.wait(1)

        #坐标轴及其绘制
        axes=Axes(
            x_range=[-8,8,1],
            y_range=[-2,2.5,1],
            x_length=12,
            y_length=8,
            axis_config={
                "include_tip":True,
                "include_ticks":False,
                "include_numbers":False,
                "stroke_width":2.5
            })
        self.play(Create(axes), run_time=2)
        self.wait(1)

        #x轴与y轴的标签
        x_label=axes.get_x_axis_label("x")
        y_label=axes.get_y_axis_label("y")

        self.play(Write(x_label),Write(y_label),run_time=0.5)
        self.wait(1)

        #目标函数sinx的绘制
        def function(x):
            return np.sin(x)

        sin_func=axes.plot(function,stroke_width=4,color=RED)
        sin_label = MathTex(r"sin(x)", color=RED)   #函数标签
        sin_label.shift(RIGHT * 4)
        sin_label.shift(UP * 3)

        self.play(Create(sin_func),Write(sin_label),run_time=2.5)
        self.wait(2)
        self.play(FadeOut(sin_label),run_time=1.5)

        #用last与current两个变量存储前后两个泰勒展开式的表达式，后面用ReplacementTransform实现转换，达成一定的视觉效果
        last_func=axes.plot(taylor_func[0], color=BLUE)
        last_label=taylor_label[0]
        current_func=None
        current_label=None

        self.play(Create(last_func),run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(last_label),run_time=1.2)
        self.wait(1)

        #循环遍历，实现last与current的递推，绘制每阶泰勒展开式的图像
        for i in range(1, len(taylor_func)):
            if current_func is None:
                pass
            else:
                last_func=current_func
                last_label=current_label
            current_func=axes.plot(taylor_func[i], color=BLUE)
            current_label=taylor_label[i]

            self.play(FadeOut(last_label))
            self.play(ReplacementTransform(last_func,current_func),run_time=1.5)
            self.wait(0.5)
            self.play(FadeIn(current_label),run_time=1.2)
            #最后一项不进行FadeIn操作
            if i!=len(taylor_func)-1:
                self.wait(1)
        #绘制sinx的无穷阶泰勒展开式，即sinx本身，用不同颜色表示
        sin_func2 = axes.plot(function, stroke_width=4, color=BLUE)
        final_label = MathTex(r"\sin(x) \approx x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots",font_size=70,color=BLUE).shift(UP*2)

        self.wait(1.5)
        self.play(ReplacementTransform(current_func,sin_func2),run_time=1.8)
        self.play(ReplacementTransform(current_label,final_label),run_time=1.8)
        self.wait(1.5)
        self.play(FadeOut(sin_func),FadeOut(sin_func2),FadeOut(final_label),run_time=1.2)
        self.wait(0.8)
        self.play(FadeOut(axes),FadeOut(x_label),FadeOut(y_label),run_time=1.2)

        end=Text("Thank you for watching!",color=BLUE)

        self.play(Write(end),run_time=1.8)
        self.wait(3.5)
