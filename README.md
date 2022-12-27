# Computer-Olympiad
## Programming practice: list of computer olympiad's accepted candidates

Ahmad is sending the final list of the names of those accepted to the Computer Olympiad to the results review committee so that the committee can print the entry cards for the final competitions, but because a specific format was not defined for registering the names during the test, the participants did not write their names in the standard format; besides, the programming language with which they participated in the competition is written in the continuation of each name, and the gender of the people is also specified at the beginning of each name. The standard form of names is that the first letter of the name is uppercase and the rest of the letters of the name are lowercase. 

Write a program that reads the number, name, gender, and programming language of the accepted candidates from the input and separates the names based on their gender, standardizes them, and writes the programming language in front of each name with which they participated in the competition. (In the output, the female gender should be printed first and then the male gender. The names of each gender should be printed in the order of the English alphabet.)

Note: If you plan to use the dictionary to solve your problems, note that the dictionary does not maintain the order.

Example input:
```
4  
m.hosSein.python  
f.miNa.C  
m.aHMad.C++  
f.Sara.java
```
Example output:
```
f Mina C  
f Sara java  
m Ahmad C++  
m Hossein python
```
