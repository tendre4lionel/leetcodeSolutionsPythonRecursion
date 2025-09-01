# 495 Teemo Attacking
🔹 Recursive with Explicit State (heavily commented)
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        Recursive solution with explicit state parameters.
        Each recursive call computes poison from current attack plus rest.
        """

        # Helper function to handle attack at index i
        def helper(i):
            # Base case: last attack
            if i == len(timeSeries) - 1:
                return duration  # last attack adds full duration

            # Overlap calculation:
            # If next attack comes before poison ends, only count non-overlapping part
            overlap = min(duration, timeSeries[i+1] - timeSeries[i])

            # Recursive call for next attack
            return overlap + helper(i + 1)

        # Edge case: empty attack list
        if not timeSeries:
            return 0

        # Start recursion from the first attack
        return helper(0)

"""
🔹 Iterative Solution (heavily commented)
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        Iterative solution with detailed comments.
        Goal: accumulate total poisoned time, accounting for overlapping attacks.
        """

        if not timeSeries:
            return 0  # No attacks → no poison

        total = 0  # Total poisoned seconds

        # Process all attacks except the last one
        for i in range(len(timeSeries) - 1):
            # Time until next attack
            time_to_next = timeSeries[i+1] - timeSeries[i]

            # If next attack happens after current poison ends:
            # min(duration, time_to_next) ensures we only count non-overlapping part
            total += min(duration, time_to_next)

            # Debug info (optional)
            # print(f"Attack at {timeSeries[i]} adds {min(duration, time_to_next)} seconds")

        # Last attack always contributes full duration
        total += duration

        return total


# Example usage
sol = Solution()
print(sol.findPoisonedDuration([1,4], 2))   # 4
print(sol.findPoisonedDuration([1,2], 2))   # 3

🔹 Pure Functional Recursion (heavily commented)
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        Pure functional recursion.
        Recursively reduce the list of attacks,
        each time computing poison contribution from the first attack.
        """

        # Base case: no attacks → no poison
        if not timeSeries:
            return 0

        # Base case: single attack → full duration
        if len(timeSeries) == 1:
            return duration

        # Calculate contribution of first attack
        # If next attack happens before poison ends, only count non-overlapping part
        first_overlap = min(duration, timeSeries[1] - timeSeries[0])

        # Recursively compute poison for the rest of the attacks
        return first_overlap + self.findPoisonedDuration(timeSeries[1:], duration)

🔎 Complexity Analysis

Time Complexity: O(n) for all approaches — each attack is processed exactly once.

Space Complexity:

Iterative: O(1) → only a counter is stored.

Recursive with explicit state: O(n) → recursion stack.

Pure functional recursion: O(n) → recursion stack + list slicing in each call.


"""