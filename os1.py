import os
import webbrowser
import random
ma1 = "https://www.youtube.com/watch?v=ywu88KEoh2g "
ma2 = "https://www.youtube.com/watch?v=kQi6TG58ehQ&pbjreload=10 "
ma3 = "https://www.youtube.com/watch?v=WG28goIw-pw "
ma4 = "https://www.youtube.com/watch?v=Ff4WI9hcjLM&pbjreload=10"
ma5 = "https://www.youtube.com/watch?v=ILbpKu9owmg"
ma_list = [ma1, ma2 , ma3, ma4 , ma5]
ma_random = random.choice(ma_list)
webbrowser.open(ma_random)
