import unittest
from PKPD.models import model_class
import matplotlib.pyplot as plt

class TestVariables(unittest.TestCase):

    file_name = 'PKPD/mmt/one_compartment.mmt'
    temp_model = model_class.Model(file_name)

    def test_get(self):
        p1 = self.temp_model.get_variable('param.CL')
        self.assertEqual(p1, 3)

    def test_set(self):
        self.temp_model.set_variable('param.CL', 4)
        p1 = self.temp_model.get_variable('param.CL')
        self.assertEqual(p1, 4)

    def test_simulation(self):
        self.temp_model.update_simulation()
        self.temp_model.run_simulation(48)
        plt.plot(self.temp_model.sim_results['engine.time'], self.temp_model.sim_results['bolus.y_c'])
        plt.show()



