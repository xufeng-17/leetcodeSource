class Solution:
    def wordBreak(self, s, wordDict):
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]


# 记忆化回溯
class Solution:
    def wordBreak(self, s, wordDict) :
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if(not s):
                return True
            res=False
            for i in range(1,len(s)+1):
                if(s[:i] in wordDict):
                    res=back_track(s[i:]) or res
            return res
        return back_track(s)



def cost(n):
    fn = 0
    if n >= 11:
        fn = 1 + min(cost(n - 5), cost(n - 1), cost(n - 11))
    elif n >= 5:
        fn = 1 + min(cost(n - 5), cost(n - 1))
    elif n >= 1:
        fn = n * 1
    return fn

def longest(a, lis=[]):
    l = len(lis)
    if len(a) > 0:
        if a[0] > (max(lis) if lis else 0):
            lis.append(a[0])
        else:
            lis[-1] = a[0]
        if len(a) > 1:
            longest(a[1:], lis)


    return len(lis)



if __name__ == "__main__":
    s="acatsdog"
    wordDict = ["cat", "dog", "cats"]
    so = Solution()
    print(so.wordBreak(s, wordDict))

    # print(cost(15))

    # a = [1, 5, 3, 4, 6, 9, 7, 8]
    # lis = []
    # print(longest(a,lis))
