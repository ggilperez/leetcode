class Solution:
    """
    >>> obj = Solution()
    >>> obj.isMatch("aa", "a")
    False
    >>> obj.isMatch("aa", "a*")
    True
    >>> obj.isMatch("ab", ".*")
    True
    >>> obj.isMatch("aaa", "a*a")
    True
    """
        
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
