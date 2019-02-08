# reversi
Generate very tiny reverse shell binaries for Linux!

Usage:
    python3 reversi.py RHOST RPORT OUTFILE

Supply RHOST, RPORT, and optionally an OUTFILE name.

Using binary minification concepts detailed [here](https://medium.com/@dmxinajeansuit/elf-binary-mangling-pt-2-golfin-7e5c82bb482c) and [here](https://medium.com/@dmxinajeansuit/elf-binary-mangling-part-3-weaponization-6e11971108b3), reversi.py is built for rapid creation of very tiny 64 bit elf binaries that you can use to launch reverse shells back to you. It also generates a handy one liner that you can use to paste into most Linux based terminals to launch your binary and background it. 

reversi.asm is the annotated assembly source for the binary that reversi.py is based around. You can compile your own shell with:

    nasm -f bin -o rshell reversi.asm

