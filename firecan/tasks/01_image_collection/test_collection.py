import unittest
import image_collection


class TestDateIterator(unittest.TestCase):
    def test_prior_day(self):
        test_case = "20230602"
        expected = "20230601"
        got = image_collection.date_iterator(test_case)
        self.assertEqual(got, expected)

    def test_prior_month(self):
        test_case = "20230601"
        expected = "20230531"
        got = image_collection.date_iterator(test_case)
        self.assertEqual(got, expected)

    def test_prior_year(self):
        test_case = "20230101"
        expected = "20221231"
        got = image_collection.date_iterator(test_case)
        self.assertEqual(got, expected)
    
    def test_leap_year(self):
        test_case = "20200301"
        expected = "20200229"
        got = image_collection.date_iterator(test_case)
        self.assertEqual(got, expected)


class TestImageRequest(unittest.TestCase):
    def test_response_ft(self):
        test_img_type, test_date_str = "ft", "20230606"
        response = image_collection.request_image_page(img_type=test_img_type, 
                                                  date_str=test_date_str)
        self.assertTrue(response is not None)

    def test_response_hfi(self):
        test_img_type, test_date_str = "hfi", "20230606"
        response = image_collection.request_image_page(img_type=test_img_type, 
                                                  date_str=test_date_str)
        self.assertTrue(response is not None)

class TestImageScrape(unittest.TestCase):
    def test_image_scrape(self):
        test_img_type, test_date_str = "ft", "20230607"
        final = image_collection.scrape_images(n=10,
                                               img_type=test_img_type, 
                                               date_str=test_date_str)
        self.assertEqual(final, 0)

    

if __name__ == '__main__':
    unittest.main()