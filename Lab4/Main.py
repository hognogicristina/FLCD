# from Scanner import Scanner
from FA import FA


class Main:
    @staticmethod
    def main():
        fa = FA("L1/fa.in")
        print("1. Print states")
        print("2. Print alphabet")
        print("3. Print output states")
        print("4. Print initial state")
        print("5. Print transitions")
        print("6. Check word")
        print("7. Get matching substring")
        print("0. Exit")

        while True:
            option = int(input("> "))
            if option == 1:
                fa.print_states()
            elif option == 2:
                fa.print_alphabet()
            elif option == 3:
                fa.print_output_states()
            elif option == 4:
                fa.print_initial_state()
            elif option == 5:
                fa.print_transitions()
            elif option == 6:
                word = input("Enter word: ")
                print(fa.check_accepted(word))
            elif option == 7:
                word = input("Enter word: ")
                accepted = fa.get_next_accepted(word)
                if accepted is None:
                    print("No matching substring")
                else:
                    print(accepted)
            elif option == 0:
                break
            else:
                print("Invalid option")


if __name__ == "__main__":
    # program1 = "p1.txt"
    # program2 = "p2.txt"
    # program3 = "p3.txt"
    # program1err = "p1err.txt"
    #
    # scanner1 = Scanner()
    # scanner1.read_tokens()
    # scanner1.scan(program1)
    #
    # scanner2 = Scanner()
    # scanner2.read_tokens()
    # scanner2.scan(program2)
    #
    # scanner3 = Scanner()
    # scanner3.read_tokens()
    # scanner3.scan(program3)
    #
    # scanner4 = Scanner()
    # scanner4.read_tokens()
    # scanner4.scan(program1err)

    Main.main()
