build:
	python setup.py bdist_wheel
	python -m twine upload dist/*

clean:
	del build dist JCryptor.egg-info
