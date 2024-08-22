# RobotPython2024
 Fresh start ; created for the 2025 season; transition to python


 # FRC Robot Project

This repository contains the code for our FRC robot using Python, PyRobot, and WPILib.

## Setup

1. Make sure you have Python 3.12.5
    ```sh
    python --version
    ------------------------ 
    OUTPUT: Python 3.12.5
1a. If not go to [Other Resources] and download it.

2. Clone the repository:
   ```sh
   git clone https://github.com/Team2556/RobotPython2025.git
   cd RobotPython2025
<!-- 3. Activate the virtual environment:
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
    py -3 -m robotpy init -->

<!-- 6. Create folders named 'src/subsytems' and 'tests'
    ```sh
    mkdir src/subsytems
    mkdir tests

7. move robot.py file created by initilization to 'src' folder
    move robot2.py src\ -->

3. Run the robot code:
    ```sh
    python src/robot.py

# Repository Structure
- We plan to use the following structure.
    <!-- ├── src/
    │   ├── ?maybe? __init__.py
    │   ├── robot.py
    │   └── subsystems/
    │       ├── ?maybe? __init__.py
    │       └── example_subsystem.py 
    ├── ?maybe? config/
    │   └── config.yaml
    -->
    ```sh
    FRC-Robot-Project/
    ├── tests/
    │   ├── __init__.py
    │   └── test_robot.py
    ├── .gitignore
    ├── README.md
    ├── pyproject.toml
    ├── robot.py
    └── venv/

# Other Resources
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

## ORIGINAL Setup (FYI)

1. Clone the repository:
   ```sh
   git clone https://github.com/Team2556/RobotPython2025.git
   cd RobotPython2025
2. Create a vertual environment (from a terminal; in the repo directry on your pc)
    ```sh
    python -m venv venv
3. Activate the virtual environment:
    ```sh
    On Windows: 
    venv\Scripts\activate
    On macOS/Linux: 
    source venv/bin/activate
<!-- 4. Install the dependencies:
    ```sh
    pip install . #the dot references your current directory -->

5. initialize robotpy
    ```sh
    py -m robotpy init

<!-- 6. Create folders named 'src/subsytems' and 'tests'
    ```sh
    mkdir src/subsytems
    mkdir tests

7. move robot.py file created by initilization to 'src' folder
    move robot2.py src\ -->

6. Run the robotpy sync to get the RoboRIO python
    ```sh 
    py -m robotpy sync
8. Run the robot code:
    ```sh
    python src/robot.py