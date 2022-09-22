#!/opt/homebrew/bin/python3

import argparse
from pathlib import Path

import numpy as np

import wave_io
import regressions
import utils

regression_types = ["linear", "cuadratic"]
plotting_backends = ["matplotlib", "bokeh"]

parser = argparse.ArgumentParser(description="Creates an HTML file containing \
        the plot of waves defined by the input file in text table format.")
parser.add_argument("-i", "--input_file", type=str, dest="wave_input_file",
                    required=True, help="Specifies the input waveform file \
                            in text table format.")
parser.add_argument("-o", "--output_file", type=str, dest="wave_output_file",
                    help="Specifies the output plot file.")
parser.add_argument("-hi", "--header_index", type=int, dest="header_index",
                    default=1, help="Specifies the line at which the data \
                            starts. Default=1.")
parser.add_argument("-t", "--title", type=str, dest="title", default="",
                    help="Specifies the output plot title.")
parser.add_argument("-xl", "--x_label", type=str, dest="x_axis_label",
                    help="Specifies the label for the x axis.")
parser.add_argument("-yl", "--y_label", type=str, dest="y_axis_label",
                    help="Specifies the label for the y axis.")
parser.add_argument("-dp", "--show_data_points", action="store_true",
                    default=False, help="Show data point over the plot-line.")
parser.add_argument("-nl", "--no_line", action="store_true", default=False,
                    help="Do not show connecting line between the different \
                            data points.")
parser.add_argument("-lw", "--line_width", type=int, dest="line_width",
                    choices=range(1, 7), default=1, help="Specifies the data \
                            line width. Affects all the lines.")
parser.add_argument("--x_axis_log", action="store_true", default=False,
                    help="Changes the x axis to log scale.")
parser.add_argument("--y_axis_log", action="store_true", default=False,
                    help="Changes the y axis to log scale.")
parser.add_argument("-pm", "--presentation_mode", action="store_true",
                    default=False, help="Shows the legend for the different \
                            curves inside the plotting area.")
parser.add_argument("-xr", "--x_range", type=float, dest="x_range", nargs=2,
                    help="Values between which the range for the x axis \
                            is plotted.")
parser.add_argument("-yr", "--y_range", type=float, dest="y_range", nargs=2,
                    help="Values between which the range for the y axis \
                            is plotted.")
parser.add_argument("--use_scientific", action="store_true",
                    default=False, help="Defines wether or not to use \
                            scientific notation for the axis' scale.")
parser.add_argument("--width", type=int, dest="plot_width", default=600,
                    help="Select the width of the plot. Default=600.")
parser.add_argument("--height", type=int, dest="plot_height", default=600,
                    help="Select the height of the plot. Default=600.")
parser.add_argument("-ls", "--label_text_size", type=int,
                    dest="label_text_size", default=12,
                    help="Set the size for both axis' labels.")
parser.add_argument("-sep", type=str, default=r"\s+", help="Specifies the \
        character used to split the data in columns.")
parser.add_argument("--save_svg", action="store_true", default=False,
                    help="Saves the plot in a svg file.")
parser.add_argument("--save_png", action="store_true", default=False,
                    help="Saves the plot in a png file.")
parser.add_argument("--no_output", action="store_true", default=False,
                    help="Does not create the HTML output file and does not \
                    open the browser to show it.")
parser.add_argument("--regression", type=str, choices=regression_types,
                    default=None, help="Add the specified regression type to \
                            the plot.")
parser.add_argument("-ia", "--input_above", type=str, dest="wave_input_above",
                    default=None, \
                    required=False, help="Specifies the input waveform file \
                            for the above confidence band in text table \
                            format.")
parser.add_argument("-ib", "--input_below", type=str, dest="wave_input_below",
                    default=None, \
                    required=False, help="Specifies the input waveform file \
                            for the below confidence band in text table \
                            format.")
parser.add_argument("-s", "--signal", type=str, dest="signal",
                    default=None, required=False, help="Specifies the \
                            input waveform name for the main plot in text \
                            table format.")
parser.add_argument("-sa", "--signal_above", type=str, dest="signal_above",
                    default=None, \
                    required=False, help="Specifies the input waveform name \
                            for the above confidence band in text table \
                            format.")
parser.add_argument("-sb", "--signal_below", type=str, dest="signal_below",
                    default=None, \
                    required=False, help="Specifies the input waveform name \
                            for the below confidence band in text table \
                            format.")
parser.add_argument("-b", "--backend", type=str, choices=plotting_backends,
                    dest="backend", default=plotting_backends[0],
                    help="Selects the backend library to create the plot.")
args = parser.parse_args()

# Data configuration section ##################################################

wave_input_file = Path(args.wave_input_file)

if (args.wave_input_above is not None) and (Path(args.wave_input_above).is_file()):
    wave_input_above = Path(args.wave_input_above)
    table_above = wave_io.load(wave_input_above, header=args.header_index, sep=args.sep)
    x_above = table_above[table_above.columns[0]]


if (args.wave_input_below is not None) and (Path(args.wave_input_below).is_file()):
    wave_input_below = Path(args.wave_input_below)
    table_below = wave_io.load(wave_input_below, header=args.header_index, sep=args.sep)
    x_below = table_below[table_below.columns[0]]

