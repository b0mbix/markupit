# MarkupIt

MarkupIt is a Python-based command-line interface (CLI) application designed to easily convert markup languages. It provides a simple way to convert Markdown (GitHub Flavored Markdown) files into Typst and LaTeX formats.

[Read the full documentation here.](https://b0mbix.github.io/markupit/)

## Installation
### Prerequisites
`python` and `poetry` have to be installed.

### Installation
To install MarkupIt, follow these steps in cloned repository:
```sh
# create a virtual environment
poetry shell

#install the package
poetry install

#run the package
markupit
```

## Usage
Once installed, you can use the `markupit` command to convert your Markdown files. The basic usage is as follows:

```sh
# output written on screen
markupit --from <input_format> --to <output_format> -i <input_file>
# output written to file
markupit --from <input_format> --to <output_format> -i <input_file> -o <output_file>
```

### Example
To convert a Markdown file named `example.md` to Typst and LaTeX formats:
```sh
markupit --from md --to typst -i example.md -o example.typ
markupit --from md --to latex -i example.md -o example.tex
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors and contact
This project was created on Warsaw University of Technology by students:
- Jakub Bąba <jakub.baba.stud@pw.edu.pl>
- Hubert Brzóskniewicz <hubert.brzoskniewicz.stud@pw.edu.pl>
- Nikita Sushko <nikita.sushko.stud@pw.edu.pl>

### Project mentor
- [dr inż. Łukasz Neumann](https://repo.pw.edu.pl/info/author/WUT7244d020213e4e41ac349f81b7b6f3b0/%25C5%2581ukasz%2BNeumann+title?affil=IN&r=publication&lang=pl)
