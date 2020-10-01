class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.entries = [None] * capacity
        self.capacity = capacity
        self.num_entries = 0
        # Your code here


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_entries/self.capacity
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash = 14695981039346656037
        for char in key:
            hash = hash * 1099511628211
            hash = hash ^ ord(char)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            hash = (( hash << 5) + hash) + ord(char)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value, storage=None):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if storage is None:
            storage = self.entries
        hI = self.hash_index(key)
        if storage[hI] is None:
            storage[hI] = HashTableEntry(key,value)
            self.num_entries += 1
        else:
            stored = False
            bucket = storage[hI]
            while not stored:
                if bucket.key == key:
                    bucket.value = value
                    stored = True
                elif bucket.next is None:
                    bucket.next = HashTableEntry(key,value)
                    self.num_entries += 1
                    stored = True
                else:
                    bucket = bucket.next
        # Your code here


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hI = self.hash_index(key)
        if self.entries[hI] is None:
            print("No entry found with key {} - {}".format(key,hI))
            return None
        else:
            if self.entries[hI].key == key:
                if self.entries[hI].next is not None:
                    self.entries[hI] = self.entries[hI].next
                else:
                    self.entries[hI] = None
                self.num_entries -= 1
                print("Removed hi")
                return None
            elif self.entries[hI].next is None:
                print("No entry found with key {} - {}".format(key,hI))
                return None
            else:
                parent = self.entries[hI]
                child = parent.next
                while True:
                    if child.key == key:
                        if child.next is not None:
                            parent.next = child.next
                        else:
                            parent.next = None
                        self.num_entries -= 1
                        print("Removed pc")
                        return None
                    elif child.next is None:
                        print("No entry found with key {} - pc".format(key))
                        return None
                    else:
                        parent = child
                        child = child.next


        # Your code here


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hI = self.hash_index(key)
        if self.entries[hI] is None:
            return None
        else:
            if self.entries[hI].key == key:
                return self.entries[hI].value
            elif self.entries[hI].next is None:
                    return None
            else:
                found = False
                bucket = self.entries[hI].next
                while not found:
                    if bucket.key == key:
                        return bucket.value
                    else:
                        if bucket.next is None:
                            return None
                        else:
                            bucket = bucket.next
        # Your code here
        #
    def get_all(self):
        """
        Retrieves all entries as a k,v tuple in a list
        """
        all_array = []
        for i in range(len(self.entries)):
            if self.entries[i] is not None:
                all_array.append((self.entries[i].key,self.entries[i].value))
                if self.entries[i].next is not None:
                    bucket = self.entries[i].next
                    while bucket is not None:
                        all_array.append((bucket.key,bucket.value))
                        bucket = bucket.next
        return all_array

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        new_store = [None] * new_capacity
        self.num_entries = 0
        for k,v in self.get_all():
            self.put(k,v,new_store)
        self.entries = new_store
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
