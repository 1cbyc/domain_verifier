import unittest
from domain_verifier.verifier import DomainVerifier

class TestDomainVerifier(unittest.TestCase):

    def test_valid_domain(self):
        verifier = DomainVerifier('example.com')
        self.assertTrue(verifier.is_valid())

    def test_invalid_domain(self):
        verifier = DomainVerifier('invalid_domain')
        self.assertFalse(verifier.is_valid())

    # You can add tests for reachability here if desired
    # Note: Reachability tests may require internet access and may be unreliable in tests

if __name__ == '__main__':
    unittest.main()
