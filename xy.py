import sys, pyperclip

# ØpbBvV
# def admissible(s):
#   return s in ["small", "p", "b", "B", "v", "V", ""]

def intersperse(iterable, delimiter):
  it = iter(iterable)
  yield next(it)
  for x in it:
    yield delimiter
    yield x

def plit(matrix):
  beg = "\\xymatrix{\n"
  end = "\n}"
  entries = list(map(lambda x: x.split(","), matrix.split(";")))
  body = "".join(intersperse(map(lambda x : "".join(list(intersperse(x, "\t&\t"))), entries), " \\\\ \n"))
  tex_matrix = beg + body + end
  return tex_matrix

def send(message):
  pyperclip.copy(message)
  spam = pyperclip.paste()

mtrx = plit(sys.argv[1])
send(mtrx)