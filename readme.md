# Raspberry Pico Line Following Car

This project demonstrates how to build a car that can follow a line using the Raspberry Pi Pico, L9110 motor driver, and IR sensors.

## Components

- Raspberry Pi Pico
- L9110 Motor Driver Module
- 2 IR Sensors
- 4 DC Motors
- Chassis for the car
- Jumper wires
- Power supply

## Wiring Diagram

| Raspberry Pi Pico | L9110 Motor Driver | IR Sensors |
|-------------------|--------------------|------------|
| GP5               | A_IA               |            |
| GP4               | A_IB               |            |
| GP3               | B_IA               |            |
| GP2               | B_IB               |            |
| GP0               |                    | IR_LEFT    |
| GP1               |                    | IR_RIGHT   |

## How to Run

1. Connect the components as per the wiring diagram.
2. Copy the provided code into a new file on your Raspberry Pi Pico.
3. Run the code on the Raspberry Pi Pico.
4. Place the car on a track with a black line and watch it follow the line.

## Troubleshooting

- Ensure all connections are secure.
- Verify the IR sensors are working correctly by checking their output values.
- Adjust the speed values if the car is not responding as expected.

## License

This project is licensed under the MIT License.

---

# Raspberry Pico Obstacle Avoidance Car

This project demonstrates how to build a car that can avoid obstacles using the Raspberry Pi Pico, L9110 motor driver, and an ultrasonic sensor.

## Components

- Raspberry Pi Pico
- L9110 Motor Driver Module
- 1 Ultrasonic Sensor (HC-SR04)
- 4 DC Motors
- Chassis for the car
- Jumper wires
- Power supply

## Wiring Diagram

| Raspberry Pi Pico | L9110 Motor Driver | Ultrasonic Sensor |
|-------------------|--------------------|-------------------|
| GP5               | A_IA               |                   |
| GP4               | A_IB               |                   |
| GP3               | B_IA               |                   |
| GP2               | B_IB               |                   |
| GP2               |                    | TRIG              |
| GP3               |                    | ECHO              |

## How to Run

1. Connect the components as per the wiring diagram.
2. Copy the provided code into a new file on your Raspberry Pi Pico.
3. Run the code on the Raspberry Pi Pico.
4. Place the car in an environment with obstacles and watch it avoid them.

## Troubleshooting

- Ensure all connections are secure.
- Verify the ultrasonic sensor is working correctly by checking its output values.
- Adjust the speed values if the car is not responding as expected.

## License

This project is licensed under the MIT License.