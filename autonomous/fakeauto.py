from magicbot import AutonomousStateMachine, timed_state, state
import wpilib

# this is one of your components
from components.drivetrain import DriveTrain


class DriveForward(AutonomousStateMachine):

    MODE_NAME = "Drive Forward"
    DEFAULT = True

    # Injected from the definition in robot.py
    drivetrain: DriveTrain

    @timed_state(duration=3, first=True)
    def drive_forward(self):
        self.drivetrain.move(-0.7, 0)