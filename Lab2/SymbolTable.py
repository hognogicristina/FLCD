from HashTable import HashTable

class SymbolTable(HashTable):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.next_code = 0

    # Add a symbol to the symbol table with an associated incremental value
    def add_symbol(self, symbol):
        # Get the hash value for the symbol
        hash_value = self.get_hash_value(symbol)
        # If the symbol is not already in the symbol table, add it with the next code
        if not self.contains(symbol):
            code = self.next_code
            self.next_code += 1
            # Add the symbol and its code at the beginning of the bucket
            self.hashTable[hash_value].insert(0, (symbol, code))

    # Retrieve the code associated with a symbol from the symbol table
    def get_code(self, symbol):
        # Get the hash value for the symbol
        hash_value = self.get_hash_value(symbol)
        for item in self.hashTable[hash_value]:
            if item[0] == symbol:
                return item[1]  # Return the code associated with the symbol
        return None

    def __str__(self):
        result = "SymbolTable { symbols and codes="
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
