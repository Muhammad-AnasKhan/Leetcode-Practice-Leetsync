class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # jewels = set(jewels)
        # count = 0
        # for s in stones:
        #     if s in jewels:
        #           count +=1
        # return count

        # one liner for the above
        return sum(num_jewels in set(jewels) for num_jewels in stones)

        