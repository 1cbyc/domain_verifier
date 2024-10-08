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