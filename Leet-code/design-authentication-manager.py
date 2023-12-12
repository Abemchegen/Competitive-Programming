class AuthenticationManager:


    def __init__(self, timeToLive: int):
        self.timeToLive=timeToLive
        self.d= {}
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.d[tokenId]=currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.d:
           if self.d[tokenId]+self.timeToLive>currentTime:
               self.d[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for item in self.d:
            if self.d[item]+self.timeToLive>currentTime:
                count+=1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)