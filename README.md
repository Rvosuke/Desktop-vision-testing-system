# Vision Function Detection Software for Windows

This is a vision function detection software developed for the Windows platform. It provides an easy-to-use interface for users to test their visual acuity through a series of interactive tests. The software has been awarded a "Good Project Conclusion" at the university level for student innovation projects.

## Features

1. User-friendly application interface
2. Algorithm design for generating visual targets and corresponding detection mechanisms
3. Integration of computer camera for gesture recognition during tests

## Technologies and Dependencies

- Python 3.9
- PySide2 for GUI development
- NumPy for algorithm development

## Update Log

### 2022.11.7

- Temporarily set the equivalent focal length of the camera to 24mm.

### 11.11

- Implemented Hough Transform for card edge detection, successfully detecting the two long edges of the card. Planning to require users to hold the short edge during distance measurement.
- Successfully calculated the pixel width of the card.

### 11.13

- Successfully added a Windows application written with PySide2.

### 2023.3.1

- Successfully designed a vision test, but distance determination is not yet implemented.
- Bug: First test always fails.

### 3.2

- Gradually fixed the issue with the first test failing.
- Reduced the memory usage of the application.

### 3.3

- Successfully integrated the camera interface into the debugging interface.
- Implemented gesture recognition for covering one eye with one hand and pointing with the other.

### 3.4

- Added usage instructions.
- Fixed the refresh bug.

### 3.5

- New feature: Stretching out both hands simultaneously indicates the user cannot see clearly. However, related usage instructions have not been added yet.
- The current testing performance is good.

### 3.9

- Implemented a series of optimizations and tested the software. The standard deviation of test results is around 0.2, and the results are generally reliable.
- The project has now concluded.

Feel free to explore the repository and use the code in your own projects. If you have any questions or suggestions, please don't hesitate to reach out. Enjoy using the software!
