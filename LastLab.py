def editDistance(str1, str2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)

    return min(editDistance(str1, str2, m, n - 1) + 1,
               editDistance(str1, str2, m - 1, n) + 1,
               editDistance(str1, str2, m - 1, n - 1) + 1
               )

X = "kitten"
Y = "sitting"
print("The edit distance between ", X, " and ", Y, " is", editDistance(X, Y, len(X), len(Y)))
