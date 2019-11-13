import unittest
from PKPD.models import model_class

class TestVariables(unittest.TestCase):

    file_name = 'one_compartment.mmt'
    temp_model = model_class.Model(file_name)

    def test_get(self):
        p1 = self.temp_model.get_variable('param.CL')
        self.assertEqual(p1, 3)

    def test_set(self):
        self.temp_model.set_variable('param.CL', 4)
        p1 = self.temp_model.get_variable('param.CL')
        self.assertEqual(p1, 4)
