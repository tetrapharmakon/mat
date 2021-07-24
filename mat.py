import sys, pyperclip

# ØpbBvV
def admissible(s):
  return s in "pbBvV"

def intersperse(iterable, delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x

def plit(matrix):
  pre = sys.argv[1]
  beg = "\\begin{" + pre + "matrix}\n"
  end = "\n\\end{" + pre + "matrix}\n"
  splat = list(map(lambda x: x.split(","), matrix.split(";")))
  body = "".join(intersperse(map(lambda x : "".join(list(intersperse(x, "\t&\t"))), splat), " \\\\ \n"))
  splet = beg + body + end
  return splet

def send(message):
  pyperclip.copy(message)
  spam = pyperclip.paste()

if admissible(sys.argv[1]):
  mtrx = plit(sys.argv[2])
  send(mtrx)
else:
  print("Do you think this is a joke, bub?")