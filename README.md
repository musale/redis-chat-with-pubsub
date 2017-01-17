# redis-chat-with-pubsub
Simple CLI chat using redis pubsub module

# How to use
1. Clone this project
2. Open 3 different terminals
3. ```cd redis-chat-with-pubsub``` on all the 3 terminals
4. On the 1st terminal run ```python subscribe.py chatRoom```
5. On the 2nd termina run ```python publish John chatRoom```
    * A frozen ```Enter your message:``` appears
    * Type your message and it should appear on the terminal with ```subscribe.py``` running
6. On the 3rd terminal run ```python publish Doe chatRoom```
    * Repeat as sub section on ```5.```
7. Type ```exit``` to kill the chat windows or ```Ctrl + C```
