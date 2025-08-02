# test_metaapex.py
"""
Tests for MetaApex module.
"""

import unittest
from metaapex import MetaApex

class TestMetaApex(unittest.TestCase):
    """Test cases for MetaApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaApex()
        self.assertIsInstance(instance, MetaApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
