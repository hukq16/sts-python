class AbstractStance:
    def __init__(self, stance_name, stance_type, stance_description, stance_cost, stance_duration):
        self.stance_name = stance_name
        self.stance_type = stance_type
        self.stance_description = stance_description
        self.stance_cost = stance_cost
        self.stance_duration = stance_duration

    def get_stance_name(self):
        return self.stance_name

    def get_stance_type(self):
        return self.stance_type

    def get_stance_description(self):
        return self.stance_description

    def get_stance_cost(self):
        return self.stance_cost

    def get_stance_duration(self):
        return self.stance_duration

    def set_stance_name(self, stance_name):
        self.stance_name = stance_name

    def set_stance_type(self, stance_type):
        self.stance_type = stance_type

    def set_stance_description(self, stance_description):
        self.stance_description = stance_description

    def set_stance_cost(self, stance_cost):
        self.stance_cost = stance_cost

    def set_stance_duration(self, stance_duration):
        self.stance_duration = stance_duration

    def __str__(self):
        return self.stance_name + " " + self.stance_type + " " + self.stance_description + " " + str(self.stance_cost) + " " + str(self.stance_duration)