# Count Vowels and Consonants in a string

def countvowcons(inp_str):
    countvow = 0
    countcons = 0
    for char in inp_str:
        match char:
            case "a":
                countvow = countvow + 1
            case "e":
                countvow = countvow + 1
            case "i":
                countvow = countvow + 1
            case "o":
                countvow = countvow + 1
            case "u":
                countvow = countvow + 1
            case "A":
                countvow = countvow + 1
            case "E":
                countvow = countvow + 1
            case "I":
                countvow = countvow + 1
            case "O":
                countvow = countvow + 1
            case "U":
                countvow = countvow + 1
            case _:
                countcons = countcons + 1
    return countvow,countcons


inp_str=input("enter the string\n")
result = countvowcons(inp_str)
print(f"number of vowels in {inp_str} is {result[0]}")
print(f"number of consonants in {inp_str} is {result[1]}")


