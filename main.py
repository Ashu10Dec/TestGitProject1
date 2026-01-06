import sys

def main():
    if len(sys.argv) < 2:
        print("Please pass a number (1 or 2)")
        return
    
    arg = sys.argv[1]
    
    if arg == "1":
        print("HELLO")
    elif arg == "2":
        print("BYE")
    else:
        print(f"Unknown argument: {arg}. Please pass 1 or 2")

if __name__ == "__main__":
    main()

