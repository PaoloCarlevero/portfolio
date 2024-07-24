import java.util.Iterator;
import java.util.NoSuchElementException;

import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] items = (Item[]) new Object[2];
    private int size = 0;

    // construct an empty randomized queue
    public RandomizedQueue() {
    } 

    // is the queue empty?
    public boolean isEmpty() {
        return size == 0;
    } 

    // return the number of items on the queue
    public int size() {
        return size;
    } 

    // add the item
    public void enqueue(Item item) {
        if (item == null) {
            throw new NullPointerException("Can't enqueue null item");
        }
        this.items[size++] = item;
        if (size == this.items.length) {
            resize(2 * this.items.length);
        }
        swapItem();
    } 

    // remove and return a random item
    public Item dequeue() {
        if (size == 0) {
            throw new NoSuchElementException("Can't dequeue, queue is empty");
        }
        Item item = this.items[--size];
        if (size > 0 && size == this.items.length / 4) {
            resize(this.items.length / 2);
        }
        this.items[size] = null;
        return item;
    } 

    // return (but do not remove) a random item
    public Item sample() {
        if (size == 0) {
            throw new NoSuchElementException("Can't dequeue, queue is empty");
        }
        int i = StdRandom.uniformInt(size);
        return this.items[i];
    } 

    public Iterator<Item> iterator() {
        return new RQIterator();
    }

    private class RQIterator implements Iterator<Item> {
        private int i;

        public boolean hasNext() {
            return items[i] != null;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }

        public Item next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            } else {
                Item item = items[i++];
                return item;
            }
        }
    }

    private void resize(int capacity) {
        Item[] copy = (Item[]) new Object[capacity];
        for (int i = 0; i < size; i++)
            copy[i] = items[i];
        items = copy;
    }

    private void swapItem() {
        int i = StdRandom.uniformInt(size);
        Item temp = items[i];
        items[i] = items[size - 1];
        items[size - 1] = temp;
    }

    public static void main(String[] args) {
    }
}