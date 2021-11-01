import pandas as pd


def load(wave_input_file, header, sep):
    return pd.read_csv(wave_input_file, header=header, sep=sep,
            engine="python")


def save_figure(figure, filename, type="png"):
    figure.savefig(f"{filename}.{type}")

