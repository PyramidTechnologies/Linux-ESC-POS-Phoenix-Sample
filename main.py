import argparse
from escpos.printer import Usb, CupsPrinter

# Define Vendor ID, Product ID, and endpoint addresses
VENDOR_ID = 0x0425
PRODUCT_ID = 0x0412
IN_EP = 0x81  # Input endpoint address
OUT_EP = 0x02  # Output endpoint address

CUPS_PRINTER_NAME="Phoenix"

def print_text(method='cups'):
    print(f'Printing with method={method}')
    try:
        if method == 'cups':
            # Initialize CUPS printer
            printer = CupsPrinter(CUPS_PRINTER_NAME)
            printer.open()
        elif method == 'usb':
            # Initialize USB printer
            printer = Usb(idVendor=VENDOR_ID, 
                      idProduct=PRODUCT_ID, 
                      in_ep=IN_EP, 
                      out_ep=OUT_EP,
                    )
        else:
            raise ValueError("Invalid printing method. Use 'cups' or 'usb'.")

        # Set font and other settings if needed
        printer.set_with_default(font='a')
        printer.text('Here is some text in font a!\n')

        printer.set(font='b')
        printer.text('Here is some text in font b!\n')

        printer.set(underline=True)
        printer.text('And finally, some underlined text\n')

        printer.text('\n')

        # Cut the paper
        printer.cut()
        
        # Close the connection
        printer.close()
        print("Print job sent successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        printer.close()


def main():
    parser = argparse.ArgumentParser(description='Print text using CUPS or USB.')
    parser.add_argument('--method', choices=['cups', 'usb'], default='cups', help="Printing method: 'cups' or 'usb' (default: 'cups')")
    args = parser.parse_args()

    print_text(method=args.method)

if __name__ == "__main__":
    main()
