# fansite-analytics-challenge
This Repository is created by Gang Huang for the fan site analytics challenge from Insight Data

# Overview
This programming is written by Python. All four tasks are completed in a single program.

# Algorithms
At the beginning, the program decodes the `log.txt` by regular expression.
1. Using `Counter().most_common(10)` in Python to get the 10 most active hosts/IP and write them to a file called `hosts.txt`.
2. To identify the top 10 resources. I create a dictionary to record the bandwidth. The key of the dictionary is hosts/IP. The corresponding values are the bandwidth calculated by the bytes and the frenquency.
3. I use two pointers algorithm to complement Feature 3. That is, `p1` is the beginning of each 60-minute window. `p2` is the end of that window. To the next iteration, we just need do tiny modifications for `p1`, `p2`, instead of searching all the messages. In each iteration, counting the number of actions in each 60-minute window, if the number is bigger than the lowest value in the previous 10 busiest 60-minutes periods, just let the current record into the list of 10 busiest periods and the record with loweast value out.
4. In task 4, I create a dictionary to record all potential failed login. the key is still the hosts/IP, the corresponding value is a list with 3 elements that are the past consecutive failed login datetimes. If the difference of the third and the first elements are less than 20 seconds, just output the "trigger". If there appears a successful login, just delect the corresponding host/IP from the dictionary. If it is the first failed login of a host/IP, just initialize the value with [`past`,`past`,current_time], where `past` is just a moment before the first timestamp. After we get all the potential "triggers", we need check if anyone new one is covered by the old one within 5 minutes screen.
