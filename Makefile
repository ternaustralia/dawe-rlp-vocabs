test:
	pytest --cov=linkeddata_api tests/ --cov-report html --log-cli-level=info

htmlcov:
	python -m http.server -d htmlcov