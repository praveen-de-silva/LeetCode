class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = ListNode()
        temp = res
        
        crnt1 = l1
        crnt2 = l2

        while (crnt1 and crnt2):  
            r = (temp.val + crnt1.val + crnt2.val) // 10
            temp.val = (temp.val + crnt1.val + crnt2.val) % 10

            if crnt1.next or crnt2.next or r==1:
                temp.next = ListNode()
                temp = temp.next
                temp.val = r
            
            crnt1 = crnt1.next
            crnt2 = crnt2.next
            
        if crnt1:
            while (crnt1):  
                r = (temp.val + crnt1.val) // 10
                temp.val = (temp.val + crnt1.val) % 10

                if crnt1.next or r==1:
                    temp.next = ListNode()
                    temp = temp.next
                    temp.val = r
                
                crnt1 = crnt1.next

        if crnt2:
            while (crnt2):  
                r = (temp.val + crnt2.val) // 10
                temp.val = (temp.val + crnt2.val) % 10

                if crnt2.next or r==1:
                    temp.next = ListNode()
                    temp = temp.next
                    temp.val = r
                
                crnt2 = crnt2.next

        return res