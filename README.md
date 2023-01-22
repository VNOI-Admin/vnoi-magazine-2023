# VNOI magazine 2023

[Read online here](https://oj.vnoi.info/post/428-vnoi-magazine-2023)

## Requisite 
- Texlive (for `pdflatex` and packages used in this repo).
- Makefile
- Python3, with the following packages (can be installed with `make
install-dependencies`)
  + [`marko` markdown parser](https://marko-py.readthedocs.io/en/latest/)
  + [`pyyaml`](https://pyyaml.org/)
  
## Building
```sh
make
```

## Generate latex source from markdown
```sh
make render-articles
```
With this command, all the markdown files in `./articles` and `./interviews`
will be transformed into the corresponding latex files in `./src/articles` and
`./src/interviews` respectively.
