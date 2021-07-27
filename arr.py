import sys, pyperclip

def admissible(s):
  return s in ["c", "l", "r"]

def intersperse(iterable, delimiter):
  it = iter(iterable)
  yield next(it)
  for x in it:
    yield delimiter
    yield x

def plit(matrix):
  pre = sys.argv[1]
  entries = list(map(lambda x: x.split(","), matrix.split(";")))
  row = len(entries[0])
  beg = "\\begin{tabular}{" + row * pre + "}\n"
  end = "\n\\end{tabular}\n"
  body = "".join(intersperse(map(lambda x : "".join(list(intersperse(x, "\t&\t"))), entries), " \\\\ \n"))
  tex_matrix = beg + body + end
  return tex_matrix

def send(message):
  pyperclip.copy(message)
  spam = pyperclip.paste()

if admissible(sys.argv[1]):
  mtrx = plit(sys.argv[2])
  send(mtrx)
else:
  print("Do you think this is a joke, bub?")