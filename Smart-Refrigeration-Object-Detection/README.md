# OBJECT RECOGNITION/ SMART REFRIGERATOR
CNN based food recognition using Keras in Python 

Working Project on https://github.com/PMILINDA/ObjectDetection-SmartRefrigerator



### ABSTRACT
Some portion of what makes getting in shape so troublesome is that checking calories is a vague science at best. Eating food without knowledge of its composition and nutritional contents prompts poor processing leading to poor health.  Each time you convey nourishment from the device it indeed, even with nutritious data, one needs to screen serving sizes, people are continually searching for approaches to enhance their health and wellbeing. The typical procedure of getting nutritional data is by utilizing google or utilizing some applications. In this paper, we have proposed a system which is portable, handy, needs less space and power, fast, is more proficient and simple. The Smart Refrigerator system is able to remotely alert the user about the scarce contents, expiry date and nutritional values. The Internet of Things (IoT) refers to the coordination of devices and systems that interconnect real world sensors and actuators to the Internet. This paper presents the abstraction, architecture, interfacing and functionality of such a device that incorporates the systems stated above: a system that interacts with objects of concern, gathers information about them, process this information into relevant data with the help of a dataset that is later conveyed to the user via an IOT platform.

In this project , we made a food recognition and calorie estimation system that uses the images of the food, given by the user, to recognize food item and then estimates the calorie present in same food item. Food image recognition is one of the promising applications of visual object recognition in computer vision. 
The system uses image processing and computational intelligence for food item recognition. 
We trained a large, deep convolutional neural network to classify the 1000 high-resolution images of each category.

### CONVOLUTIONAL NEURAL NETWORKS

The Convolutional Neural Network (CNN) oﬀers a technique for many general image classiﬁcation problems. It has been applied in food classiﬁcation and resulted in a high accuracy.CNN is widely used in food recognition and provides better performance than the conventional methods.
Over the last few years, due to the advancements in the deep learning, especially in the convolutional neural networks, the accuracy in identifying and recognizing images has been increased drastically. This is not only because larger datasets but also new algorithms and improved deep architectures. Convolutional Neural Network (CNN) is also known as LeNet due to its inventor.CNN mainly comprises convolutional layers, pooling layers and sub-sampling layers followed by fully-connected layers. The very ﬁrst architecture of CNN takes an input image and applies convolution followed by sub-sampling. After two such computations, the data is fed into the fully connected neural network,where it performs the classiﬁcation task. The main advantage of CNN is the ability to learn the high-level eﬃcient features and in addition to that, it is robust against small rotations and shifts.


#### FOOD 101 DATASET

The dataset contains a number of different subsets of the full food-101 data. For this reason the data includes massively downscaled versions of the images to enable quick tests. The data has been reformatted as HDF5 and specifically Keras HDF5Matrix which allows them to be easily read in. The file names indicate the contents of the file.There are 101 categories represented, with 1000 images, and most have a resolution of around 512x512x3 (RGB, uint8).
We have used 15 categories in our project. They are Apple Pie, Club Sandwich, Grilled Cheese Sandwich, Tacos, Hamburger, Samosa, French Fries, Pizza, Ravioli, Cake, Spring Rolls, donuts, waffles, sushi, nachos.

### PACKAGES  USED

(i) KERAS
(ii) SHINY
(iii) SHINYJS
(iv)  DEVTOOLS

### SOFTWARE ESSENTIALS

Output from Load Cell sensor - The output from the Load Cell Sensor is taken through Raspberry Pi and stored in a text file. A python program fetches the new values and compares it with the threshold value.
Output form Pi camera - The camera captures a still when the user pushes the button. The Raspberry Pi saves the still as SHOWN IN tOMATO.PNG the image captured.
Machine Learning model - The image is then given to the machine learning model. We have used a pre-trained ImageNet model for classification of photos using an ImageNet image classifier which was trained on thousands of images of food items and can predict the food item.
Database - We have used a simple offline database stored in a .csv file. Which is updated weekly to widen the range and update all the data. The .csv file which holds the important data like key, item name, expiration date and nutrients. The output from the machine learning model is then compared with the database and the corresponding information is fetched by the program.
Twilio API - It is an free online SMS API which helps in sending customizable SMS messages to users' smartphones. The program then uses the fetched data to send it to the user.


### MODEL ARCHITECTURE
  
The proposed system can track food items in our refrigerator which helps us to collect data about them. This in turn will help to track our food habits and control how much and when we eat. We can plan our balanced diets using this data. Expiration date notifications will help reduce food wastage.We have used components like sensors and modules which make it possible to monitor food items

