# UniBikes
Inspired by [traintrackr](https://www.traintrackr.io/) I wanted to create something similar for visualizing bikesharing bikes as my first ever PCB design.

![An image of the finished PCB](https://raw.githubusercontent.com/strifel/UniBikes/refs/heads/main/unibikes.jpg)

Unibikes shows the 10 bike sharing locations at TU Dortmund University in germany with an RGB LED each.
Each LED can therefore represent if there are none, some or a few bikes at that station.

## Data
The micropython code directly receives the rgb values for each LED from a backend.

## Components
| Component name | Component        |
| -------------- | ---------------- |
| D1 to D10      | WS2812B LED      |
| J0             | USB C Receptable |
| J1 and J2      | 4 Pin header     |
| J3             | 2 Pin header     |
| U1             | ESP32 C3         |
| U2             | TLV1117 3.3V     |
| SW1 to SW3     | Push button      |
| R1             | 1k Resistor      |
| R2 to R4       | 10k Resistor     |
| R5 and R6      | 5.1k Resistor    |
| C1 and C4      | 10uF Capacitor   |
| C2             | 1 uF Capacitor   |
| C3             | 100nF Capacitor  |
