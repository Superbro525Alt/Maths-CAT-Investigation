import sys
import os
import pygame

import tailwind.window
import tailwind.util as util
import tailwind.widgets


if __name__ == '__main__':
    def onTick(_window: tailwind.window.Window, *args, **kwargs):
        pass

    def calculate():
        print("Calculating")

    props = util.WindowProperties(size=util.resolution(800, 500), dynamic_scaling=True, dev_resolution=util.resolution(1920, 1080))

    window = tailwind.window.Window(None, "Maths CAT Investigation", props, embed=True,
                                    debug=True, onTick=onTick)

    label = tailwind.widgets.Label(window, "Vertexes in an anticlockwise order", util.Style.empty(), {}, {})

    window.add_widget(label, util.PlaceData(0.2, 0.1, util.CenterAnchor().get_anchor()))

    vertex1 = tailwind.widgets.Entry(window, "Vertex 1 (x, y)", util.Style.empty(), {}, {})

    window.add_widget(vertex1, util.PlaceData(0.2, 0.2, util.CenterAnchor().get_anchor()))

    vertex2 = tailwind.widgets.Entry(window, "Vertex 2 (x, y)", util.Style.empty(), {}, {})

    window.add_widget(vertex2, util.PlaceData(0.2, 0.3, util.CenterAnchor().get_anchor()))

    vertex3 = tailwind.widgets.Entry(window, "Vertex 3 (x, y)", util.Style.empty(), {}, {})

    window.add_widget(vertex3, util.PlaceData(0.2, 0.4, util.CenterAnchor().get_anchor()))

    vertex4 = tailwind.widgets.Entry(window, "Vertex 4 (x, y)", util.Style.empty(), {}, {})

    window.add_widget(vertex4, util.PlaceData(0.2, 0.5, util.CenterAnchor().get_anchor()))

    shape = tailwind.widgets.Label(window, "Quadrilateral", util.Style.empty(), {}, {})

    window.add_widget(shape, util.PlaceData(0.5, 0.1, util.CenterAnchor().get_anchor()))

    proof = tailwind.widgets.Label(window, "Proof", util.Style.empty(), {}, {})

    window.add_widget(proof, util.PlaceData(0.8, 0.1, util.CenterAnchor().get_anchor()))

    calculate = tailwind.widgets.Button(window, calculate, util.Style.empty(), {}, {}, text="Calculate")

    window.add_widget(calculate, util.PlaceData(0.5, 0.9, util.CenterAnchor().get_anchor()))

    window.main_loop()
