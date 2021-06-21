//Problem Link: https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1


//Initial Template for Java

import java.util.LinkedList;
import java.util.Queue;
import java.io.*;

class Node3 {
    int data;
    Node3 left;
    Node3 right;

    Node3(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Height_of_Binary_Tree_GFG {

    static Node3 buildTree(String str) {

        if (str.length() == 0 || str.charAt(0) == 'N') {
            return null;
        }

        String ip[] = str.split(" ");
        // Create the root of the tree
        Node3 root = new Node3(Integer.parseInt(ip[0]));
        // Push the root to the queue

        Queue<Node3> queue = new LinkedList<>();

        queue.add(root);
        // Starting from the second element

        int i = 1;
        while (queue.size() > 0 && i < ip.length) {

            // Get and remove the front of the queue
            Node3 currNode = queue.peek();
            queue.remove();

            // Get the current node's value from the string
            String currVal = ip[i];

            // If the left child is not null
            if (!currVal.equals("N")) {

                // Create the left child for the current node
                currNode.left = new Node3(Integer.parseInt(currVal));
                // Push it to the queue
                queue.add(currNode.left);
            }

            // For the right child
            i++;
            if (i >= ip.length)
                break;

            currVal = ip[i];

            // If the right child is not null
            if (!currVal.equals("N")) {

                // Create the right child for the current node
                currNode.right = new Node3(Integer.parseInt(currVal));

                // Push it to the queue
                queue.add(currNode.right);
            }
            i++;
        }

        return root;
    }

    static void printInorder(Node3 root) {
        if (root == null)
            return;

        printInorder(root.left);
        System.out.print(root.data + " ");

        printInorder(root.right);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t > 0) {
            String s = br.readLine();
            Node3 root = buildTree(s);

            Solution ob = new Solution();
            System.out.println(ob.height(root));
            t--;
        }
    }
}// } Driver Code Ends

// User function Template for Java

/*
 * class Node { int data; Node left, right;
 * 
 * Node(int item) { data = item; left = right = null; } }
 */

class Solution {
    // Function to find the height of a binary tree.
    int height(Node3 node) {
        // code here
        if (node == null) {
            return 0;
        } else {
            return Math.max(height(node.left), height(node.right)) + 1;
        }
    }
}
