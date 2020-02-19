# twitch-ai

Get your token at : https://twitchapps.com/tmi/

# Live Scrapping: 

## For the JS version : 

* Download node.js : https://nodejs.org/en/
* Install tmi : ```npm install tmi.js```
* Run with node : ```node <name_file>.js```

## For the Python version : 

* Download json and twitch : 
```
pip3 install --user twitch-python
```
* Run with ```python3 name_file.py```

# VOD Scrapping: 

* You can use tcd with : ```pip3 install tcd```

and then :

```
tcd --video 547405190 --format irc --output ~/Desktop --client-id <>
```

by getting a client_id from twitch dev. 

You will receive the chat in a .log format. You can then transcript this log file into a csv using ```/python/log_to_csv.py```
and :
```
python3 log_to_csv.py --log_path 'sardo_live_nocturne.log' \
                      --csv_path 'sardo_live_nocturne.csv'
```
