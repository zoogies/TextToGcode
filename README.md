# TextToGcode

[![PyPI version](https://badge.fury.io/py/TextToGcode.svg)](https://badge.fury.io/py/TextToGcode) 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

 A python library you can utilize to create custom gcode commands from a string.

## Usage

install with `pip install TextToGcode`

import into your project with `from ttgLib.TextToGcode import ttg`

Then you can call the ToGcode function with your arguments to output or return your gcode as a file or list:

`ttg(TEXT, SIZE, ROTATION, MODE, FEEDRATE).toGcode("ON COMMAND", "OFF COMMAND", "FAST COMMAND", "SLOW COMMAND")`

**Text**: a string for the text you want to be transformed to gcode, accepted characters are a-z, 0-9

**Size**: integer that represents the scale of the text in mm

**Rotation**: integer in degrees of the rotation of the text

**Mode**: a string specifying the mode of return.

- Return: returns a string of gcode commands
- File: generates an `output.gcode` file in the same directory
- visualize: returns a raw list of tuples (if you want to plot them using matplotlib to visualize your path)

**Feedrate**: integer used to specify the feed rate for the gcode operations

**On Off Fast Slow Commands**: string commands for certain gcode operations. ex:

- ON: "M03 S500"
- OFF: "M05 S0"
- FAST: "G0"
- SLOW: "G1"
