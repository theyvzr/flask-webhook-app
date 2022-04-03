# Application Development

## About the App
 
- The application has 3 endpoints:

    1. /healthcheck
    
        * It is a simple healthcheck endpoint.

            * http://0.0.0.0:port/healthcheck

    2. /whoami
 
        * The related endpoint accepts http request only with GET method.
        * Returns the values of the "firstname" and "lastname" parameters to the user in JSON format.
        
            * http://0.0.0.0:port/whoami
 
    3. /alert
    
        * The related endpoint only accepts http request with POST method.
        * Incoming data to this endpoint is processed only if it is in JSON format.
        * It sends the incoming JSON object to https://webhook.site.

## About the Config File:

- We can think of the config file as the file where we make the configuration settings inside the application.
  It makes the project we are working on more functional by entering information such as port, host, key etc.
  In addition, this functionality provides many advantages for anyone who will be working on the application.

- The config file in this API contains the host, port, log file, log level and webhook url information.

- Example python.cfg file:

  [[APPSERVER]]
  
  host = "0.0.0.0"
  port = 80
  
  [[LOGGING]]
  
  log_file = app.log
  log_level = ERROR
  
  [[WEBHOOK]]
  
  webhook_url = https://webhook.site/example123
  
## Kaynaklar

- https://pypi.org/project/Flask/
- https://pypi.org/project/requests/
- https://pypi.org/project/configparser/
- https://docs.webhook.site/index.html# flask-webhook-app
