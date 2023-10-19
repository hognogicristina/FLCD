class HashTable:
    # Constructor to initialize the HashTable with a given capacity
    def __init__(self, capacity):
        # Create an empty list to represent the hash table with 'capacity' empty buckets
        self.hashTable = [[] for _ in range(capacity)]
        # Store the capacity of the hash table
        self.capacity = capacity

    # Method to retrieve the capacity of the hash table
    def get_capacity(self):
        return self.capacity

    # Hashing function for integers and strings
    def hash(self, key):
        if isinstance(key, int):  # If the key is an integer
            return key % self.capacity  # Use modulo to get the hash value
        elif isinstance(key, str):  # If the key is a string
            hash_val = 5381
            for c in key:
                # Update the hash value using a hashing algorithm for strings
                hash_val = ((hash_val << 5) + hash_val) + ord(c)
            return abs(hash_val) % self.capacity  # Use modulo to get the hash value

    # Check if a key exists in the hash table
    def contains(self, key):
        # Get the hash value for the key
        hash_value = self.get_hash_value(key)
        for item in self.hashTable[hash_value]:
            if item == key:
                return True  # Key is found in the hash table
        return False  # Key is not found in the hash table

    # Get the hash value for a given key (integer or string)
    def get_hash_value(self, key):
        hash_value = -1
        if isinstance(key, int):
            hash_value = self.hash(key)  # Use the hash function for integers
        elif isinstance(key, str):
            hash_value = self.hash(key)  # Use the hash function for strings
        return hash_value

    # Add a key to the hash table
    def add(self, key):
        # Get the hash value for the key
        hash_value = self.get_hash_value(key)
        # If the key is not already in the hash table, add it to the corresponding bucket
        if not self.contains(key):
            self.hashTable[hash_value].append(key)

    # Get the position (bucket index) for a key
    def get_position(self, key):
        hash_value = self.get_hash_value(key)
        if hash_value != -1:
            return hash_value  # Return the bucket index where the key would be stored
        return -1  # Key is not found or not supported

    # Custom string representation of the hash table
    def __str__(self):
        result = "SymbolTable { items="
        for bucket in self.hashTable:
            result += "["
            for item in bucket:
                result += str(item) + " "
            result += "]"
        result += " }"
        return result