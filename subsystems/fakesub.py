from commands2 import Command
from commands2 import Subsystem


class ExampleSubsystem(Subsystem):

    def __init__(self):
        """Creates a new ExampleSubsystem."""
        super().__init__()


    def exampleMethodCommand()->Command:
        """
        Example command factory method.

         :return a command
        """

        return self.runOnce(lambda: True)# one-time action goes here # )

    def exampleCondition(self)->bool:
        """
        An example method querying a boolean state of the subsystem (for example, a digital sensor).

        :return value of some boolean subsystem state, such as a digital sensor.
        """

        #Query some boolean state, such as a digital sensor.
        return False

    def periodic(self):
        # This method will be called once per scheduler run
        pass

    def simulationPeriodic(self):
        # This method will be called once per scheduler run during simulation
        pass