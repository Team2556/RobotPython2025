from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

# this is one of your components
from subsystems.drivetrain import DriveTrain


class DriveForward(AutonomousStateMachine):

    MODE_NAME = "Drive Forward"
    DEFAULT = True

    # Injected from the definition in robot.py
    drivetrain: DriveTrain
    wpilib.SmartDashboard.putData("Drive Forward", self)

    @timed_state(duration=3, first=True)
    def drive_forward(self):
        self.drivetrain.drive() (-0.7, 0)

    '''def on_enable(self):
        super().on_enable()
        wpilib.SmartDashboard.putData("Drive Forward", self)

    def on_disable(self):
        super().on_disable()
        wpilib.SmartDashboard.remove("Drive Forward")'''