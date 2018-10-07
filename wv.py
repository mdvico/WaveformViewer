#!/usr/bin/python3

import argparse
import os
import re
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.colors import named

parser = argparse.ArgumentParser(description = "Creates an HTML file containing the plot of waves defined by the input file in text table format.")
parser.add_argument("-i", "--input_file", type = str, dest = "wave_input_file", required = True, help = "Specifies the input waveform file in text table format.")
parser.add_argument("-o", "--output_file", type = str, dest = "wave_output_file", help = "Specifies the output plot file.")
parser.add_argument("-t", "--title", type = str, dest = "title", help = "Specifies the output plot title.")
parser.add_argument("-dp", "--show_data_points", action = "store_true", help = "Show data point over the plot-line.")
parser.add_argument("-lw", "--line_width", type = int, dest = "line_width", choices = range(1,7), default = 1, help = "Specifies the data line width. Affects all the lines.")
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

line_width = args.line_width
#show_data_points = False
#show_data_points = True

# Plot configutation section ##################################################

#data_line_color = "red"
#data_points_color = "blue"
#color_index = 0
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
            #signals_list = re.split(r"XVAL (.*?)\:", line)[1::]
            #signals_list.insert(0, "x_axis")
            signals_list = line.split()
            print(signals_list)
        line_index += 1

table = pd.DataFrame(columns = signals_list, data = match)
print(table)

output_file("{}.html".format(wave_output_file))
p = figure(title = plot_title)

for signal, data_color in zip(signals_list[1::], colors):
    p.line(table[signals_list[0]], table[signal], legend = signal, line_width = line_width, color = data_color)
    #color_index += 1
    if (args.show_data_points):
        p.circle(table[signals_list[0]], table[signal], color = data_color)

show(p)
