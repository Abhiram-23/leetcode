import itertools
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        if len(tiles) == 1:
            return 1
        def get_permutations(string):
            return [''.join(p) for p in itertools.permutations(string)]

        def get_combinations(string):
            combinations = []
            for i in range(len(string) + 1):
                combinations.extend([''.join(c) for c in itertools.combinations(string, i)])
            return combinations
        op = set(get_combinations(tiles))

        for i in op:
            if(len(i)>1):
                op=op.union(set(get_permutations(i)))
        return len(op)-1