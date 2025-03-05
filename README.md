**This is sample docker repo for tax calculator app using flask**

**step 1:**
clone the git repo
cmd - git clone https://github.com/Akhilrdy26/tax_pay_cal

**step 2:**
run build command
cmd - docker build .

**step 3:**
check image
cmd - docker images

**step4:**
run the docker image
cmd - docker run -p 5000:5000 -it <image id>
-> "-p" used to run the docker image in the particular port

now the flask is running in the port 
**note** - when running in ec2 instance dont froget to open inbound prot 5000

