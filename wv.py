#!/usr/bin/python3

import argparse
import os
import re
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.colors import named
from bokeh.io import export_png
from bokeh.io import export_svgs

parser = argparse.ArgumentParser(description = "Creates an HTML file containing the plot of waves defined by the input file in text table format.")
parser.add_argument("-i", "--input_file", type = str, dest = "wave_input_file", required = True, help = "Specifies the input waveform file in text table format.")
parser.add_argument("-o", "--output_file", type = str, dest = "wave_output_file", help = "Specifies the output plot file.")
parser.add_argument("-t", "--title", type = str, dest = "title", help = "Specifies the output plot title.")
parser.add_argument("-dp", "--show_data_points", action = "store_true", default = False, help = "Show data point over the plot-line.")
parser.add_argument("-lw", "--line_width", type = int, dest = "line_width", choices = range(1,7), default = 1, help = "Specifies the data line width. Affects all the lines.")
parser.add_argument("--save_svg", action = "store_true", default = False, help = "Saves the plot in a svg file.")
parser.add_argument("--save_png", action = "store_true", default = False, help = "Saves the plot in a png file.")
parser.add_argument("--no_output", action = "store_true", default = False, help = "Does not create the HTML output file and does not open the browser to show it.")
args = parser.parse_args()

# Data configutation section ##################################################

wave_input_file = args.wave_input_file
wave_output_file = args.wave_output_file

if (args.title == None):
    _, plot_title = os.path.split(args.wave_input_file)
else:
    plot_title = args.title

line_width = args.line_width

# Plot configutation section ##################################################

#colors = [name for name in named.__all__]
colors = ["red", "blue", "green", "yellow", "purple", "black"]

###############################################################################

# Example of a text table
# #format table ## [Custom WaveView] saved 14:46:01 Sat Oct  6 2018
# XVAL gm/id_long_L_6_:_dc id_long_6
#  0.000E+00  1.986E+01 -0.000E+00

header_lines = 2
line_index = 0

match = []

with open(wave_input_file) as file:
    for line in file:
        if (line_index >= header_lines):
            match.append([float(num) for num in line.strip().split()])
        elif (line_index == 1):
            signals_list = line.split()
        line_index += 1

table = pd.DataFrame(columns = signals_list, data = match)

output_file(wave_output_file + ".html")
p = figure(title = plot_title)

for signal, data_color in zip(signals_list[1::], colors):
    p.line(table[signals_list[0]], table[signal], legend = signal, line_width = line_width, color = data_color, muted_color = data_color, muted_alpha = 0.1)
    if (args.show_data_points):
        p.circle(table[signals_list[0]], table[signal], color = data_color, alpha = 0.4, muted_color = data_color, muted_alpha = 0.2)

p.legend.click_policy = "mute"

if (args.save_png):
    p.toolbar_location = None
    export_png(p, filename = wave_output_file + ".png")
    p.toolbar_location = "right"
if (args.save_svg):
    p.output_backend = "svg"
    export_svgs(p, filename = wave_output_file + ".svg")
if (not args.no_output):
    show(p)
