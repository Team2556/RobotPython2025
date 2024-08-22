# RobotPython2024
 Fresh start ; created for the 2025 season; transition to python


 # FRC Robot Project

This repository contains the code for our FRC robot using Python, PyRobot, and WPILib.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-team/FRC-Robot-Project.git
   cd FRC-Robot-Project
2. Create a vertual environment (from a terminal; in the repo directry on your pc)
    ```sh
    python -m venv venv
3. Activate the virtual environment:
    ```sh
    On Windows: 
    venv\Scripts\activate
    On macOS/Linux: 
    source venv/bin/activate
4. Install the dependencies:
    ```sh
    pip install . #the dot references your current directory

5. initialize robotpy
    ```sh
    py -3 -m robotpy init

6. Create folders named 'src/subsytems' and 'tests'
    ```sh
    mkdir src/subsytems
    mkdir tests

7. move robot.py file created by initilization to 'src' folder
    move robot2.py src\

8. Run the robot code:
    ```sh
    python src/robot.py

# Repository Structure
- We plan to use the following structure.
    ```sh
    FRC-Robot-Project/
    ├── src/
    │   ├── ?maybe? __init__.py
    │   ├── robot.py
    │   └── subsystems/
    │       ├── ?maybe? __init__.py
    │       └── example_subsystem.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_robot.py
    ├── ?maybe? config/
    │   └── config.yaml
    ├── .gitignore
    ├── README.md
    ├── pyproject.toml
    └── venv/

# Other resources
- Download python (3.12.5): https://www.python.org/downloads/windows/
- Python tutorial: https://docs.python.org/3.12/tutorial/index.html
- More instructions from WPI: https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/python-setup.html

# VS Code Extensions
TODO: Refer to our main github readme or sync here....
In the VS Code Extensions sidbar, these codes should help you find usefull extensions (well.. Git and Python are required)
- github.vscode-pull-request-github
- ms-python.python
- github.copilot
- github.copilot-chat
- tamasfe.even-better-toml
- ms-python.black-formatter
- njpwerner.autodocstring
- 