import sys
import re

def main():
    args = sys.argv[1:]  # Exclude script name
    if not args:
        print("none")
        return
    
    for arg in args:
        if not re.search(r"ism$", arg):  # Check if it does NOT end with "ism"
            print(arg + "ism")

if __name__ == "__main__":
    main()
