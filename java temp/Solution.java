class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode front = new ListNode();
        ListNode back = new ListNode();
        int counter = 0;
        front = head;
        while (counter <= n + 1 && front.next != null) {
            front = front.next;
            counter++;
        }
        back = head;
        while (front.next != null) {
            front = front.next;
            back = back.next;
        }

        back.next = back.next.next;
        return head;
    }
}