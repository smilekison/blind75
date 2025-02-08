class Solution:
    def reverseList(head):
        newValue = sorted(head, reverse=True)

        return newValue
    

    print(reverseList([1,2,3,4,5]))