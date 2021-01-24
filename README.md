# TextToGcode

 A python file you can utilize to create custom gcode from a string.

## Usage

Download a copy of the TextToGcode python file from this repository and add it to your project, then import the class from the file:

`from TextToGcode import ttg`

Then you can call the ToGcode function with your arguments to output or return your gcode as a file or list:

`ttg(TEXT, SIZE, ROTATION, MODE, FEEDRATE).toGcode("ON COMMAND", "OFF COMMAND", "FAST COMMAND", "SLOW COMMAND")`

**Text**: a string for the text you want to be transformed to gcode, accepted characters are a-z, 0-9

**Size**: integer that represents the scale of the text in mm

**Rotation**: integer in degrees of the rotation of the text

**Mode**: a string specifying the mode of return.

- Return: returns a string of gcode commands
- File: generates an `output.gcode` file in the same directory
- visualize: returns a raw list of tuples (this method is likely to be removed)

**Feedrate**: integer used to specify the feed rate for the gcode operations
