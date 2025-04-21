# Fetch Take Home Exercise

## Description

This program iteratively checks the health of endpoints supplied by a YAML file in 15 second increments and logs the results to the console. Endpoints must respond with a status code within the range 200-299 and respond within 500ms to qualify as available.

## Setup

With the assumption that you already have [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your system and accessible through your PATH, you can clone this repository to your machine by executing the following in a command-line interface like Windows PowerShell or a Bash shell:
```
git clone https://github.com/eredden/sre-take-home-exercise-python
```

This will download the repository into the present working directory that the command-line interface is running in. Once you have done this, you will want to configure a YAML configuration file containing the endpoints which you would like to check the availability of. For each YAML document (i.e. each endpoint) within the YAML file, you should specify the following values:

- *name* (string, required): A free-text name to describe the HTTP endpoint.
- *url* (string, required): The URL of the HTTP endpoint.
- *method* (string, optional): The HTTP method of the endpoint. Defaults to GET if no value is supplied.
- *headers* (dictionary, optional): The HTTP headers to include in the request. Defaults to supplying no headers is no value is supplied.
- *body* (string, optional): The HTTP body to include the request. Must be JSON encoded. Defaults to an empty body if no value is supplied.

An example of a valid YAML-formatted endpoint is provided below:
```
- body: "{}"
  headers:
    content-type: application/json
  method: POST
  name: sample body down
  url: https://dev-sre-take-home-exercise-rubric.us-east-1.recruiting-public.fetchrewards.com/body
```

## Usage

Prior to running this program, download its dependencies by running the following from the root directory of the repository:
```
pip install -r requirements.txt
```

Once you navigate down to the `src` directory, you may execute this program by running the following in a command-line interface of your choice with [Python installed](https://wiki.python.org/moin/BeginnersGuide/Download) and on the PATH:
```
python monitor.py <config_file_path>
```

## Challenges

Throughout the process of transforming the initial codebase, I encountered multiple technical challenges which I will document below. These challenges are recorded in chronological order below.

1. When initally running the `main.py` script, I encountered an error regarding the `yaml` module not being imported. I confirmed that the script relied upon two modules which were not included in the Python standard library: `yaml` and `requests`. To resolve this issue, I added a `requirements.txt` file which can be used with `pip` to make sure you have all the dependencies you need. 
*See commit `4bf83a`.*
2. This project was initially provided without a `README.md` file, so I created the document you are reading now! I hope that my format is pleasurable to your eyes. *See commit `4835f2`.*
3. Running the `main.py` script initially yielded a failure due to a method not being provided in the YAML document for the second endpoint. I added a conditional statement which sets the method variable of an endpoint to `"GET"` if it is not explicitly defined in the YAML document. *See commits `7590f3`, `7416a6`.*
4. With the growing number of unorganized files, I created the `docs` and `src` directories to segregate various pieces of this software artifact. *See commit `2a4231`.*
5. The `check_health()` function did not initially check the response time of endpoint replies to our requests, so requests over 500ms could have feasibly passed this check. I found that Python requests have a property called `elapsed` which contains the time delta between when the request was sent and replied to. I added an `and` clause and a condition for checking if the time delta was less than 500ms to the existing conditional statement for HTTP status codes. *See commit `0a7fc45`.*
6. I adjusted the `requests.request()` function to use the data parameter rather than the json parameter for passing the payload for POST requests. This fixed an issue where the first test case for the known-good POST request would fail with HTTP code 422. *See commit `unknown yet`.*