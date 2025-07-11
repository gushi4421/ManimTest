"""

manim -pql Manim.py Test

"""

from manim import *
import numpy as np


class Test(Scene):
    def construct(self):
        #开头
        begin_title=Text("定 积 分",font_size=90,color=BLUE)
        little_title=Text("Manim动画演示",font_size=30,color=BLUE).shift(DOWN*1.0)

        self.play(Write(begin_title),run_time=2.0)
        self.wait(1.5)
        self.play(Write(little_title),run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(begin_title),FadeOut(little_title),run_time=2.0)
        self.wait(1.5)

        #----------第一部分----------#
        #标题
        first_title=Text("1.积分的几何意义",font_size=90,color=BLUE)

        self.play(Write(first_title),run_time=2.5)
        self.wait(1.5)
        self.play(FadeOut(first_title),run_time=1.5)
        self.wait(1.5)

        #第一个示例
        #坐标轴
        axes1=Axes(
            x_range=[0.0,10.0,1.0],
            y_range=[0.0,5.0,1.0],
            x_length=11,
            y_length=7,
            axis_config={
                "include_tip":True,
                "include_numbers":False,
                "include_ticks":False
            }
        )
        axes1.move_to(ORIGIN)
        #x，y轴的标签
        x_label=axes1.get_x_axis_label("x")
        y_label=axes1.get_y_axis_label("y")

        self.play(Create(axes1),run_time=2.0)
        self.wait(1.5)
        self.play(Write(x_label),Write(y_label),run_time=1)
        self.wait(1.5)
        #示例函数
        def function1(x):
            return 3
        func1=axes1.plot(function1,x_range=[0.0,8.0],stroke_width=4.0,color=BLUE)
        func1_label=MathTex(r"f(x) = 3",font_size=50,color=BLUE).shift(UP*2+RIGHT)
        area1=axes1.get_area(   #填充操作，填充区域即为积分的几何意义
            graph=func1,
            x_range=[0,8],
            color=BLUE,
            opacity=0.4
        )
        #func1在坐标轴上的标签
        x_8_label=MathTex("8",font_size=40).next_to(axes1.c2p(8,0),DOWN)
        y_3_label=MathTex("3",font_size=40).next_to(axes1.c2p(0,3),LEFT)
        #积分计算的值
        integral_func1=MathTex(r"\int_{0}^{8} 3 \,dx = 24",font_size=50,color=YELLOW)
        integral_func1.to_edge(UP)
        dashed_line1 = DashedLine(      #x=8的虚线
            start=axes1.c2p(8, function1(8)),
            end=axes1.c2p(8, 0),
            color=YELLOW,
            stroke_width=2
        )

        self.wait(1.5)
        self.play(Create(func1),Write(func1_label),run_time=2.0)
        self.wait(1.5)
        self.play(FadeOut(func1_label),run_time=1)
        self.play(Create(dashed_line1),run_time=1.5)
        self.wait(1.5)
        self.play(Write(x_8_label),Write(y_3_label),run_time=1.0)
        self.wait(1.5)
        self.play(FadeIn(area1),run_time=2.0)
        self.wait(1.5)
        self.play(Write(integral_func1),run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(func1),FadeOut(area1),FadeOut(integral_func1),FadeOut(dashed_line1),FadeOut(x_8_label),FadeOut(y_3_label),run_time=2.5)
        self.wait(1.5)

        #第二个示例
        def function2(x):
            return 0.08*x**2    #为了做出视觉效果，才乘0.08

        func2=axes1.plot(function2,x_range=[0.0,8.0],stroke_width=4.0,color=BLUE)
        func2_label=MathTex(r"f(x) = x^2",font_size=50,color=BLUE).shift(UP*2+RIGHT)
        area2 = axes1.get_area(     #填充
            graph=func2,
            x_range=[0, 8],
            color=BLUE,
            opacity=0.4
        )
        x_1_label=MathTex("1",font_size=40).next_to(axes1.c2p(8,0),DOWN)
        integral_func2=MathTex(r"\int_{0}^{1} x^2 \,dx = \frac{1}{3}",font_size=50,color=YELLOW)
        integral_func2.move_to(UP*2)
        dashed_line2 = DashedLine(
                start=axes1.c2p(8, function2(8)),
                end=axes1.c2p(8, 0),
                color=YELLOW,
                stroke_width=2
            )

        self.play(Create(func2),Write(func2_label),run_time=2.0)
        self.wait(1.5)
        self.play(FadeOut(func2_label),run_time=1)
        self.wait(1.5)
        self.play(Create(dashed_line2),run_time=1.5)
        self.wait(1)
        self.play(Write(x_1_label),run_time=1)
        self.wait(1.5)
        self.play(FadeIn(area2),run_time=1)
        self.wait(1.5)
        self.play(Write(integral_func2),run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(func2),FadeOut(area2),FadeOut(integral_func2),FadeOut(dashed_line2),FadeOut(x_1_label),run_time=2.5)
        self.wait(1.5)
        self.play(FadeOut(axes1),FadeOut(x_label),FadeOut(y_label))
        self.wait(2.0)

        #----------第二部分---------#
        #标题
        second_title=Text("2.黎曼和求定积分",font_size=90,color=BLUE)

        self.play(Write(second_title),run_time=2.5)
        self.wait(1.5)
        self.play(FadeOut(second_title),run_time=1.5)
        self.wait(1.5)

        #仍以y=x^2为例，仍使用坐标轴axes1
        x_label = axes1.get_x_axis_label("x")
        y_label = axes1.get_y_axis_label("y")

        self.play(Create(axes1), run_time=2.0)
        self.wait(1.5)
        self.play(Write(x_label), Write(y_label), run_time=1)
        self.wait(1.5)
        self.play(Create(func2), Write(func2_label), run_time=2.0)
        self.wait(1.5)
        self.play(FadeOut(func2_label),run_time=1)
        self.wait(1.5)
        self.play(Create(dashed_line2),run_time=1)
        self.wait(1)
        self.play(Write(x_1_label), run_time=1.0)
        self.wait(1.5)
        self.play(Write(integral_func2),run_time=2)
        self.wait(1.5)
        self.play(FadeOut(integral_func2),run_time=2)
        self.wait(1.5)

        #选取矩形的个数
        num_rectangle=[4,8,16,32,64]
        last_rectangles=None        #利用current与last进行迭代
        for i,n in enumerate(num_rectangle):
            width=8/n       #创建矩形的宽
            rectangles=VGroup()     #用VGroup管理大量矩形
            riemann_sum=0       #矩形的面积之和
            for j in range (n):
                x_left=j*width      #计算矩形在坐标轴中左端点的坐标
                x_right=x_left+width        #右端坐标
                height=function2(x_right)       #计算矩形的高
                rectangle=Rectangle(        #创建矩形
                    height=height*axes1.y_axis.unit_size,       #*axes1.y_axis.unit_size获得在屏幕上的应有高度
                    width=width*axes1.x_axis.unit_size,
                    stroke_width=1,
                    stroke_color=WHITE,
                    fill_color=RED,
                    fill_opacity=0.4
                )
                riemann_sum += width*height
                rectangle.move_to(axes1.c2p(x_left+width/2,height/2))   #移至坐标轴上
                rectangles.add(rectangle)       #添加进VGroup中实行批量管理

            sum_text=MathTex(f"\\text{{Riemann Sum}} = {riemann_sum/40:.2f}",font_size=40,color=YELLOW).to_edge(UP)
            if i==0:
                last_rectangles=rectangles
                self.play(FadeIn(last_rectangles),run_time=1.5)
            else:
                current_rectangles=rectangles
                self.play(ReplacementTransform(last_rectangles,current_rectangles),run_time=1)
                last_rectangles=current_rectangles

            self.wait(1)
            self.play(Write(sum_text), run_time=1)
            self.wait(1)
            self.play(FadeOut(sum_text), run_time=1)
            self.wait(1)

        area4=axes1.get_area(
            graph=func2,
            x_range=[0,8],
            color=RED,
            opacity=0.4
        )
        #数学公式的书写与化简
        riemann_label1=MathTex(r"Riemann Sum = \lim_{n\to\infty} \frac{1}{n}*\frac{1}{n}^2+\frac{1}{n}*\frac{2}{n}^2+\cdots",font_size=40,color =YELLOW).to_edge(UP)
        riemann_label2=MathTex(r"Riemann Sum = \lim_{n\to\infty} \frac{1}{n^3} \sum_{i=1}^{n} i^2",font_size=40,color=YELLOW).to_edge(UP)
        riemann_label3=MathTex(r"Riemann Sum = \lim_{n\to\infty} \frac{1}{n^3} \cdot \frac{n(n+1)(2n+1)}{6}",font_size=40,color=YELLOW).to_edge(UP)
        riemann_label4=MathTex(r"Riemann Sum = \frac{1}{3}",font_size=40,color=YELLOW).to_edge(UP)

        self.play(FadeOut(current_rectangles),run_time=1.5)
        self.wait(1.5)
        self.play(FadeIn(area4),run_time=1.5)
        self.wait(1.5)
        self.play(Write(riemann_label1),run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(riemann_label1,riemann_label2), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(riemann_label2,riemann_label3), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(riemann_label3, riemann_label4), run_time=2)
        self.wait(2)
        self.play(FadeOut(func2),FadeOut(area4),FadeOut(x_1_label),FadeOut(riemann_label4),FadeOut(dashed_line2),run_time=2)
        self.wait(1)
        self.play(FadeOut(axes1),FadeOut(x_label),FadeOut(y_label),run_time=1.5)
        self.wait(1.5)

        axes2=Axes(
            x_range=[-5, 8, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=12,
            y_length=8,
            axis_config={
                "include_tip": True,
                "include_numbers": False,
                "include_ticks": False
            }
        )
        axes2.move_to(ORIGIN)
        x_label=axes2.get_x_axis_label("x")
        y_label=axes2.get_y_axis_label("y")

        self.play(Create(axes2), run_time=2.0)
        self.wait(1)
        self.play(Write(x_label), Write(y_label), run_time=1.0)
        self.wait(1.5)

        #示例函数，抛传引玉，引出牛顿-莱布尼茨公式
        def function3(x):
            return np.sin(x)

        func3=axes2.plot(function3,x_range=[-5,7],stroke_width=4.0,color=BLUE)
        func3_label=MathTex(r"f(x) = \sin(x)",font_size=50,color=BLUE).shift(UP*2+RIGHT)
        area3=axes2.get_area(
            graph=func3,
            x_range=[-5,7],
            color=BLUE,
            opacity=0.4
        )
        x_a_label=MathTex("a",font_size=40).next_to(axes2.c2p(-5,0),DOWN)
        x_b_label=MathTex("b",font_size=40).next_to(axes2.c2p(7,0),DOWN)
        integral_func3=MathTex(r"\int_{a}^{b} \sin(x) \,dx = ?", font_size=50, color=YELLOW)
        integral_func3.move_to(UP * 2)
        x_points3 = [-5, 7]  # 对应x=a和x=b处的标签
        dashed_lines3=VGroup()

        for x in x_points3:
            line=DashedLine(
                start=axes2.c2p(x, function3(x)),
                end=axes2.c2p(x, 0),
                color=YELLOW,
                stroke_width=2
            )
            dashed_lines3.add(line)

        self.play(Create(func3),Write(func3_label),run_time=2)
        self.wait(1.5)
        self.play(FadeOut(func3_label),run_time=1)
        self.play(Create(dashed_lines3),run_time=1.5)
        self.wait(1.5)
        self.play(Write(x_a_label),Write(x_b_label),run_time=1)
        self.wait(1.5)
        self.play(FadeIn(area3), run_time=1)
        self.wait(1.5)
        self.play(Write(integral_func3), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(func3), FadeOut(area3), FadeOut(integral_func3),FadeOut(x_a_label),FadeOut(x_b_label),FadeOut(dashed_lines3),FadeOut(axes2), FadeOut(x_label), FadeOut(y_label), run_time=2.5)
        self.wait(3)

        #----------第三部分---------#
        third_title=Text("3.牛顿-莱布尼茨公式", font_size=90, color=BLUE)

        self.play(Write(third_title), run_time=2.5)
        self.wait(1)
        self.play(FadeOut(third_title), run_time=1.5)
        self.wait(1.5)

        #在屏幕中显现上下两个坐标轴，分别代表原函数与导函数
        axes3=Axes(
            x_range=[0, 4, 1],
            y_range=[0, 26, 2],
            x_length=6,
            y_length=3.2,
            axis_config={
                "include_tip": True,
                "include_numbers": False,
                "include_ticks": False
            }
        )
        axes4=Axes(
            x_range=[0, 4, 1],
            y_range=[0, 26, 2],
            x_length=6,
            y_length=3.2,
            axis_config={
                "include_tip": True,
                "include_numbers": False,
                "include_ticks": False
            }
        )
        axes3.shift(LEFT*2.5+UP*2.2)
        axes4.shift(LEFT*2.5+DOWN*2)

        axes3_x_label=axes3.get_x_axis_label("x")
        axes3_y_label=axes3.get_y_axis_label("y")
        axes4_x_label=axes4.get_x_axis_label("x")
        axes4_y_label=axes4.get_y_axis_label("y")

        self.play(Create(axes3), Create(axes4), run_time=2)
        self.wait(1.5)
        self.play(Write(axes3_x_label), Write(axes3_y_label), Write(axes4_x_label), Write(axes4_y_label), run_time=1)
        self.wait(1.5)

        def f(x):   #导函数f
            return 2*(x+0.5) ** 2

        def F(x):   #原函数F
            return 2 / 3 * (x+0.5) ** 3

        Func4=axes3.plot(F, x_range=[0, 3.5], stroke_width=4, color=BLUE)
        Func4_label=MathTex(r"F(x)", font_size=40, color=RED).shift(UP * 3 + LEFT * 6.5)
        func4=axes4.plot(f, x_range=[0, 3.5], stroke_width=4, color=BLUE)
        func4_label=MathTex(r"f(x)", font_size=40, color=RED).shift(DOWN + LEFT * 6.5)

        self.play(Create(func4), Create(Func4), run_time=2)
        self.wait(1.5)
        self.play(Write(func4_label), Write(Func4_label), run_time=2)
        self.wait(1.5)

        # 创建ValueTracker控制切线位置
        x_tracker=ValueTracker(1)   #控制从x=1开始滑动
        tangent_length=1.5

        # 创建切线函数
        def get_tangent_line():
            x=x_tracker.get_value()     #获取当前x的值
            slope=f(x)      #计算x处的切线值
            x_scale=axes3.get_x_unit_size()
            y_scale=axes3.get_y_unit_size()
            screen_slope=slope * (y_scale / x_scale)    #计算斜率
            angle=np.arctan(screen_slope)       #计算斜率对应的角度
            center=axes3.c2p(x, F(x))   #获取坐标点
            return Line(
                start=center-np.array([np.cos(angle),np.sin(angle), 0])*tangent_length,
                end=center+np.array([np.cos(angle),np.sin(angle), 0])*tangent_length,
                color=RED,
                stroke_width=3
            )

        tangent_line=always_redraw(get_tangent_line)        #创建动态的切线对象

        # 创建切线的滑动轨迹
        trace_path=VMobject(color=RED, stroke_width=4, stroke_opacity=1)
        trace_path.set_points_as_corners([axes3.c2p(1, F(1)), axes3.c2p(1, F(1))])

        #切线轨迹
        def update_trace_path(path):
            x=x_tracker.get_value()     #获取当前x的值
            y=F(x)      #计算当前函数值
            new_point=axes3.c2p(x, y)
            # 仅当移动距离足够大时添加新点
            if np.linalg.norm(new_point-path.points[-1])>0.05:
                path.add_smooth_curve_to(new_point)

        trace_path.add_updater(update_trace_path)

        # 创建垂直线段和填充区域
        vertical_tracker=ValueTracker(1)

        # 垂直线段
        vertical_line=always_redraw(
            lambda:Line(
                start=axes4.c2p(vertical_tracker.get_value(), 0),
                end=axes4.c2p(vertical_tracker.get_value(), f(vertical_tracker.get_value())),
                color=GREEN,
                stroke_width=3))

        # 填充区域（精确匹配函数曲线）
        fill_area=always_redraw(
            lambda:axes4.get_area(
                graph=func4,
                x_range=[1, vertical_tracker.get_value()],
                color=GREEN,
                opacity=0.4))

        # 添加填充区域、垂直线段、轨迹和切线
        self.play(Create(tangent_line),Create(fill_area),Create(vertical_line),Create(trace_path),run_time=2)
        self.wait(1.5)

        # 同时播放两个动画
        self.play(x_tracker.animate.set_value(3),vertical_tracker.animate.set_value(3),run_time=4,rate_func=linear)
        self.wait(2)
        self.play(FadeOut(tangent_line),FadeOut(vertical_line),run_time=2)
        self.wait(2)

        # 移除轨迹的更新器，防止其继续变化
        trace_path.remove_updater(update_trace_path)

        # 创建高度差直线（F(b)-F(a)）
        height_difference=Line(
            start=axes3.c2p(3, F(1)),
            end=axes3.c2p(3, F(3)),
            color=RED,
            stroke_width=6)

        # 创建轨迹副本和高度差的副本（用于右侧显示）
        trace_copy=trace_path.copy()
        height_copy=height_difference.copy()

        # 创建填充区域的副本
        fill_copy=fill_area.copy()

        # 将副本移动到右侧
        self.play(Transform(trace_copy, height_copy.copy().shift(RIGHT * 4.5)),fill_copy.animate.shift(RIGHT * 6),run_time=3)
        self.wait(1.5)

        # 在两者之间添加竖着的等号（用两个矩形表示）
        trace_center=trace_copy.get_center()
        fill_center=fill_copy.get_center()
        equals_position=(trace_center + fill_center) / 2

        bar1=Rectangle(
            width=0.04,
            height=0.7,
            color=WHITE,
            fill_opacity=1
        )
        bar2=bar1.copy()

        bar1.move_to(equals_position+LEFT*0.15)
        bar2.move_to(equals_position+RIGHT*0.15)

        vertical_equals=VGroup(bar1, bar2)

        self.play(FadeIn(vertical_equals),run_time=1.5)
        self.wait(2)

        save_1=VGroup()     #保存状态
        save_1.add(fill_copy,trace_copy,vertical_equals)

        self.play(
            FadeOut(fill_area),
            FadeOut(trace_path),
            FadeOut(fill_copy),
            FadeOut(trace_copy),
            FadeOut(vertical_equals),
            run_time=2
        )
        self.wait(1.5)

        # 添加虚线标记
        x_points=[0.7, 1.4, 2.1, 2.8]
        lines=VGroup()
        for x in x_points:
            # 顶部坐标系（原函数）
            line_top=DashedLine(
                start=axes3.c2p(x, F(x)),
                end=axes3.c2p(x, 0),
                color=YELLOW,
                stroke_width=2
            )

            # 底部坐标系（导函数）
            line_bottom=DashedLine(
                start=axes4.c2p(x, f(x)),
                end=axes4.c2p(x, 0),
                color=YELLOW,
                stroke_width=2
            )

            lines.add(line_top, line_bottom)

        # 添加虚线动画
        self.play(Create(lines), run_time=2)
        self.wait(2)

        # 在Func4上添加直角三角形（保留Δx和Δy标签）并用方框圈起来
        def create_triangle_with_labels():
            elements=VGroup()

            # 选择x=2.1作为起点
            x_start=2.1
            x_end=2.8

            # 计算起点和终点的函数值
            y_start=F(x_start)
            y_end=F(x_end)

            # 创建三个点
            start_point=axes3.c2p(x_start, y_start)
            mid_point=axes3.c2p(x_end, y_start)
            end_point=axes3.c2p(x_end, y_end)

            # 创建水平边（Δx）
            dx_line=Line(
                start=start_point,
                end=mid_point,
                color=GREEN,
                stroke_width=3
            )

            # 创建Δx标签
            dx_label=MathTex(r"\Delta x", font_size=30, color=GREEN)
            dx_label.next_to(dx_line, DOWN, buff=0.1)

            # 创建垂直边（Δy）
            dy_line=Line(
                start=mid_point,
                end=end_point,
                color=RED,
                stroke_width=3
            )

            # 创建Δy标签
            dy_label=MathTex(r"\Delta y", font_size=40, color=RED)
            dy_label.next_to(dy_line, RIGHT, buff=0.1)

            # 创建斜边
            hypotenuse=Line(
                start=start_point,
                end=end_point,
                color=YELLOW,
                stroke_width=3
            )

            # 创建方框
            box=Rectangle(
                width=0.7*axes3.get_x_unit_size()+0.6,
                height=0.7*axes3.get_y_unit_size()+0.6,
                color=YELLOW,
                stroke_width=3,
                fill_opacity=0
            )

            # 将方框定位在三角形的中心
            box.move_to(axes3.c2p((x_start + x_end) / 2, (y_start + y_end) / 2))

            # 将元素组合
            elements.add(dx_line, dy_line, hypotenuse, dx_label, dy_label, box)

            return elements

        # 创建直角三角形和方框
        triangle_with_labels = create_triangle_with_labels()

        # 添加动画（分步骤展示）
        self.play(Create(triangle_with_labels[0]), run_time=1)  # 水平边
        self.wait(1)

        self.play(Create(triangle_with_labels[1]), run_time=1)  # 垂直边
        self.wait(1)

        self.play(Create(triangle_with_labels[2]), run_time=1.5)  # 斜边
        self.wait(1)
        self.play(Write(triangle_with_labels[4]),Write(triangle_with_labels[3]), run_time=2)
        self.wait(1)

        # 最后添加方框
        self.play(Create(triangle_with_labels[5]), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(triangle_with_labels[0]),FadeOut(triangle_with_labels[2]),FadeOut(triangle_with_labels[3]),FadeOut(triangle_with_labels[5]),run_time=2)

        point_xi=2.5    #作为中值点
        dot_xi=Dot(
            point=axes3.c2p(point_xi,F(point_xi)),
            color=RED,
            radius=0.08
        )
        line_xi1=DashedLine(
            start=axes3.c2p(point_xi, F(point_xi)),
                end=axes3.c2p(point_xi, 0),
                color=BLUE,
                stroke_width=2
        )
        line_xi2=Line(
            start=axes4.c2p(point_xi, F(point_xi)),
                end=axes4.c2p(point_xi, 0),
                color=BLUE,
                stroke_width=2
        )
        dot_xi_label=MathTex(r"\xi",font_size=40,color=BLUE).next_to(line_xi1,DOWN)
        line_label=MathTex(r"f(\xi)",font_size=40,color=BLUE).next_to(dot_xi_label,RIGHT+DOWN*7)
        temp_label1=MathTex(r" = \Delta x*F'(\xi)",font_size=40,color=YELLOW).next_to(triangle_with_labels[4],RIGHT*0.2)
        temp_label2=MathTex(r" = \Delta x*f(\xi)",font_size=40,color=YELLOW).next_to(triangle_with_labels[4],RIGHT*0.2)

        def xi_tangent_line():
            slope=f(point_xi)
            x_scale = axes3.get_x_unit_size()
            y_scale = axes3.get_y_unit_size()
            screen_slope = slope * (y_scale / x_scale)
            angle = np.arctan(screen_slope)
            center = axes3.c2p(point_xi, F(point_xi))
            tangent_length=1  # 切线长度

            # 创建切线
            tangent_line=Line(
                start=center - np.array([np.cos(angle), np.sin(angle), 0]) * tangent_length,
                end=center + np.array([np.cos(angle), np.sin(angle), 0]) * tangent_length,
                color=RED,
                stroke_width=3
            )
            return tangent_line
        tangent_xi=xi_tangent_line()
        rectangle_xi=Rectangle(
            width=0.7*axes4.get_x_unit_size(),
            height=f(2.5)*axes4.get_y_unit_size(),
            color=BLUE,
            fill_opacity=1
        ).move_to(axes4.c2p(2.45,f(2.5)/2))
        dengyu_label=MathTex(r" = ",font_size=40).next_to(triangle_with_labels[4],RIGHT*0.2)

        self.play(Create(dot_xi),run_time=1)
        self.wait(1)
        self.play(Create(tangent_xi),run_time=1.5)
        self.wait(1.5)
        self.play(Create(line_xi1),Write(dot_xi_label),run_time=2)
        self.wait(1.5)
        self.play(Create(line_xi2),Write(line_label),run_time=1)
        self.wait(1.5)
        self.play(Write(temp_label1),run_time=2)
        self.wait(1.5)
        self.play(ReplacementTransform(temp_label1,temp_label2),run_time=2)
        self.wait(1.5)
        self.play(FadeIn(rectangle_xi),run_time=2)
        self.wait(1.5)
        self.play(FadeOut(temp_label2),run_time=2)
        self.wait(1)
        self.play(Write(dengyu_label),rectangle_xi.animate.next_to(triangle_with_labels[4],RIGHT*2),run_time=2)
        self.wait(2)

        save_2=VGroup()
        save_2.add(dengyu_label,triangle_with_labels[4],rectangle_xi)

        self.play(ReplacementTransform(save_2,save_1),run_time=2)
        self.wait(1.5)

        clear_group=VGroup()
        clear_group.add(axes3,axes4,axes3_x_label,axes3_y_label,axes4_x_label,axes4_y_label,func4,func4_label,line_label,Func4,Func4_label,lines,tangent_xi,triangle_with_labels[1],tangent_line,dot_xi_label,dot_xi,line_xi1,line_xi2,save_1)
        self.play(FadeOut(clear_group),run_time=2)
        self.wait(1)

        integral_expression=MathTex(        #牛顿莱布尼茨公式的文字表示
            r"\int_{a}^{b} f(x) \, dx = F(b) - F(a)",
            font_size=80,
            color=BLUE
        )

        self.play(FadeIn(integral_expression), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(integral_expression), run_time=1.5)
        self.wait(1.5)

        final_text=Text("感 谢 观 看!",font_size=70,color=BLUE)

        self.play(Write(final_text),run_time=2.5)
        self.wait(4)

