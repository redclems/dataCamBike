# dataCamBike

## Description

This project, developed as part of the Master's in Embedded Systems for Signal Processing of Images and Sound in Clermont Ferrand, aims to create an affordable embedded system for collecting and analyzing essential data during mountain biking (MTB) sessions. Using a Raspberry Pi and a wide-angle camera, this device provides a simple and effective solution to enhance the performance and settings of full-suspension bikes.

## Features

- **Data Acquisition:** The wide-angle camera records the bike in motion, capturing data such as fork and rear suspension movements, rider posture, center of gravity, pedaling technique, speed, pedal revolutions per minute, and potentially disc temperature with the addition of a thermal camera.

- **Real-time Data Processing:** The Raspberry Pi analyzes information in real-time, generating a video for further analysis at the end of the recording.

- **Visual Presentation:** Results are presented in the form of graphs, providing a clear visualization of both bike and rider performance. Accessible through a web page hosted on the Raspberry Pi.

## Usage

The device, housed in a 3D-printed case powered by a battery, can be attached to the bike using a selfie stick. It is designed for easy installation and use during training sessions.

## Installation

# Project Installation Guide

## System Installation on Raspberry Pi

1. **Create a New Raspberry Pi Image:** Use an image creation tool to install the operating system on your Raspberry Pi.

2. **Configure the Main User:** Use the main user `dataCamBike`. Ensure SSH is activated during the initial setup.

3. **Set up WiFi:** Configure the Raspberry Pi to connect to a WiFi network. For example, share the internet connection from your phone and save the connection information.

4. **Find Raspberry Pi's IP:** In a terminal, type the following command to find the Raspberry Pi's IP:
   ```bash
   arp -a
   ```

5. **SSH Connection:** Use the SSH command to connect to the Raspberry Pi:
   ```bash
   ssh dataCamBike@[IP]
   ```

## System Updates

6. **System Updates:** Execute the following commands to update the Raspberry Pi system:
   ```bash
   sudo apt update
   sudo apt upgrade
   sudo apt update
   ```

## Samba Installation (Optional)

7. **Install Samba (Optional):** Use the following commands to install Samba if you want to share files:
   ```bash
   sudo apt-get install samba samba-common-bin
   ```

8. **Configure Samba Sharing:** Edit the Samba configuration file:
   ```bash
   sudo nano /etc/samba/smb.conf
   ```
   Add the following lines:
   ```bash
   [dataCamBike]
   comment = Home share for the project
   path = /home/dataCamBike
   read only = no
   guest ok = yes
   create mask = 0666
   directory mask = 0666
   ```

9. **Restart Samba:** Apply changes and restart the Samba service:
   ```bash
   sudo systemctl restart smbd.service
   ```

## Apache Installation

10. **Install Apache:** Use the following command to install Apache:
    ```bash
    sudo apt install apache2
    ```

11. **Server Administration Commands:** Use the following commands to administer the Apache server:
    ```bash
    sudo chown -R dataCamBike:www-data /var/www/html/
    sudo chmod -R 770 /var/www/html/
    ```

12. **Configure Apache:** Edit the Apache configuration by editing the `000-default.conf` file:
    ```bash
    sudo nano /etc/apache2/sites-enabled/000-default.conf
    ```
    Set the `DocumentRoot` as follows:
    ```bash
    DocumentRoot /home/dataCamBike/dataCamBike/www/html
    ```

13. **Modify Apache Configuration File:** Edit the Apache configuration file:
    ```bash
    sudo nano /etc/apache2/apache2.conf
    ```
    Modify it as follows:
    ```bash
    <Directory /home/dataCamBike/dataCamBike/www/>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
    ```

14. **Restart Apache:** Apply changes and restart Apache:
    ```bash
    sudo service apache2 restart
    ```

## Raspberry Pi Configuration

15. **Enable I2C:** Use the following command to enable I2C:
    ```bash
    sudo raspi-config
    ```

16. **Additional Updates:** Perform additional updates with the following commands:
    ```bash
    sudo rpi-update
    sudo apt install -y python3-picamera2
    ```

17. **PiCamera Test:** Ensure that PiCamera works correctly by taking a photo.

18. **Install OpenCV:** Install OpenCV with the following commands:
    ```bash
    sudo apt install -y python3-opencv
    sudo apt install -y opencv-data
    ```

The project is now correctly installed on your Raspberry Pi. Refer to the complete documentation for detailed instructions on usage and customization.

## List of Components for the Project

To implement the MTB Surveillance and Analysis project, you will need the following components:

1. **Raspberry Pi 3 or Raspberry Pi 4:** The core of the project, responsible for data collection, processing, and analysis. Ensure you have necessary accessories such as a microSD card and power cable.

2. **Wide-Angle Camera:** A wide-angle camera with adjustable shutter speed. If needed, choose a camera with a lens that allows better capture of bike movements.

3. **External Battery:** An external battery to power the Raspberry Pi during MTB sessions. Ensure you have a compatible cable to connect the battery to the Raspberry Pi.

4. **Selfie Stick:** Use a selfie stick to securely mount the 3D-printed case containing the Raspberry Pi and camera to the bike frame.

5. **On/Off Switch:** Add a switch for easy power control of the Raspberry Pi, conserving battery energy when the device is not in use.

6. **MicroSD Card:** Ensure you have a microSD card with sufficient capacity for the operating system and captured data.

7. **Cables and Connections:** Ensure you have all necessary cables to connect the camera, battery, and switch to the Raspberry Pi.

8. **3D-Printed Case:** A 3D-printed case to house the Raspberry Pi, camera, battery, and possibly the switch. Ensure the case is designed to protect components from shocks and weather conditions.

Adjust the quantities and specifications based on your specific project requirements. Make sure to verify compatibility of components and follow the mounting and installation instructions provided by the respective manufacturers.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.