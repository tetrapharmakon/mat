#!/usr/bin/env python3

import argparse
import pyperclip
import subprocess

parser = argparse.ArgumentParser(
    description='mat is a minimal python script to paste a LaTeX matrix on your clipboard.')

parser.add_argument('type', metavar='M', type=str,
                    choices=["s", "p", "b", "B", "v",
                             "V", "x", "tl", "tc", "tr", "m"],
                    help='type of matrix to render')

parser.add_argument('data', metavar='D', type=str,
                    help='contents of the matrix to render')

parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='print the result to console')

args = parser.parse_args()


# ==============================================================================


def intersperse(iterable, delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x


def gen_matrix(m):
    return "".join(intersperse(map(lambda x: "".join(list(intersperse(x, "\t&\t"))), m), " \\\\ \n"))


def splitter(m):
    return list(map(lambda x: x.split(","), m.split(";")))


DELIMITERS = {
    "s": lambda: ["\\left(\\begin{smallmatrix}", "\\end{smallmatrix}\\right)"],
    "t": lambda c, n: ["\\begin{tabular}{"+c*n+"}", "\\end{tabular}"],
    "*": lambda m: ["\\begin{"+m+"matrix}", "\\end{"+m+"matrix}"],
    "x": lambda: ["\\xymatrix{", "}"],
}


def wrapper(pre, entries, body):
    beg = ""
    end = ""

    if pre in ["s", "x"]:
        beg, end = DELIMITERS[pre]()
    elif pre in ["p", "b", "B", "v", "V"]:
        beg, end = DELIMITERS["*"](pre)
    elif pre[0] == "t":
        beg, end = DELIMITERS[pre[0]](pre[1], len(entries[0]))
    return "\n".join([beg, body, end, ""])


# ==============================================================================


entries = splitter(args.data)
body = gen_matrix(entries)
formatted = wrapper(args.type, entries, body)

if args.verbose > 0:
    print(formatted)

pyperclip.copy(formatted)
print(pyperclip.paste())

# Use subprocess to pipe the formatted text into xclip
process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
process.communicate(input=formatted.encode('utf-8'))  # Encode to bytes for subprocess

