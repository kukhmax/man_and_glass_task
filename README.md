## Task:

  It is necessary to implement the interaction of the classes Man and Bottle,<br>
  which describes the process of drinking liquid, taking into account the state of its volume for both objects,<br>
  and also expand this interaction using the intermediate class controller and interfaces for objects in order to expand them,<br>
  for example: Man -> Cat, Glass - > bowl and so on, don't forget to validate input parameters.<br><br>
  
  Please use MVC pattern and SOLID principal

  ## Run script
  `poetry install`
  `poetry run python3 man_and_glass/main.py`

  ## Output example

  `Man can drink 1000 ml liquid<br>
Enter the amount of liquid in glass, please<br>
400<br>
Volume exceeds the required 200 ml<br>
Enter the amount of liquid in glass, please<br>
200<br>
Enter the amout of liquid to drink<br>
30<br>
Man can drink 970 liquid<br>
There is 170 ml of liquid left in the glass`<br>
