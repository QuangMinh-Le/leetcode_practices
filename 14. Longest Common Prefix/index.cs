public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        int x = strs.Length;

        if (x == 1)
        {
            return strs[0];
        }
        else
        {
            string res = "";
            bool checker = true;
            
            for (global::System.Int32 i = 0; i < strs[0].Length; i++)
            {
                for (global::System.Int32 j = 0; j < x; j++)
                {
                    if (i > strs[j].Length-1 || strs[0][i] != strs[j][i])
                    {
                        return res;
                    }
                }
                
                res += strs[0][i];
                
            }
            
            return res;

        }
    }
}