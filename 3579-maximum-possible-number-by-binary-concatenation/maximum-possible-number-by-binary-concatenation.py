from itertools import permutations

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        # Convert numbers to binary strings without the '0b' prefix
        bin_nums = [bin(num)[2:] for num in nums]
        
        # Generate all permutations of the binary strings
        all_combinations = permutations(bin_nums)
        
        # Convert each permutation to a single binary string and then to an integer
        max_value = 0
        for combination in all_combinations:
            combined_bin = ''.join(combination)
            combined_int = int(combined_bin, 2)
            max_value = max(max_value, combined_int)
        
        return max_value
