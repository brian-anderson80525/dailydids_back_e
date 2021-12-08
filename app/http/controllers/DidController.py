""" A DidController Module """

from masonite.controllers import Controller
from masonite.helpers import time
from masonite.request import Request
from app.Did import Did

class DidController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", DidController)
        """

        id = self.request.param("id")
        return Did.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", DidController)
        """

        return Did.all()

    def create(self):
        activity = self.request.input("activity")
        time = self.request.input("time")
        did = Did.create({"activity": activity, "time": time})
        return Did

    

    def update(self):
        activity = self.request.input("activity")
        time = self.request.input("time")
        id = self.request.param("id")
        Did.where("id", id).update({"activity": activity, "time": time})
        return Did.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        did = Did.where("id", id).get()
        Did.where("id", id).delete()
        return did