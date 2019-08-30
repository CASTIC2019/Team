# 1.Introduction  

## 1.1 background  

According to the investigation 10 percent of who order the takeout are in danger
The rapid evolution of the Chinese express industry has largely promote the development of the food delivery sevices in the catering industry. 
Thus, plenty of the new food delivery app was lauched to the market and now have owned millions of the users.  
(data)  
Whereas it also result in an increase in the concerns about the security problems exist during the food delivery services process.  
(data)  
  
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

![Aaron Swartz](https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/system.png)
# 2.Methodology(Hardware)  
## 2.1 OVERVIEW 
By placing a box out side the door so that the user do not need to get the takeout when the delivery is around. 
Our product can mainly be separated into three parts: frame, software, and hardware. Frame is basically the box that will contain the component. It will also protect the segments from damages by the rain and wind. Software, the most elaborated part, is where every thing else is bond together. Arduino helps with the controlling of the hardware and send data to the python code. Then the python code will work out the what will be done next and send data back for further operation. This continues in a loop. Last, the hardware has its job to collect data and display it to the user. This part consists of the output and input device. The buzzer to notify to user, the button to open the box, the insulation to keep food at its optimum temperature. Not a single part can be omitted. Now, we will be introducing you to the hardwares.

![Aaron Swartz](https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/diagram4.jpg)

![Aaron Swartz](https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/hardware.png)

## 2.2 Insulation 
We found out that many might not be able to get their food on time. So we think it might be a good idea to make two seperate space, one cold and one hot as many might also buy a drink or ice-cream with their food. Envision, putting a cold drink on a heating element or putting warm food into a refrigerator. spoiling the food! The device will identify which section, heating element or refrigerator, is needed for the difference in food. Then merely open the section needed so there is less waste of energy. When the box has food in it, the door closes and locks in order to prevent strangers from stealing the food.

### 2.2.1 Alarm 
This device has two uses. First, as the delivery man will not knock te door, the user might not notice that the food is ready. When the Face recognition device founds out that there is no one out side the door. Then, the distance sensor checks that there is food in the box. The buzzer will buzz and the light turns on to notify the user that the food is ready and get it.
The second use is obiously to protect the user. If the face recognition detects that the delivery man is in front of the door too long, the device will predicate that he is dangerous. Furthermore, the device inform the user about the condition.

 # TBD by Yuchen, flow chart for arduino code here
![Aaron Swartz](https://github.com/CASTIC2019/Team/blob/master/takeout/yuchen/flow%20chart.png)

## 2.3 Face recognition device
In this part we used a module in pyhton called the cv2. Its main function is to identify faces in images and capture videos, using the its existing database. This device will identify the position of the delivery and provide realtime data to the display and the alarm system. This device will aid the ability of detecting if the delivery man is around. The device will locate the face and add a rectangle surrounding it. Then, a counter(able to alter at any time) is set to count the time of the delivery man in front of the door. In a normal context, a circle will appear as well as notifying the user, when the face recognition device finds the absence of the delivery man. On the contrary, if the man stands there for a long time, the alarm will be set on. An additional function will be to identify whether the person standing is a family member or not. This function will help knowing if the person is safe to the user or not. Then, the alarm would not trigger, if a family memeber is standing in front of the door. 

## 2.4 Processing  
At first, when the user has ordered the takeout, this section will track down the delivery and will also help the detection of the alarm system

![Aaron Swartz](https://github.com/CASTIC2019/Team/blob/master/takeout/qitian/swflowchart.png)

## 2.5 User Interface  
Basicly, a display. This part of the product can remind the user, when the takeout is in the box and has not been taken.

# 3.RESULTS AND DISCUSSION  
## 3.1 Assessment of Graph  
Face recognition
automatic lock

## 3.2 Assessment of Application  
Our main targets are the young generations as their parents has concerns over their safty as well as they might not be able to protect themselves.

# 4.CONCLUSION  

# 5.BIBLIOGRAPHY   
