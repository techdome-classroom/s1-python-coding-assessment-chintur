def decode_message( s: str, p: str) -> bool:

# write your code here
        memo = {}

        def match(i, j):
                if (i, j) in memo:
                        return memo[(i, j)]
        
                if i == len(p) and j == len(s):
                        return True
        
                if i == len(p):
                        return False
        
                if j == len(s):
                        return all(x == '*' for x in p[i:])
        
                if p[i] == '?':
                        result = match(i + 1, j + 1)
                elif p[i] == '*':
                        result = match(i + 1, j) or match(i, j + 1)
                else:
                        result = p[i] == s[j] and match(i + 1, j + 1)
        
                memo[(i, j)] = result
                return result
        return False or match(0,0)
