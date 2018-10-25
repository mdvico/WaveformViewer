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
- Install `npm` (`apt install npm`)
- Install `phantomjs-prebuilt` (`npm install phantomjs-prebuilt`)

## Usage
- In a terminal, execute `wp.py` providing, at least, the required arguments (to see them see the help executing `wv.py --help`) to point to the data file, change the title, etc.

### Examples
1. In a terminal, execute `python3 wv.py` or `./wv.py` (if you changed the file to be executable). It will show you the help section.
2. `wv -i <data_table>` creates an HTML file with the plot for the given `data_table` and opens it in your default internet browser. Since no name for the output file is provided the same as the input is used.
3. `wv -i <data_table> -o <image_from_data_table>` same as before but now it saves the HTML file by the name `image_from_data_table.html`.
4. `wv -i <data_table> -o <image_from_data_table> -dp` same as before but now it saves the HTML file by the name `image_from_data_table.html`. The data points (actual simulated/calculated values) are also shown.
5. `wv -i <data_table> -o <image_from_data_table> -dp -lw 2` same as before but changing the lines width.
6. `wv -i <data_table> -o <image_from_data_table> -dp -lw 2 --no_output --save_png` same as the previous one. The HTML file is not created, and also not shown. Finally a PNG file is created.

## TODO
- [ ] Add support for batch file processing.
- [ ] Add option to export table.
- [ ] Change x axis notation to scientific (milli, micro, nano, etc.).
- [ ] Add some sort of verbosity.
- [ ] Add some sort of debug capability.
- [ ] Add the option of sourcing a local configuration file to have a consistent format for different plots.
- [ ] Add option to control the DPI output for the PNG output file.
- [ ] Add argument to control the axis ticks to db20.

## DONE
- [x] Use pandas dataframe to manipulate the data.
- [x] Include support for multiple waveforms.
- [x] Allow to mute the different plots pressing on its legends.
- [x] Avoid showing the pandas dataframe on the terminal.
- [x] Add argument to ask for an PNG output file.
- [x] Add argument to ask for an SVG output file.
- [x] Add argument to avoid showing the output, just to create the output file.
- [x] Add argument to control the axis ticks to log.
- [x] Add argument to change the axis labels.
