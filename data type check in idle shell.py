Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1=10
>>> type(num1)
<class 'int'>
>>> num2=7.71
>>> type(num2)
<class 'float'>
>>> r=range(1,100)
>>> type(r)
<class 'range'>
>>> A=[1,12,1.2,'RAKESH',"ACHANTA"]
>>> type(A)
<class 'list'>
>>> B=(1,12,1.2,'RAKESH',"ACHANTA")
>>> type(B)
<class 'tuple'>
>>> X='RAKESH'
>>> type(X)
<class 'str'>
>>> Y="ACHANTA"
>>> type(Y)
<class 'str'>
>>> Z='RAKESH',"ACHANTA
SyntaxError: EOL while scanning string literal
>>> Z='RAKESH',"ACHANTA"
>>> type(Z)
<class 'tuple'>
>>> sett={1,2,3,}
>>> type(sett)
<class 'set'>
>>> z
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> Z
('RAKESH', 'ACHANTA')
>>> 