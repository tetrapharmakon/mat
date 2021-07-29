import sys, pyperclip

# ØpbBvV is a matrix environment
def is_matrix(c):
  return c in ["s", "p", "b", "B", "v", "V", ""]

def intersperse(iterable, delimiter):
  it = iter(iterable)
  yield next(it)
  for x in it:
    yield delimiter
    yield x

def gen_matrix(m):
  return "".join(intersperse(map(lambda x : "".join(list(intersperse(x, "\t&\t"))), m), " \\\\ \n"))

def splitter(m):
  return list(map(lambda x: x.split(","), m.split(";")))

def matter(matrix):
  pre = sys.argv[1]
  entries = splitter(matrix)
  body = gen_matrix(entries)
  if is_matrix(pre):
     # catches argv[1] containing the specific matrix env
    beg = "\\left(\\begin{smallmatrix}\n" if pre == "s" else "\\begin{" + pre + "matrix}\n"
    end = "\n\\end{smallmatrix}\\right)\n" if pre == "s" else "\n\\end{" + pre + "matrix}\n"
    # `smallmatrix` needs brackets around the env
    tex_matrix = beg + body + end
    return tex_matrix
  elif pre[0] == "t": # is_tabular(pre)
    row = len(entries[0])
    beg = "\\begin{tabular}{" + row * pre[1] + "}\n"
    end = "\n\\end{tabular}\n"
    tex_matrix = beg + body + end
    return tex_matrix
  elif pre[0] == "x": # is_xy(pre)
    beg = "\\xymatrix{\n"
    end = "\n}"
  else:
    beg = "Do "
    body = "you "
    end = "think this is a joke, bub?"
  tex_matrix = beg + body + end
  return tex_matrix

def send(message):
  pyperclip.copy(message)
  spam = pyperclip.paste()

mtrx = matter(sys.argv[2])
send(mtrx)