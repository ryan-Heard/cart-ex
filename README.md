# cart-ex
Simple Discount Cart

Steps to run
1)go to docker-machine and run git cloone https://github.com/ryan-Heard/cart-ex.git
2)Enter cart-ex directory "cd cart-ex"
3)Enter "docker built -t pyapp ." note that pyapp can be replaced with any name
4)To run the program type "docker run -it pyapp"
5)From here you are able to use the cart. It should follow all the rules laid out in the game

Notes
1) The .5 bags rule is ambigous. I have have applied so tha it can stack with the APPL rule

Improvement:
1)If I had time I would have set up a db to pull these things from. I would have loved to add a feature that has dates so that the cart would prefrom normal when the features become invalid
2)UI is simple but making it into a full blown webapp could give the interface more graphics. 
