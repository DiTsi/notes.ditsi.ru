# Arduino

## Restore Arduino bootloader

- In Arduino IDE open Example 11. ArduinoISP
- Save copy of project in your dir
- Compile it
- In menu "Sketch" > "Export compiled Binary"
- Rename HEX firmware with bootloader to main.hex
- Connect USBASP programmer to Arduino board
- Flash file "main.hex" with command
  ```shell
  avrdude -c usbasp -p atmega328p -u -U flash:w:./main.hex -F
  ```
