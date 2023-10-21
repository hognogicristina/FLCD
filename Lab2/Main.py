from SymbolTable import SymbolTable

def main():
    symbol_table = SymbolTable(10)

    symbol_table.add_symbol("x")
    symbol_table.add_symbol("y")
    symbol_table.add_symbol("z")

    code_x = symbol_table.get_code("x")
    if code_x is not None:
        print(f"Code for symbol 'x': {code_x}")
    else:
        print("Symbol 'x' not found in the symbol table.")

    code_w = symbol_table.get_code("w")
    if code_w is not None:
        print(f"Code for symbol 'w': {code_w}")
    else:
        print("Symbol 'w' not found in the symbol table.")

    print(symbol_table)

if __name__ == "__main__":
    main()

'''
Output:
Code for symbol 'x': 0
Symbol 'w' not found in the symbol table.
SymbolTable { symbols and codes=[(z, 2) ][][(y, 1) ][][(x, 0) ][][][][][] }
'''