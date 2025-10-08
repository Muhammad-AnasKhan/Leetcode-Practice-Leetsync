public class Solution {
    public bool IsAnagram(string s, string t) {
        var s1 = string.Join( "",s.OrderBy(a => a));
        var s2 = string.Join( "",t.OrderBy(a => a));
        return s1==s2;
    }
}