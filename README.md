# Project Title

Applying Metadata Tags for TIFF & JPEG files

## Description

* Apply the Metadata tags "Document Name, Artist, Scanner Manufacture, Scanner  Model, Software, DateTime"
* Used exiftool.exe (download from https://exiftool.org/)
* Images type: TIF, JPG

## Getting Started

### Dependencies

* Windows 7

### Installing

### Executing program

* Run the program
* Ask user to enter the path of the input image file
* Tool will apply the TIFF tag in the same location Input file directory


### Help
* copy the "exiftool.exe" file in the tool path
* copy the "tag.ini" file in the tool path
* Metadata Tag values should capture in the "tag.ini" file in respective xml tags
* If no value for particular element then leave that tag as empty tag, i.e. <Scanner></Scanner>
* TIFF date & time value format should be "YYYY:MM:DD HH:MM:SS", if format is wrong tool notify the error message in "error.log" file.

## Version History

* 0.1
    * Initial Release
