import argparse
from escpos.printer import Usb, CupsPrinter, File

CONFIGURATIONS = {
    'reliance': {
        'cups_printer_name': 'Reliance-Printer',
        'vendor_id': 0x0425,
        'product_id': 0x8147,
        # Bulk endpoints - use lsusb -v -d 0425:8147
        # to find the correct endpoint addresses on
        # your system
        'in_ep': 0x87,
        'out_ep': 0x08,
    },
    'phoenix': {
        'cups_printer_name': 'Phoenix',
        'vendor_id': 0x0425,
        'product_id': 0x0412,
        # Bulk endpoints - use lsusb -v -d 0425:0412
        # to find the correct endpoint addresses on
        # your system
        'in_ep': 0x81,
        'out_ep': 0x02,
    },
}

# use ls /dev/usb/ to find the correct file name on your system
FILE_NAME = '/dev/usb/lp0'

def print_text(printer='phoenix', method='cups'):
    print(f'Printing with method={method}')
    settings: dict = CONFIGURATIONS[printer]
    try:
        if method == 'cups':
            # Initialize CUPS printer
            printer = CupsPrinter(settings['cups_printer_name'])
            printer.open()
        elif method == 'usb':
            # Initialize USB printer
            printer = Usb(idVendor=settings['vendor_id'],
                      idProduct=settings['product_id'],
                      interface=1,
                      in_ep=settings['in_ep'],
                      out_ep=settings['out_ep']
                    )
        elif method == 'file':
            # Initialize FILE Printer
            printer = File(FILE_NAME)
            # printer.open()
        else:
            raise ValueError("Invalid printing method. Use 'cups', 'usb', or 'file'")

        # Set font and other settings if needed
        printer.set_with_default(font='a')
        printer.text('Here is some text in font a!\n')

        printer.set(font='b')
        printer.text('Here is some text in font b!\n')

        printer.set(underline=True)
        printer.text('And finally, some underlined text\n')

        printer.text('\n')
        printer.text('\n')
        printer.text('\n')
        printer.text('\n')

        # Cut the paper
        printer.cut()
        
        # Close the connection
        # printer.close()
        print("Print job sent successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        printer.close()


def main():
    parser = argparse.ArgumentParser(description='Print text using CUPS or USB.')
    parser.add_argument('--printer', choices=['reliance', 'phoenix'], default='phoenix', help="Printer name: 'reliance' or 'phoenix' (default: 'phoenix')")
    parser.add_argument('--method', choices=['cups', 'usb', 'file'], default='cups', help="Printing method: 'cups', 'usb', or 'file (default: 'cups')")
    args = parser.parse_args()

    print_text(method=args.method, printer=args.printer)

if __name__ == "__main__":
    main()
