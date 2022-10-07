from src.components.objective.objective import Objective


class TestObjective:

    def test_addition(self):
        o = Objective("phrase")
        assert o.name == "phrase"
