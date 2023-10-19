from SymbolTable import SymbolTable

def main():
    symbol_table = SymbolTable(10)

    symbol_table.add_symbol("x", {"type": "int", "value": 4})
    symbol_table.add_symbol("y", {"type": "real", "value": 2.02})
    symbol_table.add_symbol("z", {"type": "string", "value": "I love cats"})

    symbol_x_attributes = symbol_table.get_attributes("x")
    if symbol_x_attributes:
        print(f"Attributes for symbol 'x': {symbol_x_attributes}")
    else:
        print("Symbol 'x' not found in the symbol table.")

    symbol_w_attributes = symbol_table.get_attributes("w")
    if symbol_w_attributes:
        print(f"Attributes for symbol 'w': {symbol_w_attributes}")
    else:
        print("Symbol 'w' not found in the symbol table.")

    print(symbol_table)

if __name__ == "__main__":
    main()

'''
Output:
Attributes for symbol 'x': {'type': 'int', 'value': 4}
Symbol 'w' not found in the symbol table.
SymbolTable { symbols and attributes=[(x, {'type': 'int', 'value': 4}) ][(y, {'type': 'real', 'value': 2.02}) ][(z, {'type': 'string', 'value': 'I love cats'}) ][] [] [] [] [] [] [] }
'''