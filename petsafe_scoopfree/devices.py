import json

def get_pets(client):
    """
    Sends a request to PetSafe's API for all pets associated with account.

    :param client: PetSafeClient with authorization tokens
    :return: list of pets

    """
    response = client.api_get("/pets/pets")
    data = response.json()
    response.raise_for_status()
    return [DeviceScoopfree(client, pet_data) for pet_data in data["data"]]    

def get_scoopers(client):
    """
    Sends a request to PetSafe's API for all scoopers associated with account.

    :param client: PetSafeClient with authorization tokens
    :return: list of scoopers

    """
    response = client.api_get("/scoopfree/product/product")
    data = response.json()
    response.raise_for_status()
    return [DeviceScoopfree(client, feeder_data) for feeder_data in data["data"]]

def get_activity(client, device):
    """
    Sends a request to PetSafe's API for all activities associated with account.

    :param client: PetSafeClient with authorization tokens
    :return: list of activities

    """
    response = client.api_get("/scoopfree/product/product/{device}/activity".format(device=device))
    data = response.json()
    response.raise_for_status()
    return [DeviceScoopfree(client, activity_data) for activity_data in data["data"]]

class DeviceScoopfree:
    def __init__(self, client, data):
        """
        PetSafe Scoopfree device.

        :param client: PetSafeClient with authorization tokens
        :param data: data regarding feeder
        """
        self.client = client
        self.data = data

    def __str__(self):
        return self.to_json()

    def to_json(self):
        """
        All scooper data formatted as JSON.

        """
        return json.dumps(self.data, indent=2)

    def update_data(self):
        """
        Updates self.data to the scooper's current online state.

        """
        response = self.client.api_get(self.api_path)
        response.raise_for_status()
        self.data = json.loads(response.content.decode("UTF-8"))

    def rake_now(self, update_data=True):
        """
        Triggers the rake to begin raking.

        :param amount: the amount to feed in 1/8 increments.
        :param slow_feed: if True, will use slow feeding. If None, defaults to current settings.
        :param update_data: if True, will update the feeder's data after feeding. Defaults to True.

        """
        response = self.client.api_post(
            "/scoopfree/product/product/"+ self.api_name + "/rake-now", data={}
        )
        response.raise_for_status()

        if update_data:
            self.update_data()
            return self.data["data"]

    def reset(self, amount=0, update_data=True):
        """
        Triggers the rake to begin raking.

        :param amount: the amount to feed in 1/8 increments.
        :param slow_feed: if True, will use slow feeding. If None, defaults to current settings.
        :param update_data: if True, will update the feeder's data after feeding. Defaults to True.

        """
        response = self.client.api_patch(
            "/scoopfree/product/product/"+ self.api_name + "/shadow",
            data={"rakeCount": amount},
        )
        response.raise_for_status()

        if update_data:
            self.update_data()
            return self.data["data"]

    def modify_timer(self, amount=20, update_data=True):
        """
        Modifies the specified schedule.

        :param time: the time to dispense the food in 24 hour notation with colon separation (e.g. 16:35 for 4:35PM)
        :param amount: the amount to feed in 1/8 increments.
        :param schedule_id: the id of the scheduled feed to delete (six digits as of writing)
        :param update_data: if True, will update the feeder's data after feeding. Defaults to True.

        """
        response = self.client.api_patch(
            "/scoopfree/product/product/"+ self.api_name + "/shadow",
            data={"rakeDelayTime": amount},
        )
        response.raise_for_status()

        if update_data:
            self.update_data()
            return self.data["data"]

    @property
    def api_name(self):
        """The feeder's thing_name from the API."""
        return self.data["thingName"]

    @property
    def api_path(self):
        """The feeder's path on the API."""
        return "/scoopfree/product/product/" + self.api_name + "/"

    @property
    def id(self):
        """The feeder's ID."""
        return self.data["id"]

    @property
    def friendly_name(self):
        """The feeder's display name."""
        return self.data["settings"]["friendly_name"]

    @friendly_name.setter
    def friendly_name(self, value):
        self.put_setting("friendly_name", value)

