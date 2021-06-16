import numpy as np
import math


def draw_yline(graph, z_buffer, size, y, z, x1, x2, color):
    h, w = size

    if not 0 < y < h:
        return

    while x1 <= x2:
        if 0 < x1 < w and z_buffer[h - y][x1] > z:
            z_buffer[h - y][x1] = z
            graph[h - y][x1] = (color.red, color.green, color.blue)

        x1 += 1


def fill_bottom_flat_triangle(graph, z_buffer, size, v1, v2, v3, color):
    slope1 = (v2[0][0] - v1[0][0]) / (v2[1][0] - v1[1][0])
    slope2 = (v3[0][0] - v1[0][0]) / (v3[1][0] - v1[1][0])

    if math.fabs(slope1) > 5 or math.fabs(slope2) > 5:
        return

    cur_x1 = v1[0][0]
    cur_x2 = v1[0][0]
    z = round(v1[2][0])

    scan_line = round(v1[1][0])
    stop = round(v2[1][0])
    while scan_line <= stop:
        draw_yline(graph, z_buffer, size, scan_line, z, round(cur_x1), round(cur_x2), color)
        cur_x1 += slope1
        cur_x2 += slope2
        scan_line += 1


def fill_top_flat_triangle(graph, z_buffer, size, v1, v2, v3, color):
    slope1 = (v3[0][0] - v1[0][0]) / (v3[1][0] - v1[1][0])
    slope2 = (v3[0][0] - v2[0][0]) / (v3[1][0] - v2[1][0])

    if math.fabs(slope1) > 5 or math.fabs(slope2) > 5:
        return

    cur_x1 = v3[0][0]
    cur_x2 = v3[0][0]
    z = round(v1[2][0])

    scan_line = round(v3[1][0])
    stop = round(v1[1][0])
    while scan_line > stop:
        draw_yline(graph, z_buffer, size, scan_line, z, round(cur_x1), round(cur_x2), color)
        cur_x1 -= slope1
        cur_x2 -= slope2
        scan_line -= 1


def draw_triangle(graph, z_buffer, size, triangle, color):
    # sort vertices by Y coordinate
    triangle.sort(key=lambda v: v[1][0])
    v1, v2, v3 = triangle

    if v2[1][0] == v3[1][0]:
        fill_bottom_flat_triangle(graph, z_buffer, size, v1, v2, v3, color)
    elif v1[1][0] == v2[1][0]:
        fill_top_flat_triangle(graph, z_buffer, size, v1, v2, v3, color)
    else:
        v4 = np.array([[v1[0][0] + (v2[1][0] - v1[1][0]) / (v3[1][0] - v1[1][0]) * (v3[0][0] - v1[0][0])],
                       v2[1],
                       v2[2],  # FIXME: it should be interpolated as in X axis
                       [1.]])

        fill_bottom_flat_triangle(graph, z_buffer, size, v1, v2, v4, color)
        fill_top_flat_triangle(graph, z_buffer, size, v2, v4, v3, color)
