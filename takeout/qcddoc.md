Wang Yuchen, Shanghai Pinghe Bilingual School, Grade 11
Qi Tian, Shanghai smic School, Grade 10
# 1.Introduction  

## 1.1 background  

According to the investigation, 10 percent of who order the takeout are in danger.
The rapid evolution of the Chinese express industry has largely promote the development of the food delivery sevices in the catering industry. Thus, plenty of the new food delivery app was lauched to the market and now have owned millions of the users.  Whereas it also result in an great increase in the concerns about the security problems exist during the food delivery services process. One main type of cases that have happened for a great number is  that the deliveryman ilegally violate the users when the users pick the food from the deliveryman face to face.
 
  
One of the main reasons why users choose to order a food delivery is due to the convenience and time-saving since the it allow users to just wait for the food to come.
The common process of a user use the food delivery app to order a delivery services includes choosing items on the app, writing down the address, and waiting for the arrival of the food. The app will randomly release the delivery tasks to the deliveryman and also provide uses’ information including phone numbers, names, and the addresses.

The safety problems may occur during the process when the deliveryman give the food to the users. Those problems mostly are the violation from the deliveryman to the users, mostly come from such private environments of the transitions and the exposure of the users private information. Other problems including the food preservation and the stealing problems may also exist after the food has been delivered to the users’ ordering places.

In this project, we will specially focus on designing an high-tech receiving box which possess the techniques of the monitoring, temperature-controlling, and the anti-stealing, which would help to prevent the problems mentioned above and provide the users with a safer and more convenient food delivery experiences.

### 1.2.1 CURRENT APPROACH  

For the food delivery services, since the food cannot be stored as other normal goods, the products must be directly given to users face to face. This is because that the food tends to get metamorphism or lose its original quality. However, this face to face condition would carry out many potential dangers for both users and deliverymen. Thus, the most effective method to reduce the problems is to prevent the direct contact between the users and the deliveryman. 

The most common methods that people use to prevent the direct contact is to command deliverymen to put the products outside their doors or at the public places in their living buildings, and then go out and pick up the food after the deliverymen have left. Whereas this would also remain some potential problems. For instance, people cannot make sure that the deliverymen have really left or are still wandering nearby; the food can be stolen away; and if people don’t pick up their food immediately, the food would lose the original quality.

Currently, some buildings have already started to use the receiving boxes to help the residents store their food and products from the delivery services. Those boxes which can be locked after the products are put in can solve many problems existed

However, there are limitations to the this solution. Those, who buy food takeout have an obvious desire to not go outside and get the food, because the wheather is too harsh or they do not have the time. If the food were to be placed outside, which takes a long time walk to, the main problem is not solved. The person still has to go out. Up to this extent, a better solution seem to be very crucial and desirable. Our approach is to place a box beside the door of our user, so they do not need to walk out the door. Also, forbid the delivery man from harming our user.

## 1.3 Objective  
Our objective is to provide our comsumer the safest way to get a food takeout
<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/system.png" width="75%" height="75%">

# 2.Methodology(Hardware)  
## 2.1 OVERVIEW 
By placing a box out side the door so that the user do not need to get the takeout when the delivery is around. 
Our product can mainly be separated into three parts: frame, software, and hardware. Frame is basically the box that will contain the component. It will also protect the segments from damages by the rain and wind. Software, the most elaborated part, is where every thing else is bond together. Arduino helps with the controlling of the hardware and send data to the python code. Then the python code will work out the what will be done next and send data back for further operation. This continues in a loop. Last, the hardware has its job to collect data and display it to the user. This part consists of the output and input device. The buzzer to notify to user, the button to open the box, the insulation to keep food at its optimum temperature. Not a single part can be omitted. Now, we will be introducing you to the hardwares.

<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/diagram4.jpg" width="65%" height="65%">

| | Out black | Out red |  |  |  
| ---- | ---- | ---- | ---- | ---- |
| left | GND | 12v | heating | Red light |    
| right | 12v | GND | cooling | Green light |  

<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/hardware.png" width="70%" height="70%"> 

## 2.2 Insulation 
We found out that many might not be able to get their food on time. So we think it would be useful if the box can heat or freeze the food according to its type to store it for a long time. The Python system would get the name of the food and identify whether the food is cold or hot right after a user has commited a delivery service. Then the box would immediately start to work to either heat or cool inside. When the food arrives, the box has probably already reach the most suitable temperature inside for the food. Deliveryman just need to touch the swich to unlock the box and put the food inside. When the box has food in it, the door closes and locks in order to prevent strangers from stealing the food.

