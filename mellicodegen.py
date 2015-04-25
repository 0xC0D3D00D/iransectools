from random import randint

def main():
        code = 0
        control_digit = 0
        
        for i in range(0,9):
                digit = randint(1,9)
                code *= 10
                code += digit
                control_digit += (10-i)*digit

        control_digit %= 11
        if control_digit<2:
                code = code*10 + control_digit
        else:
                code = code*10 + 11-control_digit

        print "Generated Mellicode: " + str(code)

if __name__ == "__main__":
        main()
