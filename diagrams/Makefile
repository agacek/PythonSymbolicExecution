MMD_FILES := $(wildcard *.mmd)
PNG_FILES := $(MMD_FILES:.mmd=.png)

.PHONY: all
all: $(PNG_FILES)

# mmdc: https://github.com/mermaid-js/mermaid-cli
%.png: %.mmd
	mmdc -i $< -o $@ -s 10

clean:
	rm -f $(PNG_FILES)
