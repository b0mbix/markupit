# Poetry quick intro

1. Installation: https://python-poetry.org/docs/

I've installed via pipx. If u don't have pipx, there is also link on how to install it on the page I provided earlier. Pls don't install pipx via apt, it's outdated. Installation via pip works as charm.

2. Run in main folder of the project:

```bash
poetry install
```

3. As we don't have any scripts yet in pyproject.toml, you can run the following command to run the python file and verify everything is working:

```bash
poetry run python markup_converter/simple_class.py
```

And to run tests:

```bash
poetry run pytest
```

4. To format/check code with ruff run the following command:

```bash
poetry run ruff check
```

or

```bash
poetry run ruff format
```

More ruff commands here: https://docs.astral.sh/ruff/tutorial/

5. If you want to add a new dependency, you can run the following command:

```bash
poetry add <package_name>
```

Keep in mind that some packages might be installed as dev dependencies, so you might want to add `--group dev` flag (`--group test ` for test dependencies).

Also I've added some pre-commit hooks. They check for code formatting and linting. If you want to run them manually, you can run the following command:

```bash
pre-commit run --all-files
```

Also, if u want this hooks to run automatically before commit, you can install them with the following command:

```bash
pre-commit install
```

Note: they will not let u commit if there are any issues with formatting or linting that can be fixed automatically.

That's it for now! ᕦ(ò_óˇ)ᕤ
