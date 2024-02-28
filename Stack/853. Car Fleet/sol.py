class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = [((target-position[i]), float(target-position[i])/float(speed[i])) for i in range(len(speed))]
        cars = sorted(cars, key = lambda x : x[0], reverse=True)

        fleets = []
        for car in cars:
            if not fleets or fleets[-1] < car[1]: # empty OR (not same fleet as last one)
                fleets.append(car[1]) # new fleet
        return len(fleets)