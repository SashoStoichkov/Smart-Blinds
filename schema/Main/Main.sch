EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Raspberry_Pi_2_3 RPi3
U 1 1 5E1FF9CE
P 1700 2150
F 0 "RPi3" H 1700 3631 50  0000 C CNN
F 1 "Raspberry_Pi_3" H 1700 3540 50  0000 C CNN
F 2 "" H 1700 2150 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 1700 2150 50  0001 C CNN
	1    1700 2150
	1    0    0    -1  
$EndComp
$Comp
L Sensor:BME280 TempSensor
U 1 1 5E20274D
P 3700 1350
F 0 "TempSensor" V 3133 1350 50  0000 C CNN
F 1 "BME280" V 3224 1350 50  0000 C CNN
F 2 "Package_LGA:Bosch_LGA-8_2.5x2.5mm_P0.65mm_ClockwisePinNumbering" H 5200 900 50  0001 C CNN
F 3 "https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BME280-DS002.pdf" H 3700 1150 50  0001 C CNN
	1    3700 1350
	0    1    1    0   
$EndComp
NoConn ~ 900  1250
NoConn ~ 900  1350
NoConn ~ 900  1550
NoConn ~ 900  1650
NoConn ~ 900  1750
NoConn ~ 900  1950
NoConn ~ 900  2050
NoConn ~ 900  2150
NoConn ~ 900  2550
NoConn ~ 900  2650
NoConn ~ 900  2750
NoConn ~ 900  2850
NoConn ~ 1300 3450
NoConn ~ 1400 3450
NoConn ~ 1500 3450
NoConn ~ 1600 3450
NoConn ~ 1700 3450
NoConn ~ 1800 3450
NoConn ~ 1900 3450
NoConn ~ 3100 1250
NoConn ~ 4300 1250
NoConn ~ 1500 850 
NoConn ~ 1600 850 
NoConn ~ 1800 850 
Text GLabel 1900 850  2    50   Input ~ 0
3V3
Text GLabel 4300 1450 2    50   Input ~ 0
3V3
Text GLabel 2500 1550 2    50   Input ~ 0
SDA
Text GLabel 2500 1650 2    50   Input ~ 0
SCL
Text GLabel 3600 1950 3    50   Input ~ 0
SDA
Text GLabel 3800 1950 3    50   Input ~ 0
SCL
NoConn ~ 3400 1950
NoConn ~ 2500 1250
NoConn ~ 2500 1350
NoConn ~ 2500 1850
NoConn ~ 2500 1950
NoConn ~ 2500 2050
NoConn ~ 2500 2250
NoConn ~ 2500 2350
NoConn ~ 2500 2450
NoConn ~ 2500 2550
NoConn ~ 2500 2650
NoConn ~ 2500 2850
NoConn ~ 2500 2950
$Comp
L power:GND #PWR?
U 1 1 5E22C65D
P 4000 1950
F 0 "#PWR?" H 4000 1700 50  0001 C CNN
F 1 "GND" H 4005 1777 50  0000 C CNN
F 2 "" H 4000 1950 50  0001 C CNN
F 3 "" H 4000 1950 50  0001 C CNN
	1    4000 1950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E22E222
P 3100 1450
F 0 "#PWR?" H 3100 1200 50  0001 C CNN
F 1 "GND" H 3105 1277 50  0000 C CNN
F 2 "" H 3100 1450 50  0001 C CNN
F 3 "" H 3100 1450 50  0001 C CNN
	1    3100 1450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E22E909
P 2000 3450
F 0 "#PWR?" H 2000 3200 50  0001 C CNN
F 1 "GND" H 2005 3277 50  0000 C CNN
F 2 "" H 2000 3450 50  0001 C CNN
F 3 "" H 2000 3450 50  0001 C CNN
	1    2000 3450
	1    0    0    -1  
$EndComp
Text GLabel 3400 2550 0    50   Input ~ 0
SCL
Text GLabel 4000 2550 2    50   Input ~ 0
SDA
Text GLabel 4000 2650 2    50   Input ~ 0
3V3
$Comp
L TSL2591:TSL2591 LightSensor
U 1 1 5E21D573
P 3700 2850
F 0 "LightSensor" H 3700 3415 50  0000 C CNN
F 1 "TSL2591" H 3700 3324 50  0000 C CNN
F 2 "" H 3700 3050 50  0001 C CNN
F 3 "" H 3700 3050 50  0001 C CNN
	1    3700 2850
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E20FB04
P 3400 2750
F 0 "#PWR?" H 3400 2500 50  0001 C CNN
F 1 "GND" H 3405 2577 50  0000 C CNN
F 2 "" H 3400 2750 50  0001 C CNN
F 3 "" H 3400 2750 50  0001 C CNN
	1    3400 2750
	1    0    0    -1  
