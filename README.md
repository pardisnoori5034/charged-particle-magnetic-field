# Simulation of a Charged Particle in a Magnetic Field

This project simulates the trajectory of a charged particle moving through a **uniform magnetic field** using Python.

## How it works
The simulation uses the **Lorentz Force** equation:

$$ \vec{F} = q (\vec{v} \times \vec{B}) $$

When a particle has a velocity component perpendicular to the magnetic field, it moves in a circle. If it also has a component parallel to the field, the resulting path is a **helix (spiral)**.

## Requirements
To run this simulation, you need:
* Python 3.x
* NumPy
* Matplotlib

## How to Run
1. Clone this repository.
2. Install dependencies: `pip install numpy matplotlib`
3. Run the script: `python simulation.py`

## Preview
The code generates a 3D plot showing the helical path of the particle.

