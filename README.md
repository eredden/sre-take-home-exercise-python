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