if args.wave_output_file is None:
    wave_output_file = wave_input_file
else:
    wave_output_file = Path(args.wave_output_file)

# Plot configuration section ##################################################

colors = ["red", "blue", "green", "yellow", "purple", "black"]

###############################################################################

# Example of a text table
# #format table ## [Custom WaveView] saved 14:46:01 Sat Oct  6 2018
# XVAL gm/id_long_L_6_:_dc id_long_6
#  0.000E+00  1.986E+01 -0.000E+00

table = wave_io.load(wave_input_file, header=args.header_index, sep=args.sep)
print(wave_output_file)
print(table)
print()
print()
print()
print()
print()

# output_file(str(wave_output_file.parent / (wave_output_file.stem + ".html")))
p, ax = utils.create_figure(title=args.title,
                            x_axis_label=args.x_axis_label,
                            y_axis_label=args.y_axis_label,
                            x_axis_log=args.x_axis_log,
                            y_axis_log=args.y_axis_log,
                            x_axis_label_size=args.label_text_size,
                            y_axis_label_size=args.label_text_size,
                            plot_width=args.plot_width,
                            plot_height=args.plot_height,
                            x_range=args.x_range,
                            y_range=args.y_range,
                            use_scientific=args.use_scientific,
                            toolbar_location="above")

# labels = LabelSet(text_font_size=f"{args.label_text_size}px")
# p.add_layout(labels)
# p.xaxis.axis_label_text_font_size = f"{args.label_text_size}px"
# p.yaxis.axis_label_text_font_size = f"{args.label_text_size}px"

legends = []

x = table[table.columns[0]]
print(x)

signals = []
if args.signal is not None:
    if args.signal in table.columns.to_list():
        signals.append("".join(args.signal))
else:
    signals = table.columns[1::]

for signal, data_color in zip(signals, colors):
    y = table[signal]
    if args.show_data_points:
        utils.add_plot(ax, "circle", x, y,
                       legend_label=signal,
                       color=data_color,
                       alpha=1,
                       muted_color=data_color,
                       muted_alpha=0.2)
    if args.no_line:
        pass
    else:
        if args.presentation_mode:
            obj = utils.add_plot(ax, "line", x, y,
                                 legend_label=signal,
                                 line_width=args.line_width,
                                 line_style="-",
                                 color=data_color,
                                 alpha=1,
                                 muted_color=data_color,
                                 muted_alpha=0.1)
        else:
            obj = utils.add_plot(ax, "line", x, y,
                                 legend_label=None,
                                 line_width=args.line_width,
                                 line_style="-",
                                 color=data_color,
                                 alpha=1,
                                 muted_color=data_color,
                                 muted_alpha=0.1)
            # obj = p.line(x, y,
            #              line_width=line_width,
            #              color=data_color,
            #              muted_color=data_color,
            #              muted_alpha=0.1)
            # legends.append((signal, [obj]))

    if args.regression is not None:
        model = regressions.cuadratic(x, y)
        polyline = np.linspace(min(x) - abs(min(x))*0.1 , max(x) + abs(max(x))*0.1, 10*len(x))
        print(f"{x=}")
        print(f"{min(x)=}")
        print(f"{max(x)=}")
        print(f"{len(x)=}")
        print(polyline)
        utils.add_plot(ax, "line", polyline, model(polyline),
                       legend_label=signal,
                       color=data_color,
                       line_width=0.5*args.line_width,
                       muted_color=data_color,
                       line_style="--",
                       alpha=0.5,
                       muted_alpha=0.1)

    if args.wave_input_above is not None: 
        utils.add_plot(ax, "band_above", x, y, above=table_above[args.signal_above], \
                line_width=args.line_width,
                line_style="-",
                legend_label=signal,
                color=data_color,
                alpha=0.5,
                )

    if args.wave_input_below is not None: 
        utils.add_plot(ax, "band_below", x, y, below=table_below[args.signal_below], \
                line_width=args.line_width,
                line_style="-",
                legend_label=signal,
                color=data_color,
                alpha=0.5,
                )

# Integrate
# legend = Legend(items=legends, location=(10, 0))
# legend.click_policy = "mute"
# p.add_layout(legend, "right")
# p.legend.background_fill_alpha = 1

if args.save_png:
    # p.toolbar_location = None
    # export_png(p, filename=str(wave_output_file.parent / (wave_output_file.stem + ".png")))
    wave_io.save_figure(p, filename=str(wave_output_file.parent / (wave_output_file.stem)))
    # p.toolbar_location = "above"
if args.save_svg:
    # p.output_backend = "svg"
    # export_svgs(p, filename=str(wave_output_file.parent / (wave_output_file.stem + ".svg")))
    wave_io.save_figure(p, filename=str(wave_output_file.parent / (wave_output_file.stem)), type="svg")

if not args.no_output:
    p.show()


# Flow structure
# 1. [X] - BE selection
# 2. [X] - Data loading
# 3. [ ] - Data handling
# 4. [~] - Figure creation
# 5. [~] - Figure style & configuration
# n. [X] - Plotting
# n+1. [X] - Legends
# n+2. [ ] - Showing the plot
# n+3. [X] - Saving plot
