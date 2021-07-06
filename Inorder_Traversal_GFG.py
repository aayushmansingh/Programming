#Driver Code Starts
#Initial Template for Python 3
#Problem Link: https://practice.geeksforgeeks.org/problems/inorder-traversal/1

class Node:
    data = 0
    left = None
    right = None


def createNewNode(value):
    temp = Node()
    temp.data = value
    temp.left = None
    temp.right = None
    return temp


def newNode(root, data):
    if (root is None):
        root = createNewNode(data)
    elif (data < root.data):
        root.left = newNode(root.left, data)
    else:
        root.right = newNode(root.right, data)

    return root

# } Driver Code Ends


#User function Template for python3


#Function to return a list containing the inorder traversal of the BST.
def Order(root, a):
    # code here
    if root == None:
        return a
    a = Order(root.left, a)
    a.append(root.data)
    a = Order(root.right, a)
    return a


def inOrder(root):
    b = []
    Order(root, b)
    return b


#{
#Driver Code Starts.


def main():
    testcases = int(input())
    while (testcases > 0):
        root = None
        sizeOfArray = int(input())
        arr = [int(x) for x in input().strip().split()]
        for i in arr:
            root = newNode(root, i)

        res = inOrder(root)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

        testcases -= 1


if __name__ == "__main__":
    main()
#} Driver Code Ends
