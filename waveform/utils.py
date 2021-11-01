# import matplotlib.pyplot as mplt
# from bokeh.colors import name
# from bokeh.models import Legend, LabelSet
# from bokeh.plotting import figure, output_file, show
from matplotlib import pyplot as mplt
from bokeh import plotting as bplt


def create_figure(backend="matplotlib", **kwargs):
    print(kwargs.items())
    if (backend == "matplotlib"):
        # figure = mplt.figure()
        px = 1/96
        figure, axes = mplt.subplots(figsize=(kwargs["plot_width"]*px, kwargs["plot_height"]*px))
        # figure.tight_layout(pad=5)
        axes.grid(True)
        axes.set_axisbelow(True)
        axes.set_title(kwargs["title"])
        axes.set_xlabel(kwargs["x_axis_label"], fontsize=kwargs["x_axis_label_size"])
        axes.set_ylabel(kwargs["y_axis_label"], fontsize=kwargs["y_axis_label_size"])
        if (kwargs["x_axis_log"]):
            axes.set_xscale("log")
        if (kwargs["y_axis_log"]):
            axes.set_yscale("log")
        if kwargs["x_range"] is not None:
            axes.set_xlim(tuple(kwargs["x_range"]))
        if kwargs["y_range"] is not None:
            axes.set_ylim(tuple(kwargs["y_range"]))
        if (kwargs["use_scientific"] and not (kwargs["x_axis_log"] or kwargs["y_axis_log"])):
            axes.ticklabel_format(axis="both", style="sci")

    elif (backend == "bokeh"):
        figure = bplt.figure()
        axes = None
        # p.left[0].formatter.use_scientific = False
        # p.below[0].formatter.use_scientific = False
    pass

    return figure, axes


def add_plot(axes, type, x, y, **kwargs):
    if (type == "line"):
        axes.plot(x, y,
                  color=kwargs["color"],
                  linewidth=kwargs["line_width"],
                  linestyle=kwargs["line_style"],
                  label=kwargs["legend_label"])
        # print(f"{kwargs['legend_label']=}")
        # axes.set_label(kwargs["legend_label"])
        if (kwargs["legend_label"] is not None):
            axes.legend()
    elif (type == "circle"):
        axes.scatter(x, y,
                     color=kwargs["color"],
                     label=kwargs["legend_label"])
