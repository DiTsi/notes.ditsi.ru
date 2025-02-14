# avrdude

## Commands

```shell
avrdude -c usbasp -p attiny2313 -U flash:r:./1.hex
avrdude -c usbasp -p attiny2313 -U flash:w:/home/ditsi/temp/trash/avr/1.hex

# do not verify
avrdude -c usbasp -p attiny2313 -V -U flash:w:/home/ditsi/temp/trash/avr/1.hex
```

## Fuses

```shell
# read fuses
avrdude -c usbasp -p m328p -U lfuse:r:

# write fuses
avrdude -c usbasp -p m8 -U lfuse:w:0xE4:m
```