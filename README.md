# ItsAnThermometer
Its a simple Thermometer... what did you expect. It has 3 leds for tempature (under 20 for blue, 20-24 for green and over 24 for red. But can be changed) powered but a XIAO RP2040
## How to use
1. Build it
2. Flash circutpython to the XIAO
3. Upload main.py to it
4. Plug in or add 4x AA batteries
6. Observe

You can use the toggle switch to change the power source

## Why did I make it
I was sick so I was off school and had 2 days to make something and I needed one. Also it is to show my little brother eletronics.

## Schematic

<img width="2400" height="2100" alt="image" src="https://github.com/user-attachments/assets/f3878732-837e-46bf-ad78-1839a726f517" />

## PCB

<img width="907" height="778" alt="image" src="https://github.com/user-attachments/assets/561e0880-15fc-449c-91ca-4fab389b91ac" />

## 3D Model

<img width="1920" height="1080" alt="ThermometerPLAN" src="https://github.com/user-attachments/assets/b4bafbf3-d485-48ac-bc89-b6058a09d34e" />
<img width="1920" height="1080" alt="ThermometerISO" src="https://github.com/user-attachments/assets/4a2f8e73-603a-45b8-b7b7-6b67817c6ab5" />
<img width="1920" height="1080" alt="ThermometerBOARD" src="https://github.com/user-attachments/assets/ee026fe0-0b61-455a-b98e-71b884f82aeb" />


## BOM

|Reference(s)|Qty|Value/Description             |MFR                         |MFR No.        |Mouser No.         |Unit Price GBP    |Total Price GBP|Link                                                                                                           |FIELD10            |FIELD11               |FIELD12        |
|------------|---|------------------------------|----------------------------|---------------|-------------------|------------------|---------------|---------------------------------------------------------------------------------------------------------------|-------------------|----------------------|---------------|
|~           |5  |PCB and Partial assebly       |JLCPCB                      |~              |~                  |~                 |2.46           |https://jlcpcb.com/                                                                                            |                   |                      |               |
|U2          |1  |Seeed XIAO RP2040 with Headers|Raspberry Pi                |102010630      |713-102010630      |3.9               |3.9            |https://www.mouser.co.uk/ProductDetail/Seeed-Studio/102010630?qs=sqEgtWRSLJ0HHL%252BkmwiGyA%3D%3D              |                   |                      |               |
|U1          |1  |LM35 Temp sensor              |Texas Instruments           |LM35DZ/LFT1    |926-LM35DZ/LFT1    |1.26              |1.26           |https://www.mouser.co.uk/ProductDetail/Texas-Instruments/LM35DZ-LFT1?qs=QbsRYf82W3H30AtKgrS0IA%3D%3D           |                   |                      |               |
|BT1         |1  |4x AA Battey Holder           |Keystone Electronics        |2477           |534-2477           |1.6               |1.6            |https://www.mouser.co.uk/ProductDetail/Keystone-Electronics/2477?qs=Q3RoVmURDolEbXnNenQutg%3D%3D               |                   |                      |               |
|R2, R3      |2  |10ohm resistor                |YAGEO                       |MF0207FTE52-75R|603-MF0207FTE52-75R|0.08              |0.16           |https://www.mouser.co.uk/ProductDetail/YAGEO/MF0207FTE52-10R?qs=Is6ZsIPfHkZVWUebLBVbaw%3D%3D                   |                   |                      |               |
|R1          |1  |75ohm resistor                |YAGEO                       |MF0207FTE52-75R|603-MF0207FTE52-75R|0.08              |0.08           |https://www.mouser.co.uk/ProductDetail/YAGEO/MF0207FTE52-75R?qs=KUIzHt%2Fe91nXiKietXMfvA%3D%3D                 |                   |                      |               |
|SW1         |1  |SPDT Switch                   |E-Switch                    |100SP1T1B4M2QE |612-100-A1421      |1.97              |1.97           |https://www.mouser.co.uk/ProductDetail/E-Switch/100SP1T1B4M2QE?qs=YXf4ACKMM4xJ0mJK%2FyIa1g%3D%3D               |                   |                      |               |
|J1          |1  |USB A Port                    |Molex                       |67643-0910     |538-67643-0910     |1.12              |1.12           |https://www.mouser.co.uk/ProductDetail/Molex/67643-0910?qs=EuyFtE1skifNhj6pwWTsXw%3D%3D                        |                   |                      |               |
|C1          |1  |100nF Capacitor               |Vishay / BC Components      |K104K15X7RF5WH5|594-K104K15X7RF5WH5|0.17              |0.17           |https://www.mouser.co.uk/ProductDetail/Vishay-BC-Components/K104K15X7RF5WH5?qs=8fb2TFeI5qGYDjl7%252BWZxcg%3D%3D|                   |                      |               |
|D4, D5      |2  |Schottky Diode                |Vishay General Semiconductor|SB140-E3/73    |625-SB140-E3/73    |0.14              |0.28           |https://www.mouser.co.uk/ProductDetail/Vishay-General-Semiconductor/SB140-E3-73?qs=u91jd7aysvPpl5oKH36UtQ%3D%3D|                   |                      |               |
|U3          |1  |AMS1117-3.3 Breakout Board    |Texas Instruments           |~              |~                  |1.26              |1.26           |https://www.aliexpress.com/item/1005007091283048.html                                                          |                   |                      |               |
|D1, D2, D3  |3  |Coloured LEDs                 |~                           |~              |~                  |(In a 450pcs pack)|0.76           |https://www.aliexpress.com/item/1005008664239729.html                                                          |                   |                      |               |
|~           |2  |Screw 6 mm M3                 |RND                         |610-00421      |~                  |(In 200pcs pack)  |0.74           |https://uk.rs-online.com/web/p/machine-screws/0492499                                                          |                   |                      |               |
|~           |1  |10cm x 10cm MDF 12mm Thick    |MEDITE                      |~              |~                  |2                 |2              |https://www.cutmy.co.uk/wood/mdf-board/standard/12mm/L100-W100/                                                |                   |                      |               |
|            |   |                              |                            |               |                   |                  |               |                                                                                                               |                   |                      |               |
|            |   |                              |                            |               |                   |                  |               |                                                                                                               |                   |Total Price USD approx|Total Price GBP|
|            |   |                              |                            |               |                   |                  |               |                                                                                                               |Items              |23.7                  |17.76          |
|            |   |                              |                            |               |                   |                  |               |                                                                                                               |Shipping (and fees)|24.72                 |18.52          |
|            |   |                              |                            |               |                   |                  |               |                                                                                                               |Final              |48.42                 |36.28          |
