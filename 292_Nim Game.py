# 292 Nim Game
class Solution(object):
    def canWinNim(self, n):
        """
        Determine if you can win the Nim Game.
        
        :type n: int
        :rtype: bool
        """
        # You win if the number of stones is NOT a multiple of 4
        return n % 4 != 0


"""
🔹 Observations

If n = 1, 2, 3, you can take all stones and win. ✅

If n = 4, no matter what you take (1, 2, or 3), the opponent can take the rest to win. ❌

From here, a pattern emerges:

You lose if n % 4 == 0.

You win if n % 4 != 0.


n	Can you win?	Explanation
1	True	Take 1 stone → win
2	True	Take 2 stones → win
3	True	Take 3 stones → win
4	False	Any move leaves 1–3 stones → opponent wins
5	True	Take 1 stone → leaves 4 → opponent loses
8	False	Multiple of 4 → cannot force a win
"""