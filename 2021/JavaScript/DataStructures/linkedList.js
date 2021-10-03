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
     /**
     * *shift() : removes a node from the start of the list
     * -> Similar to pop, it removes the node from the beginning of the list.
     * -> Check if head is equal to null then return false.
     * -> Else: store the current head in a variable and point the current head to the next property of the current head. And decrement the length by 1
     * -> If the current length is equal to 0 after removing the node, then set the head and tail to null and return the list.
     */
    shift() {
        if(!this.head) return false

        let currentHead = this.head;
        this.head = currentHead.next;
        this.length--;

        if(this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return this;
    }

    /**
     *  *unshift(val) : adds at the beginning of the list
     *  @param {*} val
     * -> Similar to push() method, accepts a value and creates a new Node and adds at the beginning of the list.
     * -> If head is null, set the head and tail to the newly created node.
     * -> Else: set next property of the newly create node to current head and set current head to new node.
     * -> increment the length by 1 and return the list.
     */
    unshift(val) {
        let newNode = new Node(val);
        if(!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }
        this.length++;
        return this;

    }

    /**
     * *get(): gets a particular node from the list
     * -> accepts an index and gets the node at that particular list.
     * -> traverse the entire list till we get the node and return the node
     */
    get(index) {
        if(index < 0 || index >= this.length) return null;

        //traversing the list
        let currentNode = this.head;
        for(let i = 0; i <= index; i++) {
            if(i === index) return currentNode;
            //update the current Node
            currentNode = currentNode.next;
        }
    }

    /**
     * *set(): sets a node at a particular index and replaces the existing node.
     * -> accepts a value and index
     * -> we can get the particular node by using the get method.
     * -> And replace the value of the found node with the provided value.
     */
    set(val, index) {
        let foundValue = this.get(index);
        if(foundValue) {
            foundValue.value = val;
            return true;
        }
        return false
    }

}

let _linkedLinked = new SinglyLinkedList();

// * PUSH
_linkedLinked.push(1) // [1] --> null
_linkedLinked.push(8) 
_linkedLinked.push(11) 
// console.log('SinglyLinkedList: ', _linkedLinked); //* [1] --> [8] --> [11] --> null

// *POP
// _linkedLinked.pop() //* [1] --> [8] --> null
// _linkedLinked.pop()
// _linkedLinked.pop()

// * SHIFT
// _linkedLinked.shift() //* [8] --> [11] --> null
// _linkedLinked.shift() 
// _linkedLinked.shift()

// * UNSHIFT
// _linkedLinked.unshift(99) //* [99] --> [1] --> [8] --> [11] --> null 

// console.log(_linkedLinked.get(2));
// console.log(_linkedLinked.get(0));
// console.log(_linkedLinked.get(10));
_linkedLinked.set(9999, 0)
console.log('SinglyLinkedList: ', _linkedLinked); 
