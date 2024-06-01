
Creating documentation using Sphinx
====================================

To modify the content of the documentation, you have to change ``.rst`` files or add new ones in ``docs/source`` folder.

Some rst syntax hints can be found here:

* `A ReStructuredText Primer <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`_
* `reStructuredText Markup Specification <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_


Building documentation
-----------------------

To build a documentation, follow steps:

.. code-block:: bash

   cd docs/source
   make html

Html files are stored in ``docs/build/html``. To check your build, simply open ``index.html`` in your browser.


Generate documentation from docstrings
--------------------------------------

To generate documentation from docstrings:

.. code-block:: bash

   sphinx-apidoc -o docs/source ./markupit

Sphinx will generate ``.rst`` file for every module in our project.
