export TEXINPUTS=.:latex/:
LATEX=pdflatex
FLAGS=-half-on-error -shell-escape
BUILD_FOLDER=build/
OUTPUT=$(BUILD_FOLDER)/vnoi-magazine-2023.pdf

all: $(OUTPUT)
	
$(OUTPUT): # TODO dependencies
	cd src; \
	$(LATEX) $(FLAGS) -output-directory=../$(BUILD_FOLDER) vnoi-magazine-2023.latex
	
install-deps:
	pip install marko
	
render-articles:
	export PYTHONPATH="${PYTHONPATH}:."; \
	mkdir -p src/articles; \
	for article in ./articles/*.md; do \
		cat $$article | marko --renderer scripts.MarkoLatexRenderer > src/$${article//.md/.latex}; \
	done
