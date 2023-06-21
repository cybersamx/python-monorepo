# Fancy

This library should be independent and completely sandboxed from other modules and projects in the monorepo.

This library depends on libs/base.

## Setup

1. Create virtual environment.

   ```shell
   $ deactivate
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   (.venv) $
   ```
   
1. Install pip and tools.

   ```shell
   $ pip install -r $(git rev-parse --show-toplevel)/pip-requirements.txt
   $ pip install -r $(git rev-parse --show-toplevel)/dev-requirements.txt
   $ pip install -r requirements.txt
   ```
   
## Credits

This project is based on the work of Tweag, copyright Clément Hurlin licensed under MIT license.

* [Tweag: Python Monorepo](https://www.tweag.io/blog/2023-04-04-python-monorepo-1/)
* [Github: tweag/python-monorepo-example](https://github.com/tweag/python-monorepo-example)
