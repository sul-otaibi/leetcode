# https://leetcode.com/problems/add-two-numbers/
'''
Runtime: 88 ms, faster than 61.34% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.8 MB, less than 90.14% of Python3 online submissions for Add Two Numbers.
'''

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if 0 == l1.val and l1.next is None:
        return l2
    if 0 == l2.val and l2.next is None:
        return l1
    
    power = 1
    num1 = l1.val
    while l1.next is not None:
        l1 = l1.next
        num1 += l1.val * 10 ** power
        power += 1
    
    power = 1
    num2 = l2.val
    while l2.next is not None:
        l2 = l2.next
        num2 += l2.val * 10 ** power
        power += 1

    the_sum = num1 + num2
    result = ListNode(the_sum % 10)

    temp = result
    while the_sum // 10 != 0:
        the_sum //= 10
        temp.next = ListNode(the_sum % 10)
        temp = temp.next
    return result
