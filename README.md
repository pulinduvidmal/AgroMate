# AgroMate: Precision Agriculture System

AgroMate is a comprehensive Precision Agriculture System designed to address key challenges in modern farming, including inefficient water management, imprecise soil monitoring, and wildlife threats to crops. Leveraging cutting-edge IoT technology and AI-driven solutions, AgroMate aims to optimize agricultural practices, enhance crop yields, and promote sustainable farming methods.

## Table of Contents
- [Introduction](#introduction)
- [Problem Definition](#problem-definition)
- [Proposed Solution](#proposed-solution)
- [Technical Overview](#technical-overview)
- [Animal Detection](#animal-detection)
- [Team Members](#team)

## Introduction
Modern agriculture faces numerous challenges, from unpredictable weather patterns to resource constraints and environmental concerns. AgroMate aims to mitigate these challenges by providing farmers with advanced tools and insights to optimize their farming practices.

## Problem Definition
The challenges in agriculture, such as inefficient water management, imprecise soil monitoring, and wildlife threats, can have significant impacts on crop yields and sustainability. AgroMate addresses these challenges by integrating real-time weather monitoring, smart irrigation systems, IoT-enabled soil sensors, and AI-driven wildlife monitoring.

## Proposed Solution
AgroMate offers a comprehensive solution to modern agricultural challenges. Its key features include:
- Real-time weather monitoring for informed decision-making.
- Smart irrigation systems for efficient water management.
- IoT-enabled soil sensors for precise soil monitoring.
- AI-driven wildlife monitoring for proactive crop protection.
- User-friendly interface and centralized dashboard for easy management.

## Technical Overview
AgroMate integrates hardware components such as weather sensors and soil sensors with software components including decision-making algorithms and user interfaces. The system utilizes data analytics and machine learning to provide real-time insights and automate farming processes.

## Animal Detection
For animal detection, AgroMate utilizes a Python script named `cam_server_with_detection.py`, which incorporates machine learning models from the Keras library and computer vision capabilities from the OpenCV library. The script is designed to run a Flask server that streams live video from a camera while simultaneously performing animal detection. This functionality enables farmers to monitor wildlife activity in their fields and take proactive measures to protect their crops.

### Trained Model
The animal classification model used in AgroMate is trained to classify the following animals:
0. Chicken
1. Elephant
2. Hamster
3. Skunk
4. Rabbit
5. Monkey
6. Wild Boar
7. Birds

### Usage
1. Ensure you have the necessary dependencies installed, including Keras, OpenCV, and Flask.
2. Run the `cam_server_with_detection.py` script.
3. Access the live video stream through the provided URL.

## Team
This project is proudly developed by the ElectroMavericks Team:
- [Prabodha K.P.K.A](https://github.com/AkhilaPrabodha)
- [Vidmal H.V.P](https://github.com/pulinduvidmal)
- [Nayanthara J.N.P](https://github.com/Navini11)
- [Surendra S.A.J.E](https://github.com/eshansurendra)
- [Achira Hansindu](https://github.com/)