The first layer is the Convolutional 2D layer which consists of 32 kernels of size 3x3 taking an input of size 100x100x3 where 100x100 is the rescaled size of our images and 3 denotes the color aspect (RGB) of the image.
The next layer is the max pooling layer with a pool size of 2x2.
The above two layers are again repeated to get better filtered convolved images and better feature extraction by the max pooling layer.
The above layers have been repeated one last time where the kernels have been increased from 32 to 64 to get more filtered images for the fully connected layers.
Two fully connected layers are used next with 128 and 90 neurons respectively and Dropouts have been added of 0.01 in between the dense layers to prevent overfitting by making the weights of some random neurons to zero so as to prevent overfitting on some particular neurons.
All the convolutional 2D layers and the fully connected layers have an activation function of ReLu (Rectified Linear Unit).
The last layer is the output layer consisting of 15 neurons equivalent to the number of categories and each neuron has an output of a probability corresponding to that particular neuron. The CNN predicts the category to be the one with the highest probability.

### RESULT
The goal of the proposed architecture is to enhance the sustainability of IoT applications by exploiting smart and reliable (networks of) things and by being able to utilize a big number of heterogeneous device platforms. The proposed architecture enables the development of an environment for IoT applications through cross-platform channels that incorporate technologies for Data, Information, Things and Decentralized Management .As briefly described previously at a conceptual level, the proposed system's workflow is as follows. The Load cell sensor and camera module work in tandem to help find out what is the status of quantity of a particular item. And use the database to retrieve the data according to the output of the previous operation and send corresponding data to the user’s smartphone using Twilio SMS API.
We have achieved the desirable result from the image detection from the classifier. The Fig. tomato shows the result of the image detected and executes the command to send a message. 
 

Conclusion
With the help of sensors like the Load cell sensor and Pi camera we were able to gather data from a food item such as its weight and what it is. We were able to process this data with the Raspberry Pi and with the help of a pre-trained Machine Learning model which compares the data with the preloaded database, further it can send SMS notifications about item type, expiration and nutritional information of the food item. This unique method will lead to relatively accurate results to track nutrition and keep a track of food items. Our results will show that the accuracy of our system is acceptable and it will greatly improve and facilitate current manual nutrition measurement techniques. Further improvements to the project would be adding the option to place orders for food items from the reply itself, suggesting recipes with the contents present in the fridge, add more sensors to gather more data about different parameters and to use them to our benefit.
The existing systems use different kinds of sensors which collect information like temperature, humidity, color of food item to recognise food items etc but they miss out on recognizing the food item exactly and using this information to our benefit. The system which we have proposed collects two types of data about a food item i.e. food item name and weight. This system uses pre-existing resources to work with which helps in making the process fast and efficient. Existing systems use Android application integration to get notifications from the fridge but in our system we have used an SMS API. This is an advantage as we can receive notification in places where there is a network but no internet and it doesn't need application integration as we have messaging applications pre installed in our smartphones. The hardware is cheap ,portable and can be accessed remotely. As the system is connected to wifi and connected to the internet, we can update databases and improve the machine learning model time to time.

By the application of various machine learning algorithms (Support Vector Machines, K-Nearest Neighbour, Random Forest Classification) and deep learning algorithm(Convolutional Neural Networks) on the image classification problem, it is concluded that CNN is the most viable method for the image classification on our dataset in terms of both speed and accuracy and that CNN performs best in the cases of large datasets.
The accuracy obtained on training set is 86% and on the test set is 80%


### FUTURE  WORK  SCOPE

(i) More categories can be added into the model and make the classifier predict on a wider variety of different food items.

(ii) Can recognize multiple count food items in the same meal, such as hamburgers and cakes on the same dish, to estimate the calories of the meal in a more efficient manner.

(iii) Can make the platform more custom based for different users, by learning from different users their preferred food categories and making suggestions for different restaurants or any eating place for the same.


### REFRENCES

Nikhil Kakade, Prof. (Dr.) S.D. Lokhande,” IoT based Intelligent home using Smart Devices”,   International Journal of Innovative Research in 	Computer and Communication Engineering, vol. 4, Issue 6, June 2016.

Deepti Singh, Preet  Jain, “IoT Based Smart Refrigerator System”, International Journal of Advanced Research in Electronics and 		Communication Engineering (IJARECE), Volume 5, Issue 7, July 2016.		

