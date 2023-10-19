from HashTable import HashTable

class SymbolTable(HashTable):
    def __init__(self, capacity):
        super().__init__(capacity)

    # Add a symbol to the symbol table with its associated attributes
    def add_symbol(self, symbol, attributes):
        # Get the hash value for the symbol
        hash_value = self.get_hash_value(symbol)
        # If the symbol is not already in the symbol table, add it with its attributes
        if not self.contains(symbol):
            # Add the symbol and its attributes at the beginning of the bucket
            self.hashTable[hash_value].insert(0, (symbol, attributes))

    # Retrieve the attributes of a symbol from the symbol table
    def get_attributes(self, symbol):
        # Get the hash value for the symbol
        hash_value = self.get_hash_value(symbol)
        for item in self.hashTable[hash_value]:
            if item[0] == symbol:
                return item[1]  # Return the attributes associated with the symbol
        return None

    def __str__(self):
        result = "SymbolTable { symbols and attributes="
        non_empty_buckets = [bucket for bucket in self.hashTable if bucket]
        for bucket in non_empty_buckets:
            result += "["
            for item in bucket:
                result += f"({item[0]}, {item[1]}) "
            result += "]"
        empty_buckets = self.capacity - len(non_empty_buckets)
        result += "[] " * empty_buckets
        result += "}"
        return result