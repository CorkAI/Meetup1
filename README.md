# User Instructions 

### Full instructions for running the tutorials at Cork AI's first meetup

#### 1: AMAZON WEB SERVICES (AWS):  
**Redeeming AWS credits:**  
 - From https://aws.amazon.com/ choose "Sign in to the Console"
 - Choose "root user sign in" and enter your AWS email address and password
 - In "Services", choose "billing" and on left menu choose "credits"  (OR go to aws.amazon.com/awscredits )
Redeem your AWS credit using the code on the voucher provided at the workshop

**Launching AWS virtual machine:**
 - Go to "Services" and under the "compute" heading, choose "EC2"
 - Set "region" in top-right corner to be Ireland
 - Click on "Launch Instance"
 - Select "Deep Learning AMI (Ubuntu) Version 1.0" AMI ID: ami-1812bb61
 - Scroll down and select "GPU compute ... p2.xlarge"
 - Click "Review and Launch"
 - Click "Launch"
 - If you do not have an existing key pair, then select "Create a new key pair".  This will direct you to create and download a .pem file to your disk. Otherwise select an existing key pair. Note that you must have access to the key pair PEM file locally.
 - Click "Launch Instances"

**Connecting to the launched instance:**
 - From Services menu choose EC2
 - From EC2 dashboard->instances
 - You should see your launched instance listed
 - To connect to the instance (using linux, mac or cygwin with openSSH setup) 
   - copy public DNS(ipv4) field
   - type ```ssh -i /path/my-key-pair.pem ubuntu@[copied-DNS]```
   (you may need to type ```chmod 400 /path/my-key-pair.pem``` if your key_pair permissions are incorrect) 
(If in doubt, see also http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
 - To connect to the instance using putty, please follow directions at http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html

Now you should be logged into the machine and see a command-line prompt $.

#### 2: Running first tutorial code
**Folder setup**
 Type the following commands to get setup for running the code:
 - ```mkdir -p cork_ai```   *(make a new folder to work in)*
 - ```cd cork_ai```         *(switch to the newly created folder)*
 - ```git clone https://github.com/CorkAI/Meetup1.git```  *(this will make a Meetup1 folder with all the code/data we need)*
 - ```cd Meetup1```     *(switch to the Meetup1 folder)*
 - ```vim mnist_softmax.py```  *(to read/edit the code you are about to run)*
    - (Type Esc then : then q! and hit enter to exit the file)

**Launch conda environment**
 Our AWS machine has multiple deep-learning environments installed (conda environments).  We need to launch one so that the libraries we need (e.g. tensorflow) are ready for use:
 ```source activate tensorflow_p27```

**Executing code**
 - Type ```python mnist_softmax.py``` *(and wait up to 2/3 mins!)* 
 - Number printed at end (~0.92) is the accuracy of the network

**Additional exercises**  
*Additional Exercise 1:* The previous exercise tells us that we achieved 92% accuracy in classifying the MNIST handwritten digits, but we have no intuition about what is going wrong in the other 8% of test images.   In this exercise we iterate through test images one-by-one and write examples to disk of successful and failed classifications.  By viewing these examples (particularly the failed ones), we get a sense of the weaknesses of the system.
Type the following commands to run this exercise:
 - ```vim mnist_softmax.py``` *(to read/edit the code)*
   - (Type Esc then : then q! and hit enter to exit the file)
 - ```python mnist_softmax.py --write_samples 1```  *(and wait)*  
 
The examples are written in sub-folder output_images in .png format with naming convention fail_[true_class]_[assigned_class].png OR success_[true_class].png
View a few of the failed/successful examples using the command below and see if the failures are 'difficult' examples
 - ```ls output_images``` *(list the created images filenames)*

To download and view the images (linux, mac, cygwin) open a new shell on your local machine and create a fresh empty directory. Then copy the output images to your local system:
 - ```mkdir output_images```
 - ```cd output_images```
 - ```scp -i /path/my-key-pair.pem ubuntu@[copied-DNS]:/home/ubuntu/cork_ai/Meetup1/output_images/* .```
 - View the images using Finder / Explorer or your preferred image viewer.

To download and view the images using putty on Windows:
 - Open a command line prompt (cmd)
 - type ```pscp -i C:\path\my-key-pair.ppk ubuntu@[copied-DNS]:/home/ubuntu/cork_ai/Meetup1/output_images/* c:\[my_local_directory]```
 - View the images using your preferred image viewer

*Additional Exercise 2:* Although the MNIST dataset has been a computer vision benchmark for a number of years, there have been complaints that the task is too simple to serve as a realistic performance benchmark for modern systems. In response to this Zalando created a drop-in replacement for MNIST, known as Fashion-MNIST, where each image represents an item of clothing, rather than a digit.  See https://github.com/zalandoresearch/fashion-mnist  .  The labels (classes) to be assigned in this case are : 0=T-shirt/top, 1=Trouser, 2=Pullover, 3=Dress, 4=Coat, 5=Sandal, 6=Shirt, 7=Sneaker, 8=Bag, 9=Ankle boot.   The fashion data is already on your machine, pulled from our github (see folder data/fashion).  To re-train and test the network on the Fasion-MNIST set, type the following commands:
 - ```python mnist_softmax.py --data_dir data/fashion --write_samples 1```
 - Number printed at the end is the accuracy of the network (~0.76)
 - Successful and failed examples are also written as in previous exercise, with prefix 'fashion' on filenames
 - use the scp command to download and inspect these images

#### 3: Pizza and Beer Break  
**Please refuel before the next session :-) **

