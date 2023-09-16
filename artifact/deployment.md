#After launching EC2 instance with Key name dissertationAWS.

chmod 400 dissertationAWS.pem
ssh -i "dissertationAWS.pem" ubuntu@ec2-100-26-239-205.compute-1.amazonaws.com

# install docker in Ubuntu EC2 instance.

### Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

### Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

### install dokcer dependencies
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo groupadd docker
sudo usermod -aG docker $USER
docker run hello-world
sudo apt install unzip

## Deploy artefact
Zip the dissertation folder with dissertation-main.zip 

## send the zip to EC2 instance.
scp -i "dissertationAWS.pem" dissertation-main.zip  ubuntu@ec2-35-171-52-53.compute-1.amazonaws.com:/home/ubuntu/

## create .localdata folder inside pipeline folder

sudo chmod 777 .localdata

sudo chmod 777 .localdata/zookeeper
sudo chown ubuntu .localdata/zookeeper

sudo chmod 777 .localdata/bookkeeper
sudo chown ubuntu .localdata/bookkeeper

sudo chmod 777 .localdata/bookkeeper2
sudo chown ubuntu .localdata/bookkeeper2

## run pipeline in /pipeline folder

sudo docker-compose up -d