Emily Moin, “Smart Refrigerator for Grocery Management”, Technical Disclosure Commons,   Defensive Publication Series, May 05,2015.

Folasade Osisanwo, Shade Kuyoro, and Oludele Awodele,” Internet Refrigerator”,3rd International Conference on Advances in Engineering 	Sciences & Applied Mathematics (ICAESM 2015) March  23-24, 2015.

Shama Mubeena, N. Swati,” The Design and Implementation of a Wi-Fi Based User- Machine   -Interacted Refrigerator”,  ISSN 2319-8885, 	Vol.06, Issue.14, April-2017.

B. Ramesh, J. Lingaiah,”  Raspberry Pi Based Interactive Home Automation System through  E-Mail”, International journal of Innovative 	Technologies ISSN 2321-8665, Vol.04, Issue.15, October-2016.

Jessica Tran, Jordan Gilles, Ryan Mann, and Vishnu Murthy, “Automated Demand Response Refrigerator Project”, CE 186, OCTOBER 2015.
 
Soundhar Ganesh S, Venkatesh S, Vidhyasagar P, Maragatha Raj S, “Raspberry Pi Based   Interactive  Home Automation System through 	Internet of Things”, International Journal for Research in Applied Science & Engineering Technology (IJRASET), Volume 3 	Issue III, March 2015.

Carson Kai-Sang Leung, Richard Kyle MacKinnon and Yang Wang, “A Machine Learning Approach for  Stock Price Prediction”, University 	of Manitoba, Winnipeg, MB, Canada. Vol 2, Issue II, July 2016

Prapulla S B, Dr. Shobha G and Dr. Thanuja T C, “SMART REFRIGERATOR USING  INTERNET OF THINGS”  Journal of 		Multidisciplinary Engineering Science and Technology (JMEST) ISSN: 3159-0040 Vol.2 Issue 7, July – 2015.  

A. Alheraish, “Design and implementation of home automation system”, IEEE Trans. Consumer Electronics, vol. 50, no. 4. Pp.1087–1092, 	2004.

Sarthak Jain, Anant  Vaibhav,  Lovely Goyal Student member, IEEE, “Raspberry Pi based Interactive Home Automation System through 	E-mail”, International Conference on Reliability, Optimization   and   Information Technology -ICROIT 2014.

Hsin-Han Wu, Yung-Ting Chuang, “Low-Cost Refrigerator”, Edge Computing (EDGE), 2017  IEEE International Conference on.

Poonam B. Patil, Roopali R. Patil, Swati V. Patil,” Home  Automation System using Android and Arduino Board”, International Journal  of  	Innovative Research  in  Science and Engineering Technology, Vol.5, Issue 4,April 2016.

Surinder Kaur, Rashmi Singh, NehaKhairwal and Pratyk Jain,” HOME AUTOMATION AND SECURITY SYSTEM”, Advanced 		ComputationalIntelligence: An International Journal (ACII), Vol.3, No.3, July 2016.

Nishchol Mishra,  Dr. Sanjay  Silakari,“Predictive Analytics: A Survey, Trends,Applications, Opportunities & Challenges”, (IJCSIT) 
International Journal of Computer Science and Information Technologies, Vol. 3 (3), 2012, 4434- 4438.

M.P. Sathish, Dr. S.A.K. Jilani, Mr. D.Girish Kumar, “Home Automation through EMail using Raspberry Pi”, InternationalJournal of 
Advanced Research in Electronics And Communication Engineering(IJARECE)  Volume 4,  Issue 9, September 2015.

Rajendra Banjade, Suraj Maharjan,”Product recommendations using linear predictive modeling”, Internet (AH-ICI),2011 Second Asian 
Himalayas International Conference, 4-6 Nov. 2011.

Ravi Kishore  Kodali, Vishal Jain, "Iot Based  smart  security  and  home  automation system", Computing, Communication and Automation
 (ICCCA), 2016 International Conference on.
 
Sharon  Panth,  Mahesh  Jivani  “HomeAutomation System (HAS) using Android for Mobile Phone”, International Journal of Electronics and 
Computer Science.

https://arxiv.org/ftp/arxiv/papers/0802/0802.2411.pdf

https://ieeexplore.ieee.org/document/6123373/?reload=true

https://medium.com/@Synced/deep-learning-based-food-calorie-estimation-method-in-dietary-assessment-1e76a2acee7

https://shiny.rstudio.com

https://www.researchgate.net/publication/311370165_Food_Image_Recognition_by_Using_Convolutional_Neural_Networks_CNNs

https://www.kaggle.com/kmader/food41/data

