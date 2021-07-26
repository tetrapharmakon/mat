import sys, pyperclip

# ØpbBvV
def admissible(s):
  return s in ["small", "p", "b", "B", "v", "V", ""]

def intersperse(iterable, delimiter):
  it = iter(iterable)
  yield next(it)
  for x in it:
    yield delimiter
    yield x

def plit(matrix):
  pre = sys.argv[1]
  # catches argv[1] containing the specific matrix env
  beg = "\\left(\\begin{smallmatrix}\n" if pre == "small" else "\\begin{" + pre + "matrix}\n"
  end = "\n\\end{smallmatrix}\\right)\n" if pre == "small" else "\n\\end{" + pre + "matrix}\n"
  # `smallmatrix` needs brackets around the env
  entries = list(map(lambda x: x.split(","), matrix.split(";")))
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