### 2.2.1 Alarm 
This device has two uses. First, as the delivery man will not knock te door, the user might not notice that the food is ready. When the Face recognition device founds out that there is no one out side the door. Then, the distance sensor checks that there is food in the box. The buzzer will buzz and the light turns on to notify the user that the food is ready and get it.
The second use is obiously to protect the user. If the face recognition detects that the delivery man is in front of the door too long, the device will predicate that he is dangerous. Furthermore, the device inform the user about the condition.

 # TBD by Yuchen, flow chart for arduino code here
<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/yuchen/%E6%B5%8B%E6%B8%A9flow%20chart%20%E6%9B%B4%E6%96%B0.png" width="45%" height="45%"> 

## 2.3 Face recognition device
In this part we used a module in pyhton called the cv2. Its main function is to identify faces in images and capture videos, using the its existing database. This device will identify the position of the delivery and provide realtime data to the display and the alarm system. This device will aid the ability of detecting if the delivery man is around. The device will locate the face and add a rectangle surrounding it. Then, a counter(able to alter at any time) is set to count the time of the delivery man in front of the door. In a normal context, a circle will appear as well as notifying the user, when the face recognition device finds the absence of the delivery man. On the contrary, if the man stands there for a long time, the alarm will be set on. An additional function will be to identify whether the person standing is a family member or not. This function will help knowing if the person is safe to the user or not. Then, the alarm would not trigger, if a family memeber is standing in front of the door. 

## 2.4 Processing  
At first, when the user has ordered the takeout, this section will track down the delivery and will also help the detection of the alarm system

<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/swflowchart.png" width="70%" height="70%"> 

## 2.5 User Interface  
Basicly, a display. This part of the product can remind the user, when the takeout is in the box and has not been taken.

# 3.RESULTS AND DISCUSSION  
## 3.1 Assessment of Graph  
<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/back.jpg" width="35%" height="35%"> 
<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/front.jpg" width="35%" height="35%"> 
<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/plan_view.jpg" width="35%" height="35%"> 
Face recognition
<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/face_recognition.png" width="35%" height="35%"> 
## 3.2 Assessment of Application  
<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/ideal_result.png" width="90%" height="90%"> 
We first laid out the ideal outcome of all situations, and tested with the box. We tested if the cooler or heater worked correctly by using a termometer.  
<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/thermometer" width="80%" height="80%"> 
The result appeared to be what we had expected.  

## 3.3 Assessment of temperature control
We record the temperature for several times after the box begin to heat or cool inside, preparing to store the food. The graphs below show how the temperature changes with the time which thus prove the temperature control of the box is effective.
<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/yuchen/%E5%8A%A0%E7%83%AD%E6%9B%B2%E7%BA%BF.png" width="70%" height="70%"> 
<img src="https://github.com/CASTIC2019/Team/blob/master/takeout/yuchen/%E9%99%8D%E6%B8%A9%E6%9B%B2%E7%BA%BF.png" width="70%" height="70%"> 

# 4.CONCLUSION  
First, we are able to get the data from the takeout website and know when is the takeout going to arrive.
Second, we have a web cam to recognize the face of the owner of the house or a stranger. By this the system is able to know when to open the lock and when to close it. 
Third, when the food is in the box, we can detect to temperature and choose to turn on the heater or the cooler.
Last, when the food is in the box the system can notify the user to get the food.
However, we still need to upgrade the system by calculating the time of the arrival and turn on the heating/cooling before hand.
So that, for example, when the ice cream arrives, the cooler is alreadily turned on and the temperature in the box is able to keep the ice-cream at its shape and no molten. 

# 5.BIBLIOGRAPHY   
[1]Eben Upton, Gareth Halfacree. Raspberry Pi User Guide. Beijing: Renminyoudian Publishing House, 2013.8. ISBN 978-7-115-32367.  
[2]Simon Monk, Programming the Raspberry Pi: Getting Started with Python. Beijing: Renminyoudian Publishing House, 2017.1 ISBN 978-7-115-44203-1  
[3]Xie Kainian, Artificial Intelligence And Maker. Shanghai: Shanghai Jiaotong University Publishing House, 2019. IBSN 978-7-313-10319-2  
