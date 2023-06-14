# Wordpress-Site-Manager
This script allows you to easily manage WordPress sites using Docker containers and docker-compose.

## Installation
Ensure that Docker is installed on your system. If Docker is not installed, you can install it by running the following command:

```
sudo apt-get install docker
```

Verify that Docker is installed correctly by running the following command:
```
docker --version
```

Install docker-compose by running the following command:
```
sudo apt-get install docker-compose
```

Verify that docker-compose is installed correctly by running the following command:
```
docker-compose --version
```


Clone this repository to your local machine using Git:
```
git clone https://github.com/Sanketar/wordpress-site-manager.git
```

Change to the project directory:
cd wordpress-site-manager

## Usage
### Creating a WordPress Site
To create a WordPress site, use the following command:
```
python script.py create [site-name]
```
Replace [site-name] with the desired name for your WordPress site. This command will create a directory with the specified site name, generate a docker-compose.yml file, start the containers, and add an entry to the /etc/hosts file.

### Enabling or Disabling the Site
To enable or disable the site, use the following command:
```
python script.py enable|disable
```
Replace enable with disable to disable the site. This command will start or stop the Docker containers for the specified site.

enable: Enables the site.
Description: This command enables the site, allowing it to be accessed and served.

disable: Disables the site.
Description: This command disables the site, temporarily preventing it from being accessed or served.

### Deleting the Site
To delete the site, use the following command:
```
python script.py delete
```
This command will stop the Docker containers, remove the site directory, and clean up all associated files.

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
