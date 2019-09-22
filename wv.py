#!/usr/bin/python3

import argparse
import os
import re
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend
from bokeh.colors import named
from bokeh.io import export_png
from bokeh.io import export_svgs

parser = argparse.ArgumentParser(description = "Creates an HTML file containing the plot of waves defined by the input file in text table format.")
parser.add_argument("-i", "--input_file", type = str, dest = "wave_input_file", required = True, help = "Specifies the input waveform file in text table format.")
parser.add_argument("-o", "--output_file", type = str, dest = "wave_output_file", help = "Specifies the output plot file.")
parser.add_argument("-hi", "--header_index", type = int, dest = "header_index", default = 1, help = "Specifies the line at which the data starts. Default = line 1.")
parser.add_argument("-t", "--title", type = str, dest = "title", help = "Specifies the output plot title.")
parser.add_argument("-xl", "--x_label", type = str, dest = "x_axis_label", help = "Specifies the label for the x axis.")
parser.add_argument("-yl", "--y_label", type = str, dest = "y_axis_label", help = "Specifies the label for the y axis.")
parser.add_argument("-dp", "--show_data_points", action = "store_true", default = False, help = "Show data point over the plot-line.")
parser.add_argument("-lw", "--line_width", type = int, dest = "line_width", choices = range(1,7), default = 1, help = "Specifies the data line width. Affects all the lines.")
parser.add_argument("--x_axis_log", action = "store_true", default = False, help = "Changes the x axis to log scale.")
parser.add_argument("--y_axis_log", action = "store_true", default = False, help = "Changes the y axis to log scale.")
parser.add_argument("-pm", "--presentation_mode", action = "store_true", default = False, help = "Shows the legend for the different curves inside the plotting area.")
parser.add_argument("--save_svg", action = "store_true", default = False, help = "Saves the plot in a svg file.")
parser.add_argument("--save_png", action = "store_true", default = False, help = "Saves the plot in a png file.")
parser.add_argument("--no_output", action = "store_true", default = False, help = "Does not create the HTML output file and does not open the browser to show it.")
args = parser.parse_args()


# Data configutation section ##################################################

wave_input_file = args.wave_input_file

if (args.wave_output_file == None):
    wave_output_file = wave_input_file
else:
    wave_output_file = args.wave_output_file


# Plot configuration section ##################################################

if (args.title == None):
    _, plot_title = os.path.split(args.wave_input_file)
else:
    plot_title = args.title

line_width = args.line_width

if (args.x_axis_log):
    x_axis_type = "log"
else:
    x_axis_type = "linear"

if (args.y_axis_log):
    y_axis_type = "log"
else:
    y_axis_type = "linear"

x_axis_label = args.x_axis_label
y_axis_label = args.y_axis_label

#colors = [name for name in named.__all__]
colors = ["red", "blue", "green", "yellow", "purple", "black"]


###############################################################################

# Example of a text table
# #format table ## [Custom WaveView] saved 14:46:01 Sat Oct  6 2018
# XVAL gm/id_long_L_6_:_dc id_long_6
#  0.000E+00  1.986E+01 -0.000E+00

table = pd.read_csv(wave_input_file, header = args.header_index, sep = "\s+")

output_file(wave_output_file + ".html")
p = figure(title = plot_title, x_axis_label = x_axis_label, y_axis_label = y_axis_label, x_axis_type = x_axis_type, y_axis_type = y_axis_type, toolbar_location = "above")

legends = []

for signal, data_color in zip(table.columns[1::], colors):
    if (args.show_data_points):
        p.circle(table[table.columns[0]], table[signal], color = data_color, alpha = 0.4, muted_color = data_color, muted_alpha = 0.2)

    if (args.presentation_mode):
        obj = p.line(table[table.columns[0]], table[signal], legend = signal, line_width = line_width, color = data_color, muted_color = data_color, muted_alpha = 0.1)
    else:
        obj = p.line(table[table.columns[0]], table[signal], line_width = line_width, color = data_color, muted_color = data_color, muted_alpha = 0.1)
        legends.append((signal, [obj]))

legend = Legend(items=legends, location=(10, 0))
legend.click_policy = "mute"
p.add_layout(legend, 'right')
p.legend.background_fill_alpha = 1

p.left[0].formatter.use_scientific = False
p.below[0].formatter.use_scientific = False

if (args.save_png):
    p.toolbar_location = None
    export_png(p, filename = wave_output_file + ".png")
    p.toolbar_location = "above"
if (args.save_svg):
    p.output_backend = "svg"
    export_svgs(p, filename = wave_output_file + ".svg")
if (not args.no_output):
    show(p)
