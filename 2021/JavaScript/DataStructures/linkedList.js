/**
 * @LinkedList
 * - A data structure that contains HEAD, TAIL AND LENGTH.
 * - consists of nodes, and each node has a value and a pointer, pointing to the another node or null
*/

/**
 * *Singly Linked List
 * 
 *  !HEAD                    Tail
 *  [1] --> [2] --> [3] --> [4] --> null
 *!|<---------length---------->|
 * 
*/

//*Initiate the Node or Create a new Node
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

//* Initiate the LinkedList
class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    /**
     * *push(val) : adding the node at the end of the list
     * @param {*} val 
     * -> function should accept a value and create a new node using the value passed.
     * -> Handle if no head is present. If head is not set or head property is null, set the head and tail to the newly created node.
     * -> Else, if head is already present or points to a value, set the next property on the tail of the newly created node. And set the tail to the new node. And increment the length.
     */
    push(val) {
        let newNode = new Node(val);
        if(!this.head) {
            this.head = newNode;
            this.tail = this.head;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        
        this.length++;
        return this;
    }
     /**
     * *pop() : removing a node from the end of the list
     * -> If the length of the list is 0 or there are no nodes, return false
     * -> Else: loop through the list untill you reach the tail starting from the head.
     * -> Set the next property of the 2nd last node to null and set the tail to the 2nd last node. And decrement the length of the list by 1
     * -> return the entire list or return the removed node.
     * -> if the function is called on list with 1 item, then set the head and tail to null.
     */
    pop() {
        if(this.head === null) return false;

        let currentNode = this.head;
        let newTail = currentNode;

        while(currentNode.next) {
            newTail = currentNode;
            currentNode = currentNode.next;
        }
        this.tail = newTail;
        this.tail.next = null;
        this.length--;
        //check if the list is empty
        if(this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return this;

    }

}

let _linkedLinked = new SinglyLinkedList();

// * PUSH
_linkedLinked.push(1) // [1] --> null
_linkedLinked.push(8) 
_linkedLinked.push(11) 
// console.log('SinglyLinkedList: ', _linkedLinked); //* [1] --> [8] --> [11] --> null

// *POP
_linkedLinked.pop() //* [1] --> [8] --> null
// _linkedLinked.pop()
// _linkedLinked.pop()
console.log('SinglyLinkedList: ', _linkedLinked); 