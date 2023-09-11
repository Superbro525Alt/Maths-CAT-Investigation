import math
import sys
import os

import numpy as np
import pygame

import tailwind.window
import tailwind.util as util
import tailwind.widgets


if __name__ == '__main__':

    def angle_between_lines(line1_start, line1_end, line2_start, line2_end):
        return np.degrees(np.arccos(np.dot((line1_end - line1_start), (line2_end - line2_start)) / (
                    np.linalg.norm(line1_end - line1_start) * np.linalg.norm(line2_end - line2_start))))


    def onTick(_window: tailwind.window.Window, *args, **kwargs):
        pass

    def calculate():
        proofs = []

        shapePoints = [
            vertex1.get_value().strip().split(","),
            vertex2.get_value().strip().split(","),
            vertex3.get_value().strip().split(","),
            vertex4.get_value().strip().split(",")
        ]

        lineLeft = [shapePoints[0], shapePoints[1]]
        lineTop = [shapePoints[1], shapePoints[3]]
        lineRight = [shapePoints[3], shapePoints[2]]
        lineBottom = [shapePoints[1], shapePoints[2]]

        topLeftAngle = angle_between_lines(np.array([int(shapePoints[0][0]), int(shapePoints[0][1])]), np.array([int(shapePoints[1][0]), int(shapePoints[1][1])]), np.array([int(shapePoints[2][0]), int(shapePoints[2][1])]), np.array([int(shapePoints[3][0]), int(shapePoints[3][1])]))
        topRightAngle = angle_between_lines(np.array([int(shapePoints[1][0]), int(shapePoints[1][1])]), np.array([int(shapePoints[2][0]), int(shapePoints[2][1])]), np.array([int(shapePoints[1][0]), int(shapePoints[1][1])]), np.array([int(shapePoints[3][0]), int(shapePoints[3][1])]))
        bottomRightAngle = angle_between_lines(np.array([int(shapePoints[2][0]), int(shapePoints[2][1])]), np.array([int(shapePoints[3][0]), int(shapePoints[3][1])]), np.array([int(shapePoints[0][0]), int(shapePoints[0][1])]), np.array([int(shapePoints[1][0]), int(shapePoints[1][1])]))
        bottomLeftAngle = angle_between_lines(np.array([int(shapePoints[3][0]), int(shapePoints[3][1])]), np.array([int(shapePoints[0][0]), int(shapePoints[0][1])]), np.array([int(shapePoints[3][0]), int(shapePoints[3][1])]), np.array([int(shapePoints[1][0]), int(shapePoints[1][1])]))

        lineTopLength = abs(int(shapePoints[0][0]) - int(shapePoints[1][0]))
        lineBottomLength = abs(int(shapePoints[2][0]) - int(shapePoints[3][0]))
        lineLeftLength = abs(int(shapePoints[0][1]) - int(shapePoints[3][1]))
        lineRightLength = abs(int(shapePoints[1][1]) - int(shapePoints[2][1]))

        print(lineTopLength, lineBottomLength, lineLeftLength, lineRightLength)
        if topLeftAngle == 90 and topRightAngle == 90 and bottomRightAngle == 90 and bottomLeftAngle == 90:
            if lineTopLength == lineBottomLength == lineLeftLength == lineRightLength:
                shapeData.set_text("Square")
                proofs.append("All angles are 90 degrees")
                proofs.append("All sides are the same length")

            else:
                shapeData.set_text("Rectangle")
                proofs.append("All angles are 90 degrees")
                proofs.append("Not all sides are the same length")


        # do the same without util.angle



        # identify shape out of Trapezium Kite Parallelogram Rectangle Rhombus Square from points including proofs

        # check for parallel sides
        if lineLeft[0][0] == lineLeft[1][0] and lineRight[0][0] == lineRight[1][0]:
            proofs.append("Left and right sides are parallel")
            if lineTop[0][0] == lineTop[1][0] and lineBottom[0][0] == lineBottom[1][0]:
                proofs.append("Top and bottom sides are parallel")
                shapeData.set_text("Square")

        elif lineTop[0][0] == lineTop[1][0] and lineBottom[0][0] == lineBottom[1][0]:
            proofs.append("Top and bottom sides are parallel")



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

    shapeTitle = tailwind.widgets.Label(window, "Quadrilateral", util.Style.empty(), {}, {})

    window.add_widget(shapeTitle, util.PlaceData(0.5, 0.1, util.CenterAnchor().get_anchor()))

    shapeData = tailwind.widgets.Label(window, "None", util.Style.empty(), {}, {})

    window.add_widget(shapeData, util.PlaceData(0.5, 0.2, util.CenterAnchor().get_anchor()))

    proofTitle = tailwind.widgets.Label(window, "Proof", util.Style.empty(), {}, {})

    window.add_widget(proofTitle, util.PlaceData(0.8, 0.1, util.CenterAnchor().get_anchor()))

    proofData = tailwind.widgets.Label(window, "None", util.Style.empty(), {}, {})

    window.add_widget(proofData, util.PlaceData(0.8, 0.2, util.CenterAnchor().get_anchor()))

    calculate = tailwind.widgets.Button(window, calculate, util.Style.empty(), {}, {}, text="Calculate")

    window.add_widget(calculate, util.PlaceData(0.5, 0.9, util.CenterAnchor().get_anchor()))



    window.main_loop()
