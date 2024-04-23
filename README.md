# Linux CUPS and USB Phoenix Sample

A simple script to demonstrate ESC/POS functionality on Linux of the Phoenix Thermal Printer.

## Requirements

- Ubuntu (may work on other distros, currently untested)
- Python 3 with the following libraries
    - python-escpos 
- Download and setup the Linux driver located on the PTI Website:
    - [Phoenix Printer Drivers](https://pyramidacceptors.com/phoenix-printer-drivers)

## Running the Sample

You have two options for printing: via USB or with [CUPS](https://wiki.archlinux.org/title/CUPS). Switch between the two by specifing the `--method` command line argument:
    
- `python3 main.py --method cups`
- `python3 main.py --method usb`

If everything has been set up correctly, your printer will print a ticket that looks like the following:
![Image](./docs/sample.jpg "Sample Ticket")


