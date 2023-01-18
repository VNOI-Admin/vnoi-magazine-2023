export TEXINPUTS=.:latex/:
LATEX=pdflatex
FLAGS=-halt-on-error -shell-escape
BUILD_FOLDER=build/
OUTPUT=$(BUILD_FOLDER)/vnoi-magazine-2023.pdf

all: magazine
	
clean:
	rm -rf build/

$(BUILD_FOLDER):
	mkdir -p $(BUILD_FOLDER)
	
magazine: | $(BUILD_FOLDER)
	cd src; \
	$(LATEX) $(FLAGS) vnoi-magazine-2023.latex; \
	cp vnoi-magazine-2023.pdf ../
	
install-deps:
	pip install marko
	
render-articles:
	export PYTHONPATH="${PYTHONPATH}:./scripts/"; \
	mkdir -p src/articles; \
	for article in ./articles/*.md; do \
		echo Processing $$article; \
		cat $$article | marko -e marko_latex_extension -o src/$${article//.md/.latex}; \
	done
