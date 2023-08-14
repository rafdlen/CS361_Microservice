# Random Number Generator API

This application is a simple API that generates a random integer from 0 to a maximum value provided by the user.

## Endpoint

**Generate Random Number**

- Path: `/generate`
- Method: `POST`
- Request Content-Type: `application/json`
- Response Content-Type: `application/json`

### Request

The request body should be a JSON object that contains a single property:
- `max` (required): An integer that specifies the maximum value for the generated random number. It must be non-negative. If `max` is not provided, 0 will be used.

Example of request body:
```
{
"max": 10
}
```
### Response

The response is a JSON object that contains one property:
- `random_number`: A randomly generated integer from 0 to `max`.

Example of response body:
```
{
"random_number": 7
}
```

### Error Handling

In case of an invalid request, the API will respond with an error message.

Example of error response:
```
{
"error": "Invalid 'max' value. It must be non-negative."
}
```

## Local Development

To run the application locally, execute the following command in your terminal:
```
python app.py
```
The application will be available at http://localhost:5000.

## UML

![Screenshot 2023-08-14 at 16 27 23](https://github.com/rafdlen/CS361_Microservice/assets/101730999/28f7865e-a155-4700-ba9a-1d2979390f71)
