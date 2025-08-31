# 401 Binary Watch
class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []

        # Recursive helper function to turn on LEDs
        def dfs(pos, leds_left, hour, minute):
            """
            pos: current LED position (0-9)
            leds_left: number of LEDs left to turn on
            hour: current hour value
            minute: current minute value
            """
            # Base case: all LEDs turned on
            if leds_left == 0:
                if 0 <= hour <= 11 and 0 <= minute <= 59:
                    # Format minute with leading zero
                    result.append("{}:{:02d}".format(hour, minute))
                return

            # If all positions processed, stop
            if pos == 10:
                return

            # Determine if current LED is for hour or minute
            if pos < 4:
                # Hour LED, value = 2^pos
                new_hour = hour + (1 << pos)
                if new_hour <= 11:
                    dfs(pos + 1, leds_left - 1, new_hour, minute)
            else:
                # Minute LED, value = 2^(pos-4)
                new_minute = minute + (1 << (pos - 4))
                if new_minute <= 59:
                    dfs(pos + 1, leds_left - 1, hour, new_minute)

            # Also explore skipping this LED
            dfs(pos + 1, leds_left, hour, minute)

        # Start recursion from first LED
        dfs(0, turnedOn, 0, 0)

        return result


"""
class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []

        # Iterate over all possible hours (0-11)
        for hour in range(12):
            # Iterate over all possible minutes (0-59)
            for minute in range(60):
                # Count total number of '1's in binary representation
                if (bin(hour) + bin(minute)).count('1') == turnedOn:
                    # Format minute with leading zero using str.format()
                    result.append("{}:{:02d}".format(hour, minute))

        return result

"""