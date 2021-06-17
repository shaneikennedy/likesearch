install:
	python -m pip install .

uninstall:
	python -m pip uninstall likesearch

test:
	python -m unittest discover

clean:
	rm -r build dist *.egg-info
