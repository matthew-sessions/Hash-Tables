# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        pos = self._hash(key) % self.capacity
        if self.storage[pos] != None:
            node = self.storage[pos]
            while node:
                if node.key == key:
                    node.value = value
                    break
                elif node.next == None:
                    node.next = LinkedPair(key, value)
                    break
                else:
                    node = node.next

        else:
            self.storage[pos] = LinkedPair(key, value)
        


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pos = self._hash(key) % self.capacity
        check = self.storage[pos]
        if self.storage[pos] == None:
            return('Key not found')
        if check.next == None:
            if check.key == key:
                check.value = None
                return
            else:
                return('Key not found')
 
        while check:
            if check.key == key:
                check.value = None
                break
            
            check = check.next
        return('Key not found')




    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pos = self._hash(key) % self.capacity
        check = self.storage[pos]
        
        res = None
        while check != None:
            if check.key == key:
                res = check.value
                return(res)
            else:
                check = check.next
        return('Key not found')


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in self.storage:
            if i != None:
                check = i
                
                while check:
                    key = check.key
                    value = check.value
                    pos = self._hash(key) % self.capacity
                    node = new_storage[pos]
                    if node != None:
                        while node:
                            if node.next != None:
                                node = node.next
                            else:
                                node.next = LinkedPair(key, value)
                                node = None
                    else:
                        new_storage[pos] = LinkedPair(key, value)

                    check = check.next

        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)
    ht.insert('this', 'uaua')

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
