#wap to crate a module named tempconv.in tempconv module to crate two function ctof()and ftoc().ctof()function converters tempreature from centigrade.now import tempconv modules and test ctof()and ftoc()functions.
import tempconv
#Test the ctof function 
celsius_temp=25
fahrenhiet_result=32
tempconv.ctof(celsius_temp)
print(str(celsius_temp)+"degrees celsius is"+str(fahrenheit_result)+"degrees fahreheit")
#Test the ftoc function 
fahrenhiet_temp=77
celsius_result=32
tempconv.ftoc(fahrenheit_temp)
print(str(fahrenheit_temp)+"degrees fahrenheit is"+ str(celsius_result)
+"degres celsius")

