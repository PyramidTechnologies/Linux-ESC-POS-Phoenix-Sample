# Linux CUPS and USB Phoenix Sample

A simple script to demonstrate ESC/POS functionality on Linux of the Phoenix Thermal Printer.

## Requirements

- Ubuntu (may work on other distros, currently untested)
- Python 3 with the following libraries
    - [python-escpos](https://github.com/python-escpos/python-escpos)
- Download and setup the Linux driver located on the PTI Website:
    - [Phoenix Printer Drivers](https://pyramidacceptors.com/phoenix-printer-drivers)

## Running the Sample

You have two options for printing: via USB or with [CUPS](https://wiki.archlinux.org/title/CUPS). Switch between the two by specifing the `--method` command line argument:
    
- `python3 main.py --method cups`
- `python3 main.py --method usb`

If everything has been set up correctly, your printer will print a ticket that looks like the following:
![Image](./docs/sample.jpg "Sample Ticket")

## Useful Commands

1. **`lsusb`**: Lists all USB devices connected to the system, showing basic details like bus number and device IDs.
2. **`ls /dev/usb`**: Displays the contents of the `/dev/usb` directory, where device files for USB devices are stored.
3. **`lsusb -v -d 0425:0412`**: Provides detailed information on a specific USB device, identified by the vendor and product ID `0425:0412`, including configurations and endpoint descriptors.
4. **tail -f /var/log/syslog**: Follow the system log as new entries are added.


