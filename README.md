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

you need to have these installed:
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
cd domain_verifier
```


you can run the domain verifier from the command line using the command you defined in the cli.py file. if you installed it in editable mode, you should be able to run it directly using the command you set up.

```bash
python -m domain_verifier.cli example.com invalid_domain
```

make sure to replace example.com and invalid_domain with the domains you want to verify.

you should get something liek this in console:

When you run the command, you should see output like this:

```plaintext
    Checking example.com...
    example.com is a valid domain.
    example.com is reachable.
    Checking invalid_domain...
    invalid_domain is not a valid domain.
```

### you can run tests too:

```bash
python -m unittest discover
```

### you can as well use the Console Script

If you set up the console script in `setup.py`, you can run the command without explicitly invoking Python. After installing the package with `pip install -e .`, you can use:

```bash
domain-verifier example.com invalid_domain
```

This will provide the same functionality as using `python -m domain_verifier.cli.`