#### 4: Running second tutorial code
The second tutorial will use a convolutional neural network to solve the same tasks as previously. The code and folder setup is ready for use.  We've added some code to store the trained model on disk, so that we only need to train one time, and for any further tests we can use the trained model stored on disk.  If you want to have a look at the code before you run it please use
 - ```vim mnist_deep.py```
    - (Type Esc then : then q! and hit enter to exit the file)  

**Executing code**
 - ```python mnist_deep.py``` *(and wait)*  
 - Verify the accuracy printed at the end of the file (~99.2%)  
 - type ```ls saved_model``` to verify that a directory named saved_model has been created and contains several files (which store the network graph and parameter values)
 - type ```python mnist_deep.py``` once more to run the code again, and note that the model is restored from disk and does not need to be trained before computing accuracy.

Note that if you wish you can copy the saved_model folder to your local machine and try to test the trained model there. The compute GPU is very helpful (or almost essential) for model training but most machines can run the testing phase once the model is trained. 
 
**Additional exercises**  
*Additional Exercise 1:*  Run the stored trained convolutional network on the Fashion MNIST data
  - ```python mnist_deep.py --data_dir data/fashion```

*Additional Exercise 2:* Run the stored trained convolutional network on the (pre-prepared): handwritten digits provided
The git repository contains some manually created test images in folder extra_test_digits.
Images 1.jpg 2.jpg and 3.jpg are created from photos of handwritten digits (manipulated to be grey-scale, 28x28, white-on-black).  The original photographs are also available to view at 1_photo.jpg etc.
Images 4.jpg 5.jpg and 6.jpg are created digitally using a 28x28 black background and white 'paintbrush'.
Have a look at the images and see how closely they resemble the MNIST data (samples in your output_images folder if you have done previous additional exercises).
Now test your trained convolutional network on these images using the following commands
 - ```python mnist_deep.py --extra_test_imgs 1```
Output files are written in folder output_images with filename extra_[pred] where pred is the digit assigned by the convolutional network.  How well did the network do?!

#### 5: Ending your AWS session
When you are finished working on AWS you need to stop (or terminate) your session to discontinue usage charges.
This is **not** achieved by just logging out in the terminal!!

**Stopping/Terminating your instance.**
- From EC2 dashboard->instances 
 - You should see your launched instance listed (and selected with blue checkbox)
 - In the "Actions" drop-down menu choose "Instance State" and either "stop" or "terminate"
   - "stop" will end your session, but keep your instance and data safe for next time you want to use it (there is a very small fee for this - Chris??)
   - "terminate" will end your session and will **not** retain your data or your instance state

