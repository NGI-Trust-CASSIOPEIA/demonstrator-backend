# Home Assistant - Demo


## Requirements

- Docker compose

## Docker

1. Create the env.sh file with user and passwords information

```
#!/bin/bash 
export INFLUXDB_ADMIN_PASSWORD=
export INFLUXDB_ADMIN_USER=
export INFLUXDB_USER=

export MYSQL_ROOT_PASSWORD= 
export MYSQL_USER= 
export MYSQL_PASSWORD=

```

And run `source env.sh`

2. Create the following directories:

    1.1 `mkdir homeassistant`

    1.2 `mkdir influxdb`

    1.3 `mkdir mariadb`

    1.4 `mkdir mosquitto`

    1.5 `mkdir mosquitto/mosquittoconf`

    1.6 `mkdir mosquitto/mosquittodata`
    
    1.7 `mkdir mosquitto/mosquittologs`

3. Run: `docker-compose up`


## Configurations

Due to the version 2 of Mosquitto it is necessary to add the following lines on Mosquitto configurations.

1. In `mosquitto/mosquittoconf/mosquitto.conf` add:

    1.1 `listener 1883`
    1.2 `allow_anonymous true`


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details