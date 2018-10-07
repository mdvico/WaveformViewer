# WaveformViewer
Waveform viewer for Synopsys CustomCompiler, text table format, simulation data

## Before usage

You will need:
- Python 3
- The `bokeh` ploting library (`pip install bokeh --user`)
- The `pandas` library (`pip install pandas --user`)

## Usage
1. Edit the `wp.py` file configuration section to point to the data file, change the title, etc.
2. In a terminal, execute `python3 wv.py` or `./wv.py` (if you changed the file to be executable).

## TODO
- Use pandas dataframe to manipulate the data.
- Include support for multiple waveforms.
- Add support for batch file processing.
- Add argument to avoid showing the output, just to create the output file.
