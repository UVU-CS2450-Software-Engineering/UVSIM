UVSim

Requirements
    - Python 3.11.x

    Python Modules
    - customtkinter
    - pytest
    - re
    - sys

Installation
    1. From .zip
        a) Unzip folder and save in desired location
    2. From GitHub
        a) Clone from git: "git clone https://github.com/UVU-CS2450-Software-Engineering/UVSIM.git"

Running UVSim
    1. Navigate to the cloned GitHub repository. It should contain the shown directories and files. 
        UVSim <- Navigate here
        | - UVSim
        | - test
        | - README.txt
        | - UVSim.py

    2.  a) Linux/Mac and some Windows systems with Python 2 alongside Python 3
            From the terminal execute one of the following commands
                - "python3 -m UVSim"
                - "python3 UVSim.py"
        b) Windows
            From CMD Prompt/Powershell execute one of the following commands
                - "python -m UVSim"
                - "python -m UVSim.py"

    3. When prompted, supply the file path to the desired program.

    4. Enter a value if/when prompted.
        * Input Restrictions: Input must be an integer from -9999 to (+)9999 [plus sign is optional]

    5. After the program has completed, press any key to close.

Program Setup
    UVSim utilizes a 100 word memory, where each word is a four digit decimal number.
    Programs will be loaded into memory with each line in the program corresponding to a word.
        * Note: If using an editor with line numbering, the memory location will be the line number minus open
    
    Valid Commands
        I/O operation:
            READ = 10 Read a word from the keyboard into a specific location in memory.
                Example: 1020 - Read a word from the keyboard and store it in memory location 20.

            WRITE = 11 Write a word from a specific location in memory to screen.
                Example: 1120 - Writes the value stored at memory location 20 to the screen.


        Load/store operations:
            LOAD = 20 Load a word from a specific location in memory into the accumulator.
                Example: 2035 - Loads the value at memory location 35 into the accumulator.

            STORE = 21 Store a word from the accumulator into a specific location in memory.
                Example: 2135 - Stores the value in the accumlator in memory location 35.


        Arithmetic operation:
            ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
                Example: 3045 - Adds the value in memory location 45 to the value in the accumulator.

            SUBTRACT = 31 Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
                Example: 3146 - Subtracts the value in memory location 46 from the value in the accumulator.

            DIVIDE = 32 Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).
                Example: 3248 - Divides the value in the accumulator by the value in memory location 48.

            MULTIPLY = 33 multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).
                Example: 3349 - Multiplies the value in the accumulator by the value in memory location 49.


        Control operation:
            BRANCH = 40 Branch to a specific location in memory
                Example: 4080 - Moves the program to memory locatio 80 and continues running from there

            BRANCHNEG = 41 Branch to a specific location in memory if the accumulator is negative.
                Example: 4120 - Moves to memory location 20 if the value in the accumulator is negative

            BRANCHZERO = 42 Branch to a specific location in memory if the accumulator is zero.
                Example: 4220 - Moves to memory location 20 if the value in the accumulator is zero.

            HALT = 43 Pause the program
                Example: 43xx OR 43 - Stops the program. 