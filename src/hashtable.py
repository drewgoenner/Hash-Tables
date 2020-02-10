
import hashlib
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
        # Find the index of the key
        index = self._hash_mod(key)
        # If collision, print error
        if self.storage[index]:
            print("ERROR: collision")
            return
        # If empty, create and add a new entry
        else:
            self.storage[index] = LinkedPair( key, value )
            
        
            



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.

        '''
        index = self._hash_mod(key)
        #If key not found, print warning

        if not self.storage[index]:
            print("ERROR: No key found")
            return
        elif not self.storage[index].value:
            print("ERROR: Nothing to delete")
        else:
            del(self.storage[index].value)
            return
            


        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if not self.storage[index]:
            return None

        else:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                print("ERROR: Keys don't match")
                


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #double capacity
        self.capacity *= 2
        #create new_storage and set to new doubled capacity
        new_storage = [None] * self.capacity

        #for each item in stoarage, has the key and add the pair to new storage
        for item in self.storage:
            if item:
                new_index = self._hash_mod(item.key)
                new_storage[new_index] = LinkedPair(item.key, item.value)
        #set storage to new_storage
        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

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
