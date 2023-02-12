.PHONY: lint

lint:
	black . -l 110 --target-version py39
