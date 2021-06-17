install:
	python -m pip install .

uninstall:
	python -m pip uninstall likesearch

clean:
	rm -r build dist *.egg-info
