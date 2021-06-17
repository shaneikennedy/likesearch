install:
	python -m pip install .

uninstall:
	python -m pip uninstall likesearch

test:
	python -m unittest discover

lint:
	pylint --disable=all --enable=unused-import likesearch/**/*.py

clean:
	rm -r build dist *.egg-info
