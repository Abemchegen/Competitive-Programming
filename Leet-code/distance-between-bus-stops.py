class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total=sum(distance)
        clock=sum(distance[min(start,destination):max(start,destination)])
        anti=total-clock
        
        return min(clock,anti) 

        