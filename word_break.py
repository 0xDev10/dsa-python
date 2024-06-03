def wordBreak(s, wordDict):
    word_set = set(wordDict)
    queue = [0]
    visited = set()
    
    while queue:
        start = queue.pop(0)
        print(start)
        if start in visited:
            continue
        for end in range(start+1, len(s)+1):
            if s[start:end] in word_set:
                queue.append(end)
                if end == len(s):
                    return True
        visited.add(start)
        print(visited)
        print('-'*10)
    
    return False

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print('len = ', len(s))
print(wordBreak(s, wordDict))