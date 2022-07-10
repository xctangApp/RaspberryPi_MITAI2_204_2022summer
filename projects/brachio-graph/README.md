
#### Prerequisite:
Raspberry Pi OS is installed and upgraded.

#### Build the plotter

References:

- https://www.brachiograph.art/get-started/build.html
- https://www.brachiograph.art/get-started/wiring.html
- https://www.brachiograph.art/how-to/calibrate.html
- https://www.brachiograph.art/how-to/use-turtle-draw.html
- https://www.brachiograph.art/explanation/understand-plotter-geometry.html#understand-plotter-geometry
- https://www.raspberrypi.org/documentation/usage/gpio/
- https://pinout.xyz/

#### Use bash command to set up enviroment (one command setup)
```
wget -O - https://raw.githubusercontent.com/xctangApp/RaspberryPi_MITAI2_204_2022summer/main/projects/brachio-graph/enviroment-setup.sh | bash


```

#### Start up the BrachioGraph

Power up the Raspberry Pi and test from Python Shell.

https://www.brachiograph.art/get-started/drive.html


- Draw a map (images/africa.jpg)
```
cd ~/BrachioGraph
wget -O - https://raw.githubusercontent.com/ciedfwsecc/2021SECC_DivisionB_Project/main/projects/brachio-graph/africa_map_draw.py > africa_map_draw.py
python3 africa_map_draw.py
```

- Draw a photo
```
cd ~/BrachioGraph
wget -O - https://raw.githubusercontent.com/ciedfwsecc/2021SECC_DivisionB_Project/main/projects/brachio-graph/photo_draw.py > photo_draw.py
wget -O - https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/600px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg > images/monalisa.jpg
python3 photo_draw.py monalisa
```

- Download a photo and Draw
```
cd ~/BrachioGraph
wget --no-cache -O - https://raw.githubusercontent.com/ciedfwsecc/2021SECC_DivisionB_Project/main/projects/brachio-graph/download_draw.py > download_draw.py
python3 download_draw.py "https://cdn.hpm.io/wp-content/uploads/2016/02/texas-and-new-hampshire-1000x666.jpg"
```



#### some good libraries and references
https://gpiozero.readthedocs.io/en/stable/index.html

https://www.brachiograph.art/index.html

