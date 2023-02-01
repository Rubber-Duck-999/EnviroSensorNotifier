# EnviroSensorNotifier

Application that uses the Enviro Sensor pHat that sends sensor data

## Install

`pip3 install -r requirements`

## Enviro

pHAT that has multiple sensors for:
* Light
* Temperature
* Humidity

<img src="enviro.png" alt="Pimoroni Enviro" width="200"/>

[Link](https://shop.pimoroni.com/products/enviro?variant=31155658489939)


## Testing

`cd tests`
`python3 -m pytest`

## Logging

Logging to a file under user on linux

`/home/{user}/sync/EnviroSensorNotifier.log`

Im using this as Im using this folder to sync multiple devices