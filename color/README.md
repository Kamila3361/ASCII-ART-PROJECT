## ascii-art-color

### Objectives

You must follow the same [instructions](../README.md) as in the first subject but this time with colors.

The output should manipulate colors using the **flag** `--color=<color> <letters to be colored>`, in which `--color` is the flag and `<color>` is the color desired by the user and `<letters to be colored>` is the letter or letters that you can chose to be colored. These colors can be achieved using different notations (color code systems, like `RGB`, `hsl`, `ANSI`...), it is up to you to choose which one you want to use.

- You should be able to choose between coloring a single letter or a set of letters.
- If the letter is not specified, the whole `string` should be colored.
- The flag must have exactly the same format as above, any other formats must return the following usage message:

```console
Usage: python3 main.py [OPTION] [STRING]

EX: python3 main.py --color=<color> <letters to be colored> "something"
```

If there are other `ascii-art` optional projects implemented, the program should accept other correctly formatted `[OPTION]` and/or `[BANNER]`.
Additionally, the program must still be able to run with a single `[STRING]` argument.

### Instructions

- Your project must be written in **Python**.

### Allowed packages

- Only the [standard Python](https://docs.python.org/3/library/) packages are allowed

This project will help you learn about :

- The Python file system(**fs**) API
- Color converters
- Data manipulation
- Terminal display
