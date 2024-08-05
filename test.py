cimport unittest
from main import to_upper


class MytestCase(unittest.TestCase):
    def test_to_upper(self):
        name="siv"
        upper_name=to_upper(name)
        self.assertEqual(upper_name,'siv')
       
if __name__ == "__main__":
    unittest.main()