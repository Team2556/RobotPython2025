# RobotPython2024
 Fresh start ; created for the 2024 season; transition to python


 # FRC Robot Project

This repository contains the code for our FRC robot using Python, PyRobot, and WPILib.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-team/FRC-Robot-Project.git
   cd FRC-Robot-Project
2. Create a vertual environment
    python -m venv venv
3. Activate the virtual environment:
    On Windows: venv\Scripts\activate
    On macOS/Linux: source venv/bin/activate
4. Install the dependencies:
    pip install . #the dot references your current directory
5. Run the robot code:
    python src/robot.py

# Repository Structure
We plan to use the following structure.
FRC-Robot-Project/
├── src/
│   ├── __init__.py
│   ├── robot.py
│   └── subsystems/
│       ├── __init__.py
│       └── example_subsystem.py
├── tests/
│   ├── __init__.py
│   └── test_robot.py
├── config/
│   └── config.yaml
├── .gitignore
├── README.md
├── pyproject.toml
└── venv/


# Other resources
Download python: https://www.python.org/downloads/windows/
More instructions from WPI: https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/python-setup.html

