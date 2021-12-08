"""DidTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Did import Did

class DidTableSeeder(Seeder):
    def run(self):
        Did.create({"activity": "CodeWars Coding Challenge", "time": 75})
        Did.create({"activity": "FreeCode Academy JS course", "time": 120})
        Did.create({"activity": "LinkedIn & cover letters", "time": 45})
        Did.create({"activity": "In person meetup", "time": 150})
