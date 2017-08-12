# Python library for PHPList REST API

## To Use

   1. `pip install -r requirements`
   2. Write your code:

      ```python
      from phplist import PHPListClient

      client = PHPListClient(URL, secret=mysecret)
      client.login(login=myusername, password=mypassword)
      output = client.lists_get()
      ```

## Run Tests

   1. `pip install nose`
   2. `nosetests tests.py`


## TODO

   * add setup.py
   * push up to pypi
