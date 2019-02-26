clean:
	rm -rf '***.adoc'
	rm -rf '**/*.html'
build:
	python3 main.py	
html:
	asciidoctor -d article -s '**/*.adoc'
book:
	asciidoctor -d book  '**/*.adoc'
view:
	open instance-types.html
