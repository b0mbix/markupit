# Poetry quick intro

1. Installation: https://python-poetry.org/docs/

    I've installed via pipx. If u don't have pipx, there is also link on how to install it on the page I provided earlier. Pls don't install pipx via apt, it's outdated. Installation via pip works as charm.

2. Create `poetry` venv and install project:

    ```bash
    poetry shell
    poetry install
    ```

3. To open the app use:

    ```bash
    markupit
    ```

    And to run tests:

    ```bash
    pytest
    ```

4. To format/check code with `ruff` run the following command:

    ```bash
    ruff check
    ruff format
    ```
    More ruff commands here: https://docs.astral.sh/ruff/tutorial/

5. If you want to add a new dependency, you can run the following command:

    ```bash
    poetry add <package_name>
    ```

    Keep in mind that some packages might be installed as dev dependencies, so you might want to add `--group dev` flag (`--group test ` for test dependencies).

6. There are pre-commit hooks. They check for code formatting and linting. If you want to run them manually, you can run the following command:

    ```bash
    pre-commit run --all-files
    ```

    Also, if u want this hooks to run automatically before commit, you can install them with the following command:

    ```bash
    pre-commit install
    ```

    Note: installing this hook will not let you commit if there are any issues with formatting or linting that can't be fixed automatically. Therefore, installing it is highly recommended.

6. Testing:

    Run following command if youu want to test code with your active python version:

    ```bash
    poetry run pytest
    ```

    Using `tox` you can test code with multiple python versions:

    ```bash
    poetry run tox
    ```

    Currently supported versions: 3.10, 3.11, 3.12.
    Note: you will need to have this python version installed in your system.

    After `tox` testing u can also view code coverage by tests.

    That's it for now! ᕦ(ò_óˇ)ᕤ
