
Installation:
```
cd ~/Desktop/daily-briefings-py/
conda create 
conda activate 
pip install -r requirements.txt
```

Running Via Flask:
```
FLASK_APP=web_app flask run
```

Running tests:
```sh
pytest

# in CI mode:
CI=true pytest
```

Obtaining data
```
To obtain the most recent data in a csv, run this google colab file: https://colab.research.google.com/drive/1SoC-q4AZak7ysHbztNMQyDCy9smHrHTo?usp=sharing. This file pulls the appropriate data from the API and creates a data frame. Because the data updates every year, I will run the google colab script every year to get the most recent dataset.
```

Running locally:
```
python -m app.college_data
```