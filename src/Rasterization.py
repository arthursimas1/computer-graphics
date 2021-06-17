import numpy as np
import math
import colorsys
import webcolors


def draw_yline(graph, z_buffer, size, y, z, x1, x2, color):
    h, w = size

    if not 0 < y < h:
        return

    while x1 <= x2:
        if 0 < x1 < w and z_buffer[h - y][x1] > z:
            z_buffer[h - y][x1] = z
            graph[h - y][x1] = color

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


def draw_triangle(graph, z_buffer, size, camera_coord, obj, scene, vertexes, triangle_index):
    # sort vertices by Y coordinate
    triangle = obj.faces[triangle_index]
    v1 = vertexes[triangle[0]]
    v2 = vertexes[triangle[1]]
    v3 = vertexes[triangle[2]]
    triangle_vertexes = [v1, v2, v3]
    triangle_vertexes.sort(key=lambda v: v[1][0])

    color = face_color(obj, scene, camera_coord, v1, triangle_index)

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


def draw_triangle_vertices(graph, z_buffer, size, camera_coord, obj, scene, vertexes, triangle_index):
    # sort vertices by Y coordinate
    triangle = obj.faces[triangle_index]
    v1 = vertexes[triangle[0]]
    v2 = vertexes[triangle[1]]
    v3 = vertexes[triangle[2]]
    triangle_vertexes = [v1, v2, v3]

    h, w = size

    color = face_color(obj, scene, camera_coord, v1, triangle_index)

    for v in triangle_vertexes:
        x = v[0][0]
        y = h - v[1][0]
        z = v[2][0]
        if 0 < x < w and 0 < y < h and z_buffer[y][x] > z:
            z_buffer[y][x] = z

            graph[y][x] = color


def face_color(obj, scene, camera_coord, vertex, triangle_index):
    def angle_between_vectors(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    obj_rgb_color = webcolors.html5_parse_simple_color(obj.hex_color)
    hue, _, saturation = colorsys.rgb_to_hls(obj_rgb_color.red, obj_rgb_color.green, obj_rgb_color.blue)

    # ambient light
    lightness = scene.k_ambient

    normal = obj.normals_of_faces[triangle_index]
    camera_vector = camera_coord - vertex.flatten()[:-1]

    for ls in scene.light_sources:
        incidence_vector = vertex.flatten()[:-1] - ls.position
        incidence_vector /= np.linalg.norm(incidence_vector)
        reflection_vector = 2 * np.dot(np.dot(normal, incidence_vector), normal) - incidence_vector

        lightness += ls.intensity * (
                    obj.k_diffuse * angle_between_vectors(incidence_vector, normal) +  # diffuse reflection
                    obj.k_specular * angle_between_vectors(reflection_vector, camera_vector)**obj.shininess    # specular reflection
        )

    # truncate
    lightness *= 100
    lightness = min(lightness, 100)  # maximum = 100
    lightness = max(lightness, 0)    # minimum = 0

    return colorsys.hls_to_rgb(hue, lightness, saturation)

