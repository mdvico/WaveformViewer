# WaveformViewer
Waveform viewer for Synopsys CustomCompiler, text table format, simulation data

## Before usage
You will need:
- Python 3
- The `bokeh` ploting library (`pip3 install bokeh --user`)
- The `pandas` library (`pip3 install pandas --user`)
- The `pillow` library for PNG export (`pip3 install pillow --user`)
- The `selenium` library for PNG export (`pip3 install selenium --user`)

If you have problems related to `phantomjs` try the following:
- Install npm (`apt install npm`)
- Install phantomjs-prebuilt (npm install phantomjs-prebuilt)

## Usage
1. Edit the `wp.py` file configuration section to point to the data file, change the title, etc.
2. In a terminal, execute `python3 wv.py` or `./wv.py` (if you changed the file to be executable).

## TODO
- [ ] Add support for batch file processing.
- [ ] Add option to export table.
- [ ] Change x axis notation to scientific (milli, micro, nano, etc.).
- [ ] Add some sort of verbosity.
- [ ] Add some sort of debug capability.
- [ ] Add the option of sourcing a local configuration file to have a consistent format for different plots.
- [ ] Add argument to change the axis labels.
- [ ] Add option to control the DPI output for the PNG output file.
- [ ] Add argument to control the axis ticks, log, db20, etc.

## DONE
- [x] Use pandas dataframe to manipulate the data.
- [x] Include support for multiple waveforms.
- [x] Allow to mute the different plots pressing on its legends.
- [x] Avoid showing the pandas dataframe on the terminal.
- [x] Add argument to ask for an PNG output file.
- [x] Add argument to ask for an SVG output file.
- [x] Add argument to avoid showing the output, just to create the output file.
