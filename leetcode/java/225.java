class MyStack {
    Queue<Integer> queue;

    public MyStack() {
        this.queue = new LinkedList<Integer>();
    }

    public void push(int x) {
        queue.add(x);
        System.out.println(queue);
        for(int i =1; i<queue.size(); i++){
            queue.add(queue.remove());
            System.out.println(queue);
        }
        System.out.println(queue);
    }

    public int pop() {
        return queue.remove();
    }

    public int top() {
        return queue.peek();
    }

    public boolean empty() {
        return queue.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */