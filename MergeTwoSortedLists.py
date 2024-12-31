class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp1 = list1
        temp2 = list2

        if not(temp1 or temp2):
            return

        mergedLL = ListNode()
        crnt = mergedLL

        while (temp1 and temp2):
            print(temp1.val, temp2.val)

            if temp1.val<=temp2.val:
                crnt.val = temp1.val
                temp1 = temp1.next
            else:
                crnt.val = temp2.val
                temp2 = temp2.next

            if temp1 or temp2:
                crnt.next = ListNode()
                crnt = crnt.next
        
        while (temp1):
            crnt.val = temp1.val
            temp1 = temp1.next

            if temp1:
                crnt.next = ListNode()
                crnt = crnt.next
       
        while (temp2):
            crnt.val = temp2.val
            temp2 = temp2.next

            if temp2:
                crnt.next = ListNode()
                crnt = crnt.next

        return mergedLL