class AbstractEvent:
    def __init__(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data