# domain verifier


how i run the command in the file is 
```bash
python -m domain_verifier.cli nsisong.com nsisonglabs.com ...
```


## for running tests

i simply did:

```bash
python -m unittest discover
```

```arduino


### Step 7: Create `setup.py`

**`setup.py`**: This file will help to package your project.

```python
# setup.py

from setuptools import setup, find_packages

setup(
    name='domain_verifier',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'validators',
    ],
    entry_points={
        'console_scripts': [
            'domain-verifier=domain_verifier.cli:main',
        ],
    },
)
```


### then, once it is all set, i have to run the project:

first, install the package:
```bash
pip install -e .
```

then, verify the domain:
```bash
domain-verifier nsisong.com invalid_domain
```


# this is how to use my tool

this guide provides instructions on how to set up and use the CLI Domain Verifier you built. you need to have these installed:
- Python 3.6 or higher
- pip

## then setup your env
   - **On macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   - **On Windows**:
     ```bash
     venv\Scripts\activate
     ```

## then go to the project dir

```bash
cd /path/to/your/domain_verifier
```
