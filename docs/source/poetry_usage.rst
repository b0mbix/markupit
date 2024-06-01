
Poetry quick intro
==================

1. Installation: `Poetry Documentation <https://python-poetry.org/docs/>`_

    I've installed via pipx. If you don't have pipx, there is also a link on how to install it on the page I provided earlier. Please don't install pipx via apt, it's outdated. Installation via pip works as a charm.

2. Create ``poetry`` venv and install the project:

.. code-block:: bash

   poetry shell
   poetry install

3. To open the app use:

.. code-block:: bash

   markupit


And to run tests:

.. code-block:: bash

   pytest

4. To format/check code with ``ruff`` run the following command:

.. code-block:: bash

   ruff check
   ruff format


More ruff commands here: `Ruff Documentation <https://docs.astral.sh/ruff/tutorial/>`_

5. If you want to add a new dependency, you can run the following command:

.. code-block:: bash

   poetry add <package_name>


Keep in mind that some packages might be installed as dev dependencies, so you might want to add ``--group dev`` flag ( ``--group test`` for test dependencies).

6. There are pre-commit hooks. They check for code formatting and linting. If you want to run them manually, you can run the following command:

.. code-block:: bash

   pre-commit run --all-files


Also, if you want these hooks to run automatically before commit, you can install them with the following command:

.. code-block:: bash

   pre-commit install


Note: installing this hook will not let you commit if there are any issues with formatting or linting that can't be fixed automatically. Therefore, installing it is highly recommended.

7. Testing:

   Run the following command if you want to test code with your active Python version:

.. code-block:: bash

   poetry run pytest


Using ``tox`` you can test code with multiple Python versions:

.. code-block:: bash

   poetry run tox


Currently supported versions: 3.10, 3.11, 3.12.
Note: you will need to have these Python versions installed on your system.

After ``tox`` testing, you can also view code coverage by tests.

That's it for now! ᕦ(ò_óˇ)ᕤ
