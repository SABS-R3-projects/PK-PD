import unittest

import myokit
import numpy as np

from PKPD.model import model as m



class TestSingleOutputModel(unittest.TestCase):
    """Tests the functionality of all methods of the SingleOutputModel class.
    """
    # Test case I: 1-compartment model
    file_name = 'PKPD/modelRepository/1comp_concentration_bolus_linear.mmt'
    one_comp_model = m.SingleOutputModel(file_name)

    def test_init(self):
        """Tests whether the Model class initialises as expected.
        """
        # Test case I: 1-compartment model
        ## expected:
        state_names = ['centralCompartment.drug']
        output_name = 'centralCompartment.drugConcentration'
        parameter_names = ['centralCompartment.CL', 'centralCompartment.V']
        number_parameters_to_fit = 3

        ## assert initilised values coincide
        assert state_names == self.one_comp_model.state_names
        assert output_name == self.one_comp_model.output_name
        for parameter_id, parameter in enumerate(self.one_comp_model.parameter_names):
            assert parameter_names[parameter_id] == parameter
        assert number_parameters_to_fit == self.one_comp_model.number_parameters_to_fit

    def test_n_parameters(self):
        """Tests whether the n_parameter method returns the correct number of fit parameters.
        """
        # Test case I: 1-compartment model
        ## expected
        n_parameters = 3

        ## assert correct number of parameters is returned.
        assert n_parameters == self.one_comp_model.n_parameters()

    def test_n_outputs(self):
        """Tests whether the n_outputs method returns the correct number of outputs.
        """
        # Test case I: 1-compartment model
        ## expected
        n_outputs = 1

        ## assert correct number of outputs.
        assert n_outputs == self.one_comp_model.n_outputs()

    def test_simulate(self):
        """Tests whether the simulate method works as expected. Tests implicitly also whether
        the _set_parameters method works properly.
        """
        # Test case I: 1-compartment model
        parameters = [0, 2, 4] # different from initialsed parameters
        times = np.arange(25)

        ## expected
        model, protocol, _ = myokit.load(self.file_name)
        model.set_state([parameters[0]])
        model.set_value('centralCompartment.CL', parameters[1])
        model.set_value('centralCompartment.V', parameters[2])
        simulation = myokit.Simulation(model, protocol)
        myokit_result = simulation.run(duration=times[-1]+1, log=['centralCompartment.drugConcentration'], log_times = times)
        expected_result = myokit_result.get('centralCompartment.drugConcentration')

        ## assert that Model.simulate returns the same result.
        model_result = self.one_comp_model.simulate(parameters, times)

        assert np.array_equal(expected_result, model_result)


class TestMultiOutputModel(unittest.TestCase):
    """Tests the functionality of all methods of the MultiOutputModel class.
    """
    # Test case I: 1-compartment model
    file_name = 'PKPD/mmt/one_compartment.mmt'
    one_comp_model = m.MultiOutputModel(file_name)

    def test_init(self):
        """Tests whether the Model class initialises as expected.
        """
        # Test case I: 1-compartment model
        ## expected:
        state_names = ['bolus.y_c']
        parameter_names = ['param.CL', 'param.V_c']
        number_model_parameters = 2
        number_parameters_to_fit = 3

        ## assert initilised values coincide
        assert state_names == self.one_comp_model.state_names
        for parameter_id, parameter in enumerate(self.one_comp_model.parameter_names):
            assert parameter_names[parameter_id] == parameter
        assert number_model_parameters == self.one_comp_model.number_model_parameters
        assert number_parameters_to_fit == self.one_comp_model.number_parameters_to_fit

    def test_n_parameters(self):
        """Tests whether the n_parameter method returns the correct number of fit parameters.
        """
        # Test case I: 1-compartment model
        ## expected
        n_parameters = 3

        ## assert correct number of parameters is returned.
        assert n_parameters == self.one_comp_model.n_parameters()

    def test_n_outputs(self):
        """Tests whether the n_outputs method returns the correct number of outputs.
        """
        # Test case I: 1-compartment model
        ## expected
        n_outputs = 1

        ## assert correct number of outputs.
        assert n_outputs == self.one_comp_model.n_outputs()

    def test_simulate(self):
        """Tests whether the simulate method works as expected. Tests implicitly also whether
        the _set_parameters method works properly.
        """
        # Test case I: 1-compartment model
        parameters = [20, 2, 4] # different from initialsed parameters
        times = np.arange(25)

        ## expected
        model, protocol, _ = myokit.load(self.file_name)
        model.set_state([parameters[0]])
        model.set_value('param.CL', parameters[1])
        model.set_value('param.V_c', parameters[2])
        simulation = myokit.Simulation(model, protocol)
        myokit_result = simulation.run(duration=times[-1]+1, log=['bolus.y_c'], log_times = times)
        expected_result = myokit_result.get('bolus.y_c')
        np_expected_result = np.array(expected_result)[:, np.newaxis] # in MultiOutputModel results are stored in 2d array.

        ## assert that Model.simulate returns the same result.
        model_result = self.one_comp_model.simulate(parameters, times)
   
        assert np.allclose(np_expected_result, model_result)