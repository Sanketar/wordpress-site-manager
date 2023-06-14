import os
import subprocess
import sys

# Function to check if a command is available
def command_exists(cmd):
    return subprocess.call(f"command -v {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

# Function to install missing packages
def install_packages(packages):
    subprocess.call(f"apt-get install -y {packages}", shell=True)

# Function to create a WordPress site using Docker and docker-compose
def create_wordpress_site(site_name):
    # Create a directory for the site
    os.makedirs(site_name, exist_ok=True)
    os.chdir(site_name)

    # Create a docker-compose.yml file
    docker_compose = f"""
    version: '3'
    services:
      db:
        image: mysql:5.7
        volumes:
          - db_data:/var/lib/mysql
        restart: always
        environment:
          MYSQL_ROOT_PASSWORD: example_root_password
          MYSQL_DATABASE: {site_name}_db
          MYSQL_USER: {site_name}_user
          MYSQL_PASSWORD: example_password

      wordpress:
        depends_on:
          - db
        image: wordpress:latest
        volumes:
          - ./wp:/var/www/html
        ports:
          - 8000:80
        restart: always
        environment:
          WORDPRESS_DB_HOST: db
          WORDPRESS_DB_USER: {site_name}_user
          WORDPRESS_DB_PASSWORD: example_password
          WORDPRESS_DB_NAME: {site_name}_db
    volumes:
      db_data:
    """

    with open("docker-compose.yml", "w") as file:
        file.write(docker_compose)

    # Start the containers
    subprocess.call("docker-compose up -d", shell=True)

    # Add /etc/hosts entry
    with open("/etc/hosts", "a") as file:
        file.write(f"127.0.0.1 {site_name}\n")

    # Prompt the user to open the site
    print(f"Open http://{site_name} in your browser")

# Function to enable or disable the site
def enable_disable_site(enable):
    action = "start" if enable else "stop"
    subprocess.call(f"docker-compose {action}", shell=True)

# Function to delete the site
def delete_site():
    subprocess.call("docker-compose down", shell=True)
    os.chdir("..")
    site_name = os.getcwd().split("/")[-1]
    os.rmdir(site_name)

# Main script logic
if __name__ == "__main__":
    if not command_exists("docker"):
        install_packages("docker")
    if not command_exists("docker-compose"):
        install_packages("docker-compose")

    if len(sys.argv) < 2:
        print("Please provide a site name as a command-line argument")
        sys.exit(1)

    site_name = sys.argv[1]
    create_wordpress_site(site_name)
