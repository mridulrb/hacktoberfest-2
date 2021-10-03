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

}

let _linkedLinked = new SinglyLinkedList();

// * PUSH
_linkedLinked.push(1) // [1] --> null
_linkedLinked.push(8) 
_linkedLinked.push(11) 
console.log('SinglyLinkedList: ', _linkedLinked); //* [1] --> [8] --> [11] --> null

