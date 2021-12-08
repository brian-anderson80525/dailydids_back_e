"""CreateDidsTable Migration."""

from masoniteorm.migrations import Migration


class CreateDidsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("dids") as table:
            table.increments("id")
            table.string("activity")
            table.integer("time")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("dids")
