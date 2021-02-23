# Floor Plan

Steps to add a floor plan on Home Assistant (3D view).

To edit images: [video](https://www.youtube.com/watch?v=9p9PBtM0O8Q)


## Requirements

- Ubuntu 20.04
- SweetHome3D (http://www.sweethome3d.com/)


## 3D Floor plan

1. Install SweetHome3D: `sudo apt install sweethome3d`

2. Open SweetHome3D and open the house created or use an example house available [here](http://www.sweethome3d.com/gallery.jsp)

3. Take a photo:
    
    1.1 Choose the best angle to the view

    1.2 `3D view/create photo...` on menu

    1.3 The quality must the best and you can choose the time of the day. The lens option must be `Depth of field`

    1.4 Click on Create and then store the photo

4. Toggle the light status (in this case turn on the light):

    2.1 Double click on lamp (plan)

    2.2 Change light power (light off = 20%; light on = 50%). It depends on the hour that you will choose to take the photo.

5. For the light on it is necessary to take a photo and store it.

**NOTE**: Only on the photo result is possible to see the effect of the light on.

# Home Assistant integration

1. On Home Assistant directory create another directory (www).

2. Copy the photos obtained to www directory

3. Restart Home Assistant:
    
    3.1 `sudo systemctl stop homeassistant`

    3.2 `sudo systemctl start homeassistant`

    3.3 To test if you can access/see the images, you can see here: `http://home:8123/local/kitchenLight.png`

4. On Home Assistant:
    
    4.1 Create a card

    4.2 Choose Plant status option
    
    4.3 Copy the content of the config.yml


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details