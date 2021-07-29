import sys, pyperclip

# ØpbBvV
def is_matrix(c):
  return c in ["s", "p", "b", "B", "v", "V", ""]

# def switcher(c):
#   cases = {
#     "":  "",
#     "s": "small",
#     "p": "p",
#     "b": "b",
#     "B": "B",
#     "v": "v",
#     "V": "V",
#     "t": "tabular",
#     "x": "xymatrix"
#   }
#   return cases.get(c, "Do you think this is a joke, bub?")

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
  if is_matrix(pre):
     # catches argv[1] containing the specific matrix env
    beg = "\\left(\\begin{smallmatrix}\n" if pre == "s" else "\\begin{" + pre + "matrix}\n"
    end = "\n\\end{smallmatrix}\\right)\n" if pre == "s" else "\n\\end{" + pre + "matrix}\n"
    # `smallmatrix` needs brackets around the env
    entries = splitter(matrix)
    body = gen_matrix(entries)
    tex_matrix = beg + body + end
    return tex_matrix
  elif pre[0] == "t": # is_tabular(pre)
    entries = splitter(matrix)
    row = len(entries[0])
    beg = "\\begin{tabular}{" + row * pre[1] + "}\n"
    end = "\n\\end{tabular}\n"
    body = gen_matrix(entries)
    tex_matrix = beg + body + end
    return tex_matrix
  elif pre[0] == "x": # is_xy(pre)
    beg = "\\xymatrix{\n"
    end = "\n}"
    entries = splitter(matrix)
    body = gen_matrix(entries)
    tex_matrix = beg + body + end
    return tex_matrix
  else:
    return "Do you think this is a joke, bub?"

def send(message):
  pyperclip.copy(message)
  spam = pyperclip.paste()

mtrx = matter(sys.argv[2])
send(mtrx)