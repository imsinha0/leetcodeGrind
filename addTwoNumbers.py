
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        elements1 = []
        elements2 = []

        while(l1!=None):
            elements1.append(l1.val)
            l1 = l1.next
        while (l2!=None):
            elements2.append(l2.val)
            l2 = l2.next


        num1 = 0
        for i in range(len(elements1)):
            num1 += elements1[i] * 10**(i)

        num2 = 0
        for i in range(len(elements2)):
            num2 += elements2[i] * 10**(i)


        total = num1 + num2
        startNode = ListNode(total%10)
        total = total//10
        currentNode = startNode
        output = startNode

        while (total != 0):
            digit = total % 10
            total = total//10
            newNode = ListNode(digit)
            currentNode.next = newNode
            currentNode = currentNode.next

        return output






if __name__ == '__main__':
    solution = Solution()
    print(solution)
