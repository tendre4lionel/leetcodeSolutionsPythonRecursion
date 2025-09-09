# 506 Relative Ranks
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Algorithm (Iterative):
        # 1. Pair each score with its index: [(score, index), ...].
        # 2. Sort descending by score.
        # 3. Iterate through sorted list, assign medals/ranks.
        # 4. Place the rank string back into result[] aligned with original index.
        #
        # Time Complexity: O(n log n)   (due to sorting)
        # Space Complexity: O(n)        (result + mapping structures)

        n = len(score)
        # Step 1: Pair score with index
        score_index_pairs = [(s, i) for i, s in enumerate(score)]

        # Step 2: Sort by score descending
        score_index_pairs.sort(key=lambda x: -x[0])

        # Step 3: Prepare result list
        result = [""] * n

        for rank, (s, idx) in enumerate(score_index_pairs, start=1):
            if rank == 1:
                result[idx] = "Gold Medal"
            elif rank == 2:
                result[idx] = "Silver Medal"
            elif rank == 3:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank)

        return result

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Algorithm (Recursive with state):
        # 1. Sort scores with indices in descending order.
        # 2. Use recursion to assign ranks one by one, storing in shared result[].
        # 3. Base case: if rank > n, stop.
        #
        # Time Complexity: O(n log n) from sorting
        # Space Complexity: O(n) for recursion depth + result storage

        n = len(score)
        score_index_pairs = [(s, i) for i, s in enumerate(score)]
        score_index_pairs.sort(key=lambda x: -x[0])

        result = [""] * n

        def assign(rank):
            # Base case
            if rank > n:
                return
            s, idx = score_index_pairs[rank - 1]
            if rank == 1:
                result[idx] = "Gold Medal"
            elif rank == 2:
                result[idx] = "Silver Medal"
            elif rank == 3:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank)
            # Recursive step
            assign(rank + 1)

        assign(1)
        return result



class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Algorithm (Pure recursion):
        # 1. Sort scores with indices in descending order.
        # 2. Define a recursive function that returns the list of ranks.
        # 3. At each step, assign rank string for current element and recurse on remainder.
        #
        # Time Complexity: O(n log n)
        # Space Complexity: O(n) recursion depth

        n = len(score)
        score_index_pairs = [(s, i) for i, s in enumerate(score)]
        score_index_pairs.sort(key=lambda x: -x[0])

        def build(rank):
            # Base case
            if rank > n:
                return []
            s, idx = score_index_pairs[rank - 1]
            if rank == 1:
                val = (idx, "Gold Medal")
            elif rank == 2:
                val = (idx, "Silver Medal")
            elif rank == 3:
                val = (idx, "Bronze Medal")
            else:
                val = (idx, str(rank))
            # Recursive step: current + rest
            return [val] + build(rank + 1)

        # Collect (index, rankString)
        indexed_ranks = build(1)

        # Build result array from recursion output
        result = [""] * n
        for idx, rank_str in indexed_ranks:
            result[idx] = rank_str

        return result










