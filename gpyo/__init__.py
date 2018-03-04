# -*- coding: utf-8 -*-

import argparse
from pywiring.i2c import PCF8574IO

def parse_args():
    parser = argparse.ArgumentParser(description="Simple command to read and write to an I²C PCF8574 board using PyWiring")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-r", "--read", type=int, help="Read pin")
    group.add_argument("-w", "--write", type=int, nargs=2, help="Write to pin")
    parser.add_argument("-b", "--bus", type=int, help="Bus number")
    parser.add_argument("-a", "--address", type=int, help="Device address")
    return parser.parse_args()

def main():
    args = parse_args()

    ioi = PCF8574IO(args.bus, args.address)

    if args.read is not None:
        ioi.pin_mode(args.read, True, localonly=True)
        print(ioi.digital_read(args.read))
    elif args.write is not None:
        ioi.pin_mode(args.write[0], False, localonly=True)
        ioi.digital_write(*args.write)


if __name__ == "__main__":
    main()