while True:
    s = input()
    if s == "EOI":
        break
    else:
        if "nemo" in s.lower():
            print("Found")
        else:
            print("Missing")