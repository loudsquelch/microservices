
class Instance(object):

    sample_data = {}
    sample_data["i-3e43qa"] = {
        "owner": "operations",
        "id": "i-3e43qa"
    }
    sample_data["i-abc123"] = {
        "owner": "alphanumeric",
        "id": "i-abc123"
    }

    def __init__(self, instance_id):
        self.scope = Instance.sample_data[instance_id]["owner"]
        self.id = instance_id
