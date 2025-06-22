class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keys_used = set()
        # hashmap = {}

        # for index, val in enumerate(strs):
        #     if index not in keys_used:
        #         key = ''.join(sorted(val))
        #         # print(key)
        #         for j_index, j_val in enumerate(strs):
        #             if j_index not in keys_used:
        #                 # print(key, ''.join(sorted(j_val)))
        #                 if key == ''.join(sorted(j_val)):
        #                     hashmap_val = hashmap.get(key, [])
        #                     hashmap_val.append(j_val)
        #                     hashmap[key] = hashmap_val
        #                     keys_used.add(j_index)
        # return list(hashmap.values())

        # refined logic
        anagram_map = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            anagram_map[sorted_word] = anagram_map.get(sorted_word, [])
            anagram_map[sorted_word].append(i)
        return list(anagram_map.values())