class Robot:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = [0, 0]
        self.direction = "East"

    def step(self, num):   

        total = ((self.width + self.height - 2) * 2)

        num= num % total

        if num != 0 :

            c = 0

            while c < num :

                if self.direction == "East" :

                    if self.position[0] == self.width - 1:
                        self.direction = "North"
                        num += 1
                    
                    else:
                        self.position[0] += 1
                
                elif self.direction == "North" :

                    if self.position[1]  == self.height - 1:
                        num += 1
                        self.direction = "West"

                    else:
                        
                        self.position[1] +=1
                    

                elif self.direction == "West" :

                    if self.position[0]  == 0 :
                        num += 1
                        self.direction = "South"
                        
                    else:
                    
                        self.position[0] -=1
                        
                elif self.direction == "South":

                    if self.position[1]  == 0:
                        num +=1
                        self.direction = "East"

                    else:
                        self.position[1] -= 1
                        
                c += 1

        elif self.position==[0,0]  and self.direction=="East":self.direction="South"

    def getPos(self):
        return self.position

    def getDir(self):
        return self.direction
