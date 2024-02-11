def FunnyString(s):
    q_re = s[::-1]
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(q_re[i]) - ord(q_re[i + 1])):
            return 'Not Funny'
    return 'Funny'