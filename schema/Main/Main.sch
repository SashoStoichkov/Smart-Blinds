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
NoConn ~ 900  2350
NoConn ~ 900  2450
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
$EndSCHEMATC
