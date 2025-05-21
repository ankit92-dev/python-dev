filename = "demo.txt"

# 1. w mode - Write (creates or overwrites file)
with open(filename, "w") as f:
    f.write("Line 1: Written with w mode\n")
print("1. 'w' mode: File created or overwritten.")

# 2. r mode - Read (file must exist)
with open(filename, "r") as f:
    content = f.read()
    print("\n2. 'r' mode: Reading file content:")
    print(content)

# 3. a mode - Append (adds to end)
with open(filename, "a") as f:
    f.write("Line 2: Appended with a mode\n")
print("\n3. 'a' mode: Appended new line.")

# 4. r+ mode - Read and write (doesn't overwrite, file must exist)
with open(filename, "r+") as f:
    print("\n4. 'r+' mode: Original content:")
    print(f.read())

    f.seek(0)
    f.write("Line 1: Overwritten by r+ mode\n")
print("Modified first line using 'r+'.")

# 5. w+ mode - Write and read (overwrites file)
with open(filename, "w+") as f:
    f.write("Line 1: Written with w+ mode\n")
    f.seek(0)
    print("\n5. 'w+' mode: After writing and reading:")
    print(f.read())

# 6. a+ mode - Append and read (adds at end, can read entire file)
with open(filename, "a+") as f:
    f.write("Line 2: Appended with a+ mode\n")
    f.seek(0)
    print("\n6. 'a+' mode: Reading after appending:")
    print(f.read())
    
    
#Note:-
"""
Why use "with" for files in Python?

Using with open(...) as f: is the recommended way because it:
1.Automatically closes the file after the block finishes.
2.Prevents file resource leaks.
3.Is cleaner and less error-prone.
4.Professionals use it

Summary:

Method	        Auto Closes     Safer in errors	    Recommended
with open()	        Yes	        Yes	                 Yes
open()+close()	    No	        No	                 Only for very simple scripts
"""
