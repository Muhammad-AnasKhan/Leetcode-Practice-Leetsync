class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current_altitude = 0
        # Highest altitude currently is 0.
        highest_altitude = current_altitude
        for i in gain:
            # Adding the gain in altitude to the current altitude.
            current_altitude += i
            # Update the highest altitude.
            if highest_altitude < current_altitude:
                highest_altitude = current_altitude
        
        return highest_altitude