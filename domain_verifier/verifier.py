import requests
import validators

class DomainVerifier:
    def __init__(self, domain):
        self.domain = domain

    def is_valid(self):
        """Check if the domain is valid."""
        return validators.domain(self.domain)

    def is_reachable(self):
        """Check if the domain is reachable."""
        try:
            response = requests.get(f'http://{self.domain}', timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False
