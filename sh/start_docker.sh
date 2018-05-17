docker stop $(docker ps -a | awk '{print $1}')
docker rm $(docker ps -a | awk '{print $1}')
docker run -d --name=jenkins --hostname=centos6-jenkins --privileged -i -t -p 2222:22 -p 1101:1101 -p 8081:8080 -p 90:80 -p 5037:5037 -p 4723:4723 192.168.248.195/appium_test/appium/robotframework:v2 /usr/sbin/sshd -D