import myokit

class Model:
    def __init__(self, file_path):
        self.file_path = file_path
        self.model,  self.protocol, _ = myokit.load(self.file_path)
        self.vardict = {var.qname(): var.eval() for var in self.model.variables()}

    def set_variable(self, qname, value):
        self.model.set_value(qname, value)

    def get_variable(self, qname):
        return self.model.get(qname).eval()

    #def save_changes(self, file_name= self.file_path+'1'):  # so don't overwrite
     #   myokit.save(filename=file_name, model=self.model, protocol=self.protocol)

    def get_params(self):
        pass
