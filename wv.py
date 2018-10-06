#!/usr/bin/python3

import re
from bokeh.plotting import figure, output_file, show

# Data configutation section ##################################################

wave_file = "/home/mvico/Documentos/DACI_2018/practico/TP_1/imagenes/gmID_vs_ID/gmID_vs_ID"
plot_title = "gmID_vs_ID"

#show_data_points = False
show_data_points = True

# Plot configutation section ##################################################

data_line_color = "red"
data_points_color = "blue"

###############################################################################

header_lines = 2
line_index = 0

x = []
y = []

with open(wave_file) as file:
    for line in file:
        if (line_index > header_lines - 1):
            match = re.findall(r"\s*(\d+\.\d+E[+|-]\d+)\s*", line)
            x.append(match[0])
            y.append(match[1])
        line_index += 1

x = [float(x) for x in x]
y = [float(y) for y in y]

output_file("{}.html".format(plot_title))
print("{}.html".format(plot_title))
p = figure(title = plot_title)

p.line(x, y, legend = plot_title, line_width = 2, color = data_line_color)

if (show_data_points):
    p.circle(x, y, color = data_points_color)

show(p)
