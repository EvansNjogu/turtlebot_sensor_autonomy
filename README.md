# TurtleBot Sensor Autonomy Task

## Description
This task implements a solution for a TurtleBot sensor system that interprets encoded signals from the environment. The sensor provides three types of outputs:
- **Negative number** – The robot performs a 120-degree right turn.
- **Positive odd number** – The robot moves 2 units forward.
- **Positive even number** – The robot moves 1 unit forward.

The solution leverages ROS (Robot Operating System) and TurtleSim to simulate the robot's movement based on the sensor readings.

---

## Task Story
A sensor was received with little documentation regarding its behavior. Through reverse engineering and experimentation, the following insights were gathered:
- **Negative values** prompt the robot to turn right by 120 degrees.
- **Positive odd values** signal the robot to advance by 2 units.
- **Positive even values** indicate a forward movement of 1 unit.

---

## Subtasks
The project is structured to address the following tasks:
1. **Install the sensor package** – Unzip and install the provided `midterm_sensor_1` package.
2. **Message Investigation** – Analyze the topics & message types to understand how sensor data is transmitted.
3. **Package Creation** – Develop a ROS package named after the provided Neptune code.
4. **Sensor Subscription** – Create a ROS node that subscribes to sensor data.
5. **TurtleSim Commanding** – Modify the node to send movement commands to TurtleSim based on sensor input.

---

## Usage
1. Launch the TurtleSim:
   ```bash
   rosrun turtlesim turtlesim_node
   ```
2. Run the sensor node:
   ```bash
   rosrun your_package sensor_node
   ```
3. Watch the TurtleBot respond to sensor input by turning or moving forward based on the sensor's output.

---

## Outcome
Upon completion, the robot autonomously responds to sensor data in real-time as shown below:

![Turtle PrintScreen1](https://njoguevans.me/TurtlePrintscreen1.png)
![Turtle PrintScreen2](https://njoguevans.me/TurtlePrintscreen2.png)

---

## Future Improvements
- Incorporate obstacle avoidance based on sensor feedback.
- Implement a visualization tool to display sensor readings.
- Extend the solution to support multiple sensor inputs.

---

## License 

This project is licensed under the MIT License – feel free to modify and use it for your personal projects.

## Contact

For any questions or collaboration opportunities, feel free to reach out at [hey@njoguevans.me](mailto:hey@njoguevans.me).
