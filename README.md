# Web-scaper

Script to scape all rental appartment information from [HuizenZoeker.nl](https://www.huizenzoeker.nl) (city, postal code, size, number of rooms, price) for all Dutch student cities. I have made this program for a school project.

You can process the resulting .json file from this program to calculate the dictance from the postal code to the center of the city the appatment is in and convert the .json to .csv for further processing using my other project [Web-scaper-geocoding](https://github.com/bob-swinkels/Web-scraper-geocoding).

---
**DISCLAIMER:**

**The author and all contributors DO NOT Promote or encourage any illegal activities, all information provided by this repository is meant for EDUCATIONAL PURPOSE only.** **There may be legal charges for using this software depending on the country you are in.**

---

## Installation
### Requirements
* Python 3.3 and up
* PyPI

## Usage
Make sure the [proxies.txt](appartment\appartment\proxies.txt) file is up to date with working proxies, any number is fine as long as they are working. More is faster. You can get proxies for free from [free-proxy-list.net](https://free-proxy-list.net/) or any other proxy site you like.
Move into the appartment folder and start the crawler with in JSON output mode.
```
$ scrapy crawl appartment -o appartment-list.json -t json
```

## Development
Clone the project and move into the project head directory using the ```cd``` command. Then create a virtual environment in the head directory of the project, activate this environment and run ```pip install -r requirements.txt```.
```
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Thanks to **Paula Wabeke** for het creative input, and effective problem-solving during the creation of this program.

## License
[MIT](LICENSE)