# domain_verifier/cli.py

import argparse
from .verifier import DomainVerifier

def main():
    parser = argparse.ArgumentParser(description='Verify domains.')
    parser.add_argument('domains', nargs='+', help='List of domains to verify')
    args = parser.parse_args()

    for domain in args.domains:
        verifier = DomainVerifier(domain)
        print(f"Checking {domain}...")
        if verifier.is_valid():
            print(f"{domain} is a valid domain.")
            if verifier.is_reachable():
                print(f"{domain} is reachable.")
            else:
                print(f"{domain} is not reachable.")
        else:
            print(f"{domain} is not a valid domain.")

if __name__ == "__main__":
    main()