$EndComp
NoConn ~ 3400 2650
Wire Wire Line
	4950 1150 4900 1150
Wire Wire Line
	4900 1150 4900 1050
Wire Wire Line
	4900 1050 4950 1050
$Comp
L Motor:Stepper_Motor_bipolar Motor1
U 1 1 5E3C1483
P 6400 1200
F 0 "Motor1" H 6588 1324 50  0000 L CNN
F 1 "Stepper_Motor_bipolar" H 6588 1233 50  0000 L CNN
F 2 "" H 6410 1190 50  0001 C CNN
F 3 "http://www.infineon.com/dgdl/Application-Note-TLE8110EE_driving_UniPolarStepperMotor_V1.1.pdf?fileId=db3a30431be39b97011be5d0aa0a00b0" H 6410 1190 50  0001 C CNN
	1    6400 1200
	1    0    0    -1  
$EndComp
Text GLabel 4950 1450 0    50   Input ~ 0
3V3
$Comp
L power:GND #PWR?
U 1 1 5E3D2796
P 4950 1550
F 0 "#PWR?" H 4950 1300 50  0001 C CNN
F 1 "GND" H 4955 1377 50  0000 C CNN
F 2 "" H 4950 1550 50  0001 C CNN
F 3 "" H 4950 1550 50  0001 C CNN
	1    4950 1550
	1    0    0    -1  
$EndComp
$Comp
L A4998:A4988 MotorDriver1
U 1 1 5E3D5118
P 5350 1850
F 0 "MotorDriver1" H 5350 2915 50  0000 C CNN
F 1 "A4988" H 5350 2824 50  0000 C CNN
F 2 "" H 5350 2950 50  0001 C CNN
F 3 "" H 5350 2950 50  0001 C CNN
	1    5350 1850
	1    0    0    -1  
$EndComp
Text GLabel 900  2350 0    50   Input ~ 0
GPIO22
Text GLabel 900  2450 0    50   Input ~ 0
GPIO23
Text GLabel 4950 1250 0    50   Input ~ 0
GPIO22
Text GLabel 4950 1350 0    50   Input ~ 0
GPIO23
Text GLabel 5750 1350 2    50   Input ~ 0
1B
Text GLabel 6100 1300 0    50   Input ~ 0
1B
Text GLabel 5750 1250 2    50   Input ~ 0
1A
Text GLabel 5750 1150 2    50   Input ~ 0
2A
Text GLabel 5750 1050 2    50   Input ~ 0
2B
Text GLabel 6100 1100 0    50   Input ~ 0
1A
Text GLabel 6500 900  1    50   Input ~ 0
2B
Text GLabel 6300 900  1    50   Input ~ 0
2A
$Comp
L Device:Battery_Cell Battery1
U 1 1 5E3E99B9
P 6950 1750
F 0 "Battery1" H 7068 1846 50  0000 L CNN
F 1 "9" H 7068 1755 50  0000 L CNN
F 2 "" V 6950 1810 50  0001 C CNN
F 3 "~" V 6950 1810 50  0001 C CNN
	1    6950 1750
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1 C
U 1 1 5E3ECAC5
P 6500 1700
F 0 "C" H 6615 1746 50  0000 L CNN
F 1 "100u" H 6615 1655 50  0000 L CNN
F 2 "" H 6500 1700 50  0001 C CNN
F 3 "~" H 6500 1700 50  0001 C CNN
	1    6500 1700
	1    0    0    -1  
$EndComp
Wire Wire Line
	5750 1550 5800 1550
Wire Wire Line
	6100 1550 6100 1900
Wire Wire Line
	6950 1450 6950 1550
Wire Wire Line
	6950 1900 6950 1850
Wire Wire Line
	6100 1900 6500 1900
Wire Wire Line
	5750 1450 6500 1450
Wire Wire Line
	6500 1450 6500 1550
Connection ~ 6500 1450
Wire Wire Line
	6500 1450 6950 1450
Wire Wire Line
	6500 1900 6500 1850
Connection ~ 6500 1900
Wire Wire Line
	6500 1900 6950 1900
$Comp
L power:GND #PWR?
U 1 1 5E4006C8
P 5800 1700
F 0 "#PWR?" H 5800 1450 50  0001 C CNN
F 1 "GND" H 5805 1527 50  0000 C CNN
F 2 "" H 5800 1700 50  0001 C CNN
F 3 "" H 5800 1700 50  0001 C CNN
	1    5800 1700
	1    0    0    -1  
$EndComp
Wire Wire Line
	5800 1700 5800 1550
Connection ~ 5800 1550
Wire Wire Line
	5800 1550 6100 1550
$EndSCHEMATC
