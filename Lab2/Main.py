from HashTable import HashTable

def main():
    intTable = HashTable(10)
    intTable.add(5)
    intTable.add(15)
    intTable.add(25)

    print(intTable)

    stringTable = HashTable(10)
    stringTable.add("apple")
    stringTable.add("banana")
    stringTable.add("cherry")

    print(stringTable)

if __name__ == "__main__":
    main()
