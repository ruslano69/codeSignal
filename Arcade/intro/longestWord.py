def longestWord(text):
    s = re.split('[^a-zA-Z]',text)
    return max(s,key=len)