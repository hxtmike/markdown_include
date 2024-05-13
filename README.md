# markdown_include

This is a simple Python script that processes Markdown files by including the contents of other Markdown files.

The script takes in a Markdown file as input, looks for lines that are similar to `<!-- include (filename) -->` (Parentheses are necessary to identify the path) and treats them as include directives. For each include directive, the script reads the specified file and writes its contents to the output file. The result is a new Markdown file that includes the contents of all included files.

## Github

<https://github.com/hxtmike/markdown_include>

## Usage

To use the script, simply pass the input file name and the output file name as command-line arguments. The script will process the input file, generate the output file, and exit. Here's an example of how to run the script:

```shell
md_incl input_file.md output_file.md
```

This script will be added as a command after installation

## Features

+ Processes Markdown files by including the contents of other Markdown files
+ Supports include directives in the format of `<!-- include (filename) -->` (Parentheses are necessary to identify the path)
+ Outputs a new Markdown file that includes the contents of the included files
+ Takes in input and output file names as command-line arguments

## Requirements

+ `>Python 3.8`
+ A text editor to modify the input and included files

## Installation

```shell
pip install md-incl
```

It could be used in some building system like `Makefile`, which allows for the automatic assembly of large and complex reports and papers.

## Contributions

If you'd like to contribute to the development of this script, feel free to fork the repository and submit a pull request. I'll be happy to review your changes and merge them into the main codebase.

## License

This script is licensed under the MIT License. See the LICENSE file for details.
