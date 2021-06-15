class Node4 {
    int key;
    Node4 left;
    Node4 right;

    Node4(int k) {
        key = k;
        left = right = null;
    }
}

class Nodes_At_Distance_K_From_Root_GFG {

    public static void main(String args[]) {
        Node4 root = new Node4(10);
        root.left = new Node4(20);
        root.right = new Node4(30);
        root.left.left = new Node4(40);
        root.left.right = new Node4(50);
        root.right.right = new Node4(70);
        root.right.right.right = new Node4(80);
        int k = 2;

        printKDist(root, k);
    }

    public static void printKDist(Node4 root, int k) {
        if (root == null)
            return;

        if (k == 0) {
            System.out.print(root.key + " ");
        } else {
            printKDist(root.left, k - 1);
            printKDist(root.right, k - 1);
        }
    }
}