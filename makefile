export TEXINPUTS=.:latex/:
LATEX=pdflatex
FLAGS=-halt-on-error -shell-escape
BUILD_FOLDER=build/
OUTPUT=$(BUILD_FOLDER)/vnoi-magazine-2023.pdf

all: magazine

install-dependencies:
	pip install marko pyyaml
	
clean:
	rm -rf build/

$(BUILD_FOLDER):
	mkdir -p $(BUILD_FOLDER)
	
magazine: render-articles | $(BUILD_FOLDER)
	cd src; \
	$(LATEX) $(FLAGS) vnoi-magazine-2023.latex; \
	cp vnoi-magazine-2023.pdf ../
	
install-deps:
	pip install marko
	
render-articles:
	export PYTHONPATH="${PYTHONPATH}:./scripts/"; \
	mkdir -p src/articles; \
	for article in ./articles/*.md ./interviews/*.md; do \
		echo Processing $$article; \
		cat $$article | marko -e marko_latex_extension -o src/$${article//.md/.latex}; \
	done
	
preprocess-interviews:
	mkdir -p src/interviews; \
	for interview in ./interviews/*.txt; do \
		echo Processing $$interview; \
		cat $$interview | python ./scripts/preprocess-interview.py > src/$${interview//.txt/.latex}; \
	done
