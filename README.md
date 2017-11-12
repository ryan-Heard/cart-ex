# cart-ex
Simple Discount Cart

<h2>Steps to run</h2>
<ol>
<li>go to docker-machine and run git cloone https://github.com/ryan-Heard/cart-ex.git</li>
<li>Enter cart-ex directory "cd cart-ex"</li>
<li>Enter "docker built -t pyapp ." note that pyapp can be replaced with any name</li>
<li>To run the program type "docker run -it pyapp"</li>
<li>From here you are able to use the cart. It should follow all the rules laid out in the game<br></li>
</ol>


<h2>Notes</h2>
1) The .5 bags rule is ambigous. I have have applied so that it can stack with the APPL rule<br><br>

<h2>Improvement:</h2>
<ol>
<li>If I had time I would have set up a db to pull these things from. I would have loved to add a feature that has dates so that the cart would prefrom normal when the features become invalid</li>
<li>UI is simple but making it into a full blown webapp could give the interface more graphics. </li>
</ol>
