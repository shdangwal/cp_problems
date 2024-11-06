using System.Collections.Generic;

public class Solution
{
    public class ListNode
    {
        public int val;
        public ListNode next;

        public ListNode(int val, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }
    }

    public int LengthOfLongestSubstring(string s)
    {
        int result = 0;
        var map = new Dictionary<int, int>();
        int i = 0;
        for (int j = 0; j < s.Length; j++)
        {
            if (map.ContainsKey(s[j]))
            {
                i = Math.Max(result, j - i + 1);
            }
            result = Math.Max(result, j - i + 1);
            map[s[j]] = j + 1;
        }
        return result;
    }

    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
        ListNode result = new ListNode(0);
        ListNode curr = result;
        int carry = 0;
        while (l1 != null || l2 != null)
        {
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;
            int sum = x + y + carry;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }
        if (carry > 0)
        {
            curr.next = new ListNode(carry);
        }
        return result.next;
    }

    public int[] TwoSum(int[] nums, int target)
    {
        var numMap = new Dictionary<int, int>();

        for (ushort i = 0; i < nums.Length; i++)
        {
            var rightNum = target - nums[i];
            if (numMap.ContainsKey(rightNum))
            {
                return new int[2] { numMap[rightNum], i };
            }
            numMap[nums[i]] = i;
        }

        return new int[2] { 0, 0 };
    }
}
