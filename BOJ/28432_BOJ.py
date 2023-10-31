n = int(input())
word1_result = [input() for i in range(n)]
first_word1 = ""
last_word1 = ""
flag = ""

if word1_result.index("?") == 0:
    if n != 1:
        first_word1 = word1_result[word1_result.index("?")+1][0]
        flag = "end"
    else:
        flag = "no"
elif word1_result.index("?") == n-1:
    last_word1 = word1_result[word1_result.index("?")-1][-1]
    flag = "fir"

else:
    first_word1 = word1_result[word1_result.index("?")-1][-1]
    last_word1 = word1_result[word1_result.index("?")+1][0]
    flag = "mid"

n2 = int(input())
word2_result = [input() for j in range(n2)]

for k in word2_result:
    if flag == "end":
        if k[-1] == first_word1 and k not in word1_result:
            print(k)
            break
    elif flag == "fir":
        if k[0] == last_word1 and k not in word1_result:
            print(k)
            break
    elif flag == "no":
        print(k)
        break
    elif flag == "mid":
        if k[0] == first_word1 and k[-1] == last_word1 and k not in word1_result:
            print(k)
            break