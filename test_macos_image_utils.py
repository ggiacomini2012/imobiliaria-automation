import unittest
import os
import tempfile
import shutil
from PIL import Image
import logging
from macos_image_utils import (
    copy_image_macos_reliable,
    prepare_image_for_macos,
    prepare_for_retina,
    verify_clipboard_image,
    cleanup_temporary_files,
    get_image_info
)

# Configure logging for tests
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestMacOSImageUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        # Create a temporary directory for test files
        cls.test_dir = tempfile.mkdtemp()
        logging.info(f"Created test directory: {cls.test_dir}")
        
        # Create test images
        cls.test_images = {}
        
        # Small PNG
        cls.test_images['small_png'] = os.path.join(cls.test_dir, 'small.png')
        img = Image.new('RGB', (100, 100), color='red')
        img.save(cls.test_images['small_png'], 'PNG')
        
        # Large PNG
        cls.test_images['large_png'] = os.path.join(cls.test_dir, 'large.png')
        img = Image.new('RGB', (3000, 3000), color='blue')
        img.save(cls.test_images['large_png'], 'PNG')
        
        # JPG
        cls.test_images['jpg'] = os.path.join(cls.test_dir, 'test.jpg')
        img = Image.new('RGB', (200, 200), color='green')
        img.save(cls.test_images['jpg'], 'JPEG')
        
        # Non-existent file
        cls.test_images['nonexistent'] = os.path.join(cls.test_dir, 'nonexistent.png')

    @classmethod
    def tearDownClass(cls):
        """Clean up test environment"""
        # Remove test directory and all contents
        shutil.rmtree(cls.test_dir)
        logging.info(f"Removed test directory: {cls.test_dir}")
        
        # Clean up any temporary files
        cleaned = cleanup_temporary_files()
        if cleaned > 0:
            logging.info(f"Cleaned up {cleaned} temporary files")

    def test_get_image_info(self):
        """Test image info retrieval"""
        info = get_image_info(self.test_images['small_png'])
        self.assertIsNotNone(info)
        self.assertEqual(info['format'], 'PNG')
        self.assertEqual(info['size'], (100, 100))
        
        # Test with non-existent file
        info = get_image_info(self.test_images['nonexistent'])
        self.assertIsNone(info)

    def test_prepare_image_for_macos(self):
        """Test image preparation"""
        # Test with small PNG (should return original)
        result = prepare_image_for_macos(self.test_images['small_png'])
        self.assertEqual(result, self.test_images['small_png'])
        
        # Test with large PNG (should create optimized version)
        result = prepare_image_for_macos(self.test_images['large_png'])
        self.assertNotEqual(result, self.test_images['large_png'])
        self.assertTrue(os.path.exists(result))
        
        # Test with JPG (should convert to PNG)
        result = prepare_image_for_macos(self.test_images['jpg'])
        self.assertNotEqual(result, self.test_images['jpg'])
        self.assertTrue(os.path.exists(result))
        self.assertTrue(result.endswith('.png'))

    def test_prepare_for_retina(self):
        """Test Retina display preparation"""
        # Test with small image
        result = prepare_for_retina(self.test_images['small_png'])
        if is_retina_display():
            self.assertNotEqual(result, self.test_images['small_png'])
            self.assertTrue(os.path.exists(result))
        else:
            self.assertEqual(result, self.test_images['small_png'])

    def test_copy_image_macos_reliable(self):
        """Test reliable image copying"""
        # Test with small PNG
        success = copy_image_macos_reliable(self.test_images['small_png'], cleanup=False)
        self.assertTrue(success)
        self.assertTrue(verify_clipboard_image())
        
        # Test with large PNG
        success = copy_image_macos_reliable(self.test_images['large_png'], cleanup=False)
        self.assertTrue(success)
        self.assertTrue(verify_clipboard_image())
        
        # Test with JPG
        success = copy_image_macos_reliable(self.test_images['jpg'], cleanup=False)
        self.assertTrue(success)
        self.assertTrue(verify_clipboard_image())
        
        # Test with non-existent file
        success = copy_image_macos_reliable(self.test_images['nonexistent'])
        self.assertFalse(success)

    def test_cleanup_temporary_files(self):
        """Test temporary file cleanup"""
        # Create some temporary files
        temp_files = []
        for i in range(3):
            path = os.path.join('/tmp', f'optimized_test_{i}.png')
            with open(path, 'w') as f:
                f.write('test')
            temp_files.append(path)
        
        # Clean up and verify
        cleaned = cleanup_temporary_files()
        self.assertGreaterEqual(cleaned, len(temp_files))
        
        # Verify files are gone
        for path in temp_files:
            self.assertFalse(os.path.exists(path))

if __name__ == '__main__':
    unittest.main() 