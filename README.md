# User Instructions 

### Full instructions for running the tutorials at Cork AI's first meetup

##### 1: AMAZON WEB SERVICES (AWS):  
**Redeeming AWS credits:**  
 - From https://aws.amazon.com/ choose "Sign in to the Console"
 - Choose "root user sign in" and enter your AWS email address and password
 - In "Services", choose "billing" and on left menu choose "credits"  (OR go to aws.amazon.com/awscredits )
Redeem your AWS credit using the code on the voucher provided at the workshop

**Launching AWS virtual machine:**
 - Go to "Services" and under the "compute" heading, choose "EC2"
 - Set "region" in top-right corner to be Ireland
 - Click on "Launch Instance"
 - Select "Deep Learning AMI CUDA 8 Ubuntu Version"
 - Scroll down and select "GPU compute ... p2.xlarge"
 - Click Review and Launch
 - Click Launch
 - Choose your existing key pair (.pem) file   (Peter: maybe some instruction on how to set this up on the fly for participants who don't have it done in advance?) 

**Connecting to the launched instance:**
 - From EC2 dashboard->instances  (Need to check again how to get there from previous step!!)
 - You should see your launched instance listed
 - To connect to the instance 
   - copy public DNS(ipv4) field
   - type ssh -Y -i /path/my-key-pair.pem ubuntu@[copied-DNS]
   (you may need to type chmod 400 /path/my-key-pair.pem if your key_pair permissions are incorrect) 
(If in doubt, see also http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

Now you should be logged into the machine and see a command-line prompt $.

#### 2: Running first tutorial code
**Folder setup**
 Type the following commands to get setup for running the code:
 - mkdir -p cork_ai   *(make a new folder to work in)*
 - cd cork_ai         *(switch to the newly created folder)*
 - git clone https://github.com/CorkAI/Meetup1.git  *(this will make a Meetup1 folder with all the code/data we need)*
 - cd Meetup1     *(switch to the Meetup1 folder)*
 - vim mnist_softmax_1_basic.py  *(to read/edit the code you are about to run)*
    - (Type Esc then : then q! and hit enter to exit the file)

**Executing code**
 - Type python mnist_softmax_1_basic.py *(and wait up to 2/3 mins!)* 
 - Number printed at end (~0.92) is the accuracy of the network

**Additional exercises**  
*Additional Exercise 1:* The previous exercise tells us that we achieved 92% accuracy in classifying the MNIST handwritten digits, but we have no intuition about what is going wrong in the other 8% of test images.   In this exercise we iterate through test images one-by-one and write examples to disk of successful and failed classifications.  By viewing these examples (particularly the failed ones), we get a sense of the weaknesses of the system.
Type the following commands to run this exercise:
 - vim mnist_softmax_2_visualise.py *(to read/edit the code)*
   - (Type Esc then : then q! and hit enter to exit the file)
 - python mnist_softmax_2_visualise.py  *(and wait)*

The examples are written in sub-folder output_images in .png format with naming convention fail_[true_class]_[assigned_class].png OR success_[true_class].png
View a few of the failed/successful examples using the command below and see if the failures are 'difficult' examples
 - ls output_images *(list the created images filenames)*
 - xdg-open output_images/[filename] *(to view an image..may take a few moments to appear on your screen)*
 
*Additional Exercise 2:* Although the MNIST dataset has been a computer vision benchmark for a number of years, there have been complaints that the task is too simple to serve as a realistic performance benchmark for modern systems. In response to this Zalando created a drop-in replacement for MNIST, known as Fashion-MNIST, where each image represents an item of clothing, rather than a digit.  See https://github.com/zalandoresearch/fashion-mnist  .  The labels (classes) to be assigned in this case are : 0=T-shirt/top, 1=Trouser, 2=Pullover, 3=Dress, 4=Coat, 5=Sandal, 6=Shirt, 7=Sneaker, 8=Bag, 9=Ankle boot.   The fashion data is already on your machine, pulled from our github (see folder data/fashion).  To re-train and test the network on the Fasion-MNIST set, type the following commands:
 - python mnist_softmax_3_fashion.py
 - Number printed at the end is the accuracy of the network (~0.76)
 - Successful and failed examples are also written as in previous exercise, with prefix 'fashion' on filenames


Stopping/Terminating your instance.
If you do not object to losing your work, terminate.
If you want to save your work, choose stop, but be aware of small cost for volume storage.

