# User Instructions 


# [Under Development!!!]

AMAZON WEB SERVICES (AWS):
Redeeming AWS credits:
From https://aws.amazon.com/ choose "Sign in to the Console"
Choose "root user sign in" and enter your AWS email address and password
In "Services", choose "billing" and on left menu choose "credits"  (OR go to aws.amazon.com/awscredits )
Redeem your AWS credit using the code on the voucher provided at the workshop

Launching AWS virtual machine:
Go to "Services" and under the "compute" heading, choose "EC2"
Set "region" in top-right corner to be Ireland
Click on "Launch Instance"
Select "Deep Learning AMI CUDA 8 Ubuntu Version"
Scroll down and select "GPU compute ... p2.xlarge"
Click Review and Launch
Click Launch
Choose your existing key pair (.pem) file   (Peter: maybe some instruction on how to set this up on the fly for participants who don't have it done in advance?) 

Connecting to the launched instance:
From EC2 dashboard->instances  (Need to check again how to get there from previous step!!)
You should see your launched instance listed
To connect to the instance 
 - copy public DNS(ipv4) field
 - type ssh -Y -i /path/my-key-pair.pem ubuntu@[copied-DNS]
   (you may need to type chmod 400 /path/my-key-pair.pem if your key_pair permissions are incorrect) 
(If in doubt, see also http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

Now you should be logged into the machine and see a command-line prompt $.
Type the following commands to get setup for running the code:
mkdir -p cork_ai/meetup1   (make a new folder to work in) 
cd cork_ai/meetup1         (switch to the newly created folder)
wget https://raw.githubusercontent.com/tensorflow/tensorflow/r1.3/tensorflow/examples/tutorials/mnist/mnist_softmax.py
vim mnist_softmax.py  (to look at the code you are about to run)
 ........(Type Esc then : then q! and hit enter to exit the file)

To run the first tutorial code:
Type python mnist_softmax.py (and wait up to 2/3 mins!) 
Number printed at end (~0.92) is the accuracy of the network

If you complete this with time to spare.......... 

sudo apt install eog


Stopping/Terminating your instance.
If you do not object to losing your work, terminate.
If you want to save your work, choose stop, but be aware of small cost for volume storage.

