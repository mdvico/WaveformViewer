#!/usr/bin/python3

import argparse
import os
import re
from bokeh.plotting import figure, output_file, show

parser = argparse.ArgumentParser(description = "Creates an HTML file containing the plot of waves defined by the input file in text table format.")
parser.add_argument("-i", "--input_file", type = str, dest = "wave_input_file", required = True, help = "Specifies the input waveform file in text table format.")
parser.add_argument("-o", "--output_file", type = str, dest = "wave_output_file", help = "Specifies the output plot file.")
parser.add_argument("-t", "--title", type = str, dest = "title", help = "Specifies the output plot title.")
parser.add_argument("-dp", "--show_data_points", action = "store_true", help = "Show data point over the plot-line.")
args = parser.parse_args()

# Data configutation section ##################################################

wave_input_file = args.wave_input_file

if (args.wave_output_file.endswith(".html")):
    wave_output_file = args.wave_output_file
else:
    wave_output_file = args.wave_output_file + ".html"

if (args.title == None):
    _, plot_title = os.path.split(args.wave_input_file)
else:
    plot_title = args.title

#show_data_points = False
#show_data_points = True

# Plot configutation section ##################################################

data_line_color = "red"
data_points_color = "blue"

###############################################################################

header_lines = 2
line_index = 0

x = []
y = []

with open(wave_input_file) as file:
    for line in file:
        if (line_index > header_lines - 1):
            match = re.findall(r"\s*(\d+\.\d+E[+|-]\d+)\s*", line)
            x.append(match[0])
            y.append(match[1])
        line_index += 1

x = [float(x) for x in x]
y = [float(y) for y in y]

output_file("{}.html".format(wave_output_file))
p = figure(title = plot_title)

p.line(x, y, legend = plot_title, line_width = 2, color = data_line_color)

if (args.show_data_points):
    p.circle(x, y, color = data_points_color)

show(p)
