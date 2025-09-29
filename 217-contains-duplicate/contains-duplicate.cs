public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        if (nums.Length < 2) 
            return false;
        var seen = new HashSet<int>();
        foreach(var i in nums){
            if(seen.Contains(i))
                return true;
            else
                seen.Add(i);
        }
        return false;

    }
}