import unittest
from src.demographic_data_analyzer import calculate_demographic_data

class TestDemographicAnalyzer(unittest.TestCase):
    def setUp(self):
        self.result = calculate_demographic_data(print_data=False)

    def test_race_count(self):
        self.assertIn('White', self.result['race_count'])
        self.assertIn('Black', self.result['race_count'])

    def test_average_age_men(self):
        self.assertIsInstance(self.result['average_age_men'], float)

    def test_percentage_bachelors(self):
        self.assertIsInstance(self.result['percentage_bachelors'], float)

    def test_higher_education_rich(self):
        self.assertIsInstance(self.result['higher_education_rich'], float)

    def test_lower_education_rich(self):
        self.assertIsInstance(self.result['lower_education_rich'], float)

    def test_min_work_hours(self):
        self.assertIsInstance(self.result['min_work_hours'], int)

    def test_rich_percentage(self):
        self.assertIsInstance(self.result['rich_percentage'], float)

    def test_highest_earning_country(self):
        self.assertIsInstance(self.result['highest_earning_country'], str)

    def test_top_IN_occupation(self):
        self.assertIsInstance(self.result['top_IN_occupation'], str)


if __name__ == "__main__":
    unittest.main()
