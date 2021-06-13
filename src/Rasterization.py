import numpy as np
import math

def fill_bottom_flat_triangle(v1, v2, v3):
	slope1 = (v2[0] - v1[0]) / (v2[1] - v1[1])
	slope2 = (v3[0] - v1[0]) / (v3[1] - v1[1])

	cur_x1 = v1[0]
	cur_x2 = v1[0]

	scan_line = v1[1]
	while(scan_line <= v2[1]):
		draw_line(int(cur_x1), scan_line, int(cur_x2), scan_line)
		cur_x1 += slope1
		cur_x2 += slope2
		scan_line += 1

def fill_top_flat_triangle(v1, v2, v3):
	slope1 = (v3[0] - v1[0]) / (v3[1] - v1[1])
	slope2 = (v3[0] - v2[0]) / (v3[1] - v2[1])

	cur_x1 = v3[0]
	cur_x2 = v3[0]

	scan_line = v3[1]
	while(scan_line > v1[1]):
		draw_line(int(cur_x1), scan_line, int(cur_x2), scan_line)
		cur_x1 = slope1
		cur_x2 = slope2
		scan_line -= 1

def draw_triangle(v1, v2, v3):
	v1, v2, v3 = sort_by_y(v1, v2, v3)

	if(v2[1] == v3[1]):
		fill_bottom_flat_triangle(v1, v2, v3)
	elif(v1[1] == v2[1]):
		fill_top_flat_triangle(v1, v2, v3)
	else:
		v4 = []
		v4.append((int(v1[0] + (v2[1] - v1[1]) / (v3[1] - v1[1]) * (v3[0] - v1[0]))))
		v4.append(v2[1])
		fill_bottom_flat_triangle(v1, v2, v4)
		fill_top_flat_triangle(v2, v4, v3)

def sort_by_y(v1, v2, v3):
	pass
