from functions.get_files_info import get_files_info 
import unittest

class Test_get_file_info(unittest.TestCase):
    def test_current_dir(self):
        result = get_files_info("calculator", ".")
        self.assertIsNotNone(result)
        print(result)
    
    def test_valid_dir(self):
        result =  get_files_info("calculator", "pkg")
        self.assertIsNotNone(result) 
        print(result)

    def test_invalid_dir(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result,
                        'Error: Cannot list "/bin" as it is outside the permitted working directory')
        print(result)
        
    
    def test_invalid_path(self):
        result = get_files_info("calculator", "../")
        self.assertEqual(result,
                        'Error: Cannot list "../" as it is outside the permitted working directory')
        print(result)
    

if __name__ == "__main__":
    unittest.main()
