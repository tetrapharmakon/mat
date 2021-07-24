# mat

`mat` is a minimal python script to paste a LaTeX matrix on your clipboard.

in:

```"1,2,3;4,5,6;7,8,9"```

out:

```
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{matrix}
```

## Options

### matrix
```mat "" "1,2,3;4,5,6;7,8,9"``` yields
```
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{matrix}
```
### pmatrix
```mat "p" "1,2,3;4,5,6;7,8,9"``` yields
```
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{pmatrix}
```
### bmatrix
```mat "b" "1,2,3;4,5,6;7,8,9"``` yields
```
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{bmatrix}
```
### Bmatrix
```mat "B" "1,2,3;4,5,6;7,8,9"``` yields
```
\begin{Bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{Bmatrix}
```
### vmatrix
```mat "v" "1,2,3;4,5,6;7,8,9"``` yields
```
\begin{vmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{vmatrix}
```
### Vmatrix
```mat "V" "1,2,3;4,5,6;7,8,9"``` yields
```
\begin{Vmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{Vmatrix}
```
### smallmatrix
```mat "small" "1,2,3;4,5,6;7,8,9"``` yields
```
\begin{smallmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9 \\
\end{smallmatrix}
```