# Question 2.2
### Introduction
Team Interplanetar participates in remote competitions like ERC Remote Edition where we are given access to a remote computer using [TeamViewer](https://www.teamviewer.com/apac/). The organizers of ERC Remote have a computer set up that can be used to control physical robots (such as a rover or a robotic arm) using a GUI. The organizers then give access to the GUI to the participants for remotely conducting manual tasks (such as Navigation and maintenance) with physical robotic systems. The participants are given access to a GUI via TeamViewer, where the participants get a controller interface and live video feeds from cameras attached at different angles. The participant teams can manually drive the robot using the GUI from anywhere around the world, as long as there is a stable internet connection. 

This module is designed to simulate a similar scenario, where you will be given a Navigation task that you will have to complete on a remote computer using a GUI via TeamViewer. **Your task is to drive a Turtlebot in a simulated Gazebo environment and navigate to specific points using a given controller GUI. You have to use the video feed from the GUI to control the Turtlebot.**

### Prerequisites
Before you begin, make sure you have properly set up the following:

 - Have Ubuntu and ROS installed in VirtualBox on your Windows device (most of you are likely to have Ubuntu set up this way. *If you have Ubuntu and Windows installed on separate devices, you won’t need VirtualBox set up in either of the devices.*)
 - Download and install [TeamViewer Full Client](https://www.teamviewer.com/apac/download/windows/?utm_source=google&utm_medium=cpc&utm_campaign=restofasia%7Cb%7Cpr%7C22%7Cjun%7Ctv-core-download-sn%7Cnew%7Ct0%7C0&utm_content=Download&utm_term=download+teamviewer) on Windows and Ubuntu devices. Select appropriate OS versions when downloading.
You may find these tutorials useful:

   [How To Install Team Viewer Remote Access Latest version in Ubuntu 20.04](https://www.youtube.com/watch?v=4X3s_OqtwHY)

   [How to Install and Use TeamViewer in Windows | Latest Version 2023](https://www.youtube.com/watch?v=efOT1JuGJN4)

 - On your Ubuntu device, download the files in this repository and extract them in an empty folder of your preference. Run the `run_nav_sim.sh` file using a Terminal:

   `bash run_nav_sim.sh`
   
   This will start installing, if not already installed, the necessary components to run this module (may take a while on the first run). Once finished, a GUI should appear, as seen in figure-1. You can run the bash scripts more than once (even if there exists a workspace folder already. It will not create duplicates).
   
![](https://lh7-us.googleusercontent.com/BXPZ95RaJUfKw5nC7CXB6wu0L5qzv_P2iItVl_igx8FP94fDvdo8HzDl9PD1VHK7qtBY0guFL5k3UWoArByPH2cTupWh_O93hJIb8FhUsAvIBiQFCKwnJ-ydkvcFs_Poif5bFs51SSEbDJgZHg_cJoE)
 *figure-1: Graphical User Interface (GUI) for this module. GUI contains buttons for steering, slider for speed adjustment and video feed for visual navigation.*

### Your Task
For this module, you will have to complete the following tasks:

 1. Setup TeamViewer on Windows and Ubuntu and make sure that Ubuntu can be accessed from the Windows device.
 2. Run `roscore` in one terminal in the Ubuntu 20.04 machine where ROS is installed.
 3. In a new terminal, run the [bash script](https://github.com/InterplanetarCodebase/recruitment24_nav_task/blob/main/run_nav_sim.sh) by typing the following command:
    
    `bash run_nav_sim.sh`

    It should open up the GUI. **Do not run any other ros command or linux command other than this command. If you are in a conda environment, deactivate it by using `conda deactivate`.**

4.  Go to your remote machine (Windows) and establish the TeamViewer connection. Now you should be able to access the running GUI from the remote machine via TeamViewer.
    
5.  You have to drive to the desired GREEN squares in the random order **displayed below the camera box of the GUI** (number of the Task order represents the id of the squares, as shown in figure-3). 
    ![2D map of nav_task](https://lh7-us.googleusercontent.com/zkQym1Kd9TQrXRUQiXa_i7S5AFwI_nUUdcdQZ_lMj6a3f9r9GXaXssZAnhtqVwDpMmuO47TelF1LLcUfGIQetrsexd5P2C0qXsLd2RhtyVrHmzEEjklL4f023ychpoobJs7OibsuOuqmEqzx0tB4jCA)
    *figure-2: The 2D map of the test ground. You must navigate the Turtlebot to the GREEN spots in the sequence indicated on the GUI (below the camera feed) and avoid the RED spots.*
    
	![](https://lh7-us.googleusercontent.com/YuCTkFx1TcmIqWZA_iFP_2MpNoIWfRbokwTDRI5-8on-7V4Hc5gQrz4R50MT3dvgpYbC1GcSMnDAX8eKRM1nuIgh9wNXKUj2i4y6Yi7egXkF8wG-bT4ErNoYGQY55wzB5xZVo4en-gBXkzrYDL8PHTk)
	*figure-3: TOP VIEW of the test ground, indicating the ID of the GREEN spots and initial pose of the Turtlebot.*
	
	 - You won't see any indication of the ID of the GREEN squares in the video feed. *You have to know the map well enough to recognize which square is which and where to go next.*
	 - The bot starts from the **central RED circle** and faces the **positive x direction**. After you start driving and leave the initial RED circle you** can not step on any of the RED circles (including the first one) otherwise there will be a penalty.**
	 - After completing this task, you can close the GUI window and terminate the program from terminal window using `ctrl+c` (you may need to enter `ctrl+c` twice).
 
6.  Record the entire process (from running the bash script to driving the Turtlebot) in a video with a screen recorder from the machine that you are driving from (remote machine). **No cuts or edits in the video are accepted.** Submit the video to the referred medium in MP4 format.
    
7.  Submit the `nav_output.bag` file that will be generated after you have closed the GUI window and ctrl+c the terminal window. This file can be found at `your_ws_folder/task_ws/nav_output.bag`.

> NOTE: There is no time limit to this module. Generally, it should take around 30 minutes to set up and complete the task. 


### Troubleshooting and Debugging

 - In case of any error, take a screenshot of the erroneous console and [mail](mailto:interplanetar.troubleshooting@gmail.com) us. Please, *do not post it in the Google Classroom.*
 - If you face any error while running the bash file, delete the `task_ws/` folder before trying again.
