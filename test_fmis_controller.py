import sys
import unittest

sys.path.append('/Users/pbenson/Documents/')
print(sys.path)

import ducktape
from ducktape import fmis_controller_class

# Testing approach: 
## Test all methods of FMIS_controller
## Need to define an FMIS_interface class.
## Used for testing basic I/O, object creation
## Edge cases:
### non-string inputs
### non-browser inputs
### Query permissions something other than PUBLIC or PRIVATE
### Invalid Query Name
### Multiple queries – both the list and independent

# Test basic object creation
class TestBasicOperations(unittest.TestCase):
    # Create instance

    # Create instance using existing display

    # Create invalid instances (with wrong types)
    pass

    # Test get_browser_elements and process_base_url