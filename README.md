**Tennis Ball Line Calling System** <br>
The Tennis Ball Line Calling System is a computer vision-based project that utilizes two Motorola G4 Play cell phone cameras and the OpenCV library to detect tennis balls on a court and accurately determine whether they are in or out of bounds. 

**Features**
- Real-time Ball Detection: The system utilizes the live video feed from the two Moto G4 Play cell phone cameras positioned on the corner of the tennis court. The frames from these cameras are processed in real-time using OpenCV, allowing for quick and accurate ball detection.
- 2+ Camera Support: By employing two cameras, the system is able to ensure that the object being detected is actually the ball. In the future, more cameras can be easily added to increase the coverage and accuracy of the system.
- Automatic Line Judgment: The system the coordinates of the ball and compares it against the manual calibration performed to determine if the ball is in or out. 

**Installation** <br>
To set up the Tennis Ball Line Calling System, follow these steps:

1. Clone the Repository: Start by cloning this GitHub repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/your-username/Tennis_Ball_Line_Validator.git

2. Download Iriun webcam and ensure that your devices are able to communicate with the program. 

3. Configure Camera Setup: Place two cell phones at suitable positions around the tennis court, ensuring a clear view of the playing area. Connect both phones to your computer via USB connection. However, it is important to note that a wireless connection is possible as well. 

4. Calibrate the System: Before running the system, it is crucial to calibrate it for accurate ball detection. Place a ball at the edge of the line and repeat this process to find the coordinates that are out of bounds.

5. Once this is complete, go ahead and run the project and see how the program is able to identify and tag a tennis ball moving on the court.
