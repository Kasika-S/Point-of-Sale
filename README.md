<!-- # VK API DOCUMENTATION -->

# API Documentation: User Registration

## Overview

This API endpoint is designed to handle user registration by sending an OTP (One-Time Password) to the provided phone number. The user enters their phone number, and upon successful validation, an OTP is generated, sent to the user, and saved in the database.

## Endpoint

- **URL:** `/api/account/user-registration/`
- **Method:** POST

## Request

### Body

- **phone_number** (required): User's phone number. Should be a valid phone number starting with the country code.

Example:

```json
{
  "phone_number": "+1234567890"
}
```

## Errors

### 1. Missing Phone Number

- **Status Code:** 400 Bad Request
- **Response:**
  ```json
  {
    "phone_number": [
      "This field is required."
    ]
  }
  ```

### 2. Blank Phone Number

- **Status Code:** 400 Bad Request
- **Response:**
  ```json
  {
    "phone_number": [
      "This field may not be blank."
    ]
  }
  ```

### 3. Invalid Phone Number Format

- **Status Code:** 400 Bad Request
- **Response:**
  ```json
  {
    "phone_number": [
      "Enter a valid phone number."
    ]
  }
  ```

## Success

- **Status Code:** 200 OK
- **Response:**
  ```json
  {
    "detail": "OTP sent successfully"
  }
  ```

## User Flow

1. User makes a POST request to the `/api/account/user-registration/` endpoint with their phone number in the request body.
2. The API validates the phone number.
    - If the phone number is missing or blank, it responds with an appropriate error message.
    - If the phone number is not in a valid format, it responds with an error message.
3. If the phone number is valid, an OTP is generated and sent to the user.
4. The OTP is saved to the user model in the database.
5. The API responds with a success message indicating that the OTP has been sent successfully.

## Example Usage (cURL)

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+1234567890"}' \
  http://example.com/api/account/user-registration/
```

## Example Usage (Python - requests library)

```python
import requests

url = "http://example.com/api/account/user-registration/"
data = {"phone_number": "+1234567890"}

response = requests.post(url, json=data)
print(response.json())
```
---------------------------------------------------
# API Documentation: Verify OTP and Generate Token

## Overview

This API endpoint is designed to verify the OTP (One-Time Password) provided by the user, and upon successful verification, it generates a JWT (JSON Web Token) for authentication. The JWT includes a refresh token and an access token. Additionally, it provides information about whether the user is a new member.

## Endpoint

- **URL:** `/api/account/verify-otp-and-generate-token/`
- **Method:** POST

## Request

### Body

- **phone_number** (required): User's phone number. Should be a valid phone number.
- **otp** (required): OTP received by the user. Should be a 6-character string.

Example:

```json
{
  "phone_number": "+255679190720",
  "otp": "123456"
}
```

## Errors

### 1. Invalid OTP Length

- **Status Code:** 400 Bad Request
- **Response:**
  ```json
  {
    "otp": [
      "Ensure this field has no more than 6 characters."
    ]
  }
  ```

### 2. Invalid Phone Number Format

- **Status Code:** 400 Bad Request
- **Response:**
  ```json
  {
    "phone_number": [
      "Enter a valid phone number."
    ]
  }
  ```

### 3. Invalid OTP

- **Status Code:** 400 Bad Request
- **Response:**
  ```json
  {
    "detail": "Invalid OTP"
  }
  ```

## Success

- **Status Code:** 200 OK
- **Response:**
  ```json
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "new_member": false
  }
  ```

## User Flow

1. User makes a POST request to the `/api/account/verify-otp-and-generate-token/` endpoint with their phone number and OTP in the request body.
2. The API validates the OTP and phone number.
    - If the OTP is not in a valid format, it responds with an error message.
    - If the phone number is not in a valid format, it responds with an error message.
3. If the OTP and phone number are valid, the API checks if the OTP matches the stored OTP for the user.
    - If the OTP is valid, the user's OTP is cleared, and a JWT token is generated.
    - If the OTP is invalid, it responds with an error message.
4. The API responds with the generated JWT token and indicates whether the user is a new member.

## Example Usage (cURL)

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+255679190720", "otp": "123456"}' \
  http://example.com/api/account/verify-otp-and-generate-token/
```

## Example Usage (Python - requests library)

```python
import requests

url = "http://example.com/api/account/verify-otp-and-generate-token/"
data = {"phone_number": "+255679190720", "otp": "123456"}

response = requests.post(url, json=data)
print(response.json())
```
------------------------------------------------------------
# API Documentation: Update User Profile

## Overview

This API endpoint allows authenticated users to update their profile information. Users can make a PATCH request to update specific fields in their profile. The endpoint requires authentication, ensuring that only authenticated users can modify their profiles.

## Endpoint

- **URL:** `/api/profile/update/`
- **Method:** PATCH
- **Authentication:** Bearer Token

## Request

### Body

The request body should contain the fields that the user wants to update.

Example:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "gender": 1,
  "avatar": (binary file),
  "marital_status": 2,
  "street": "123 Main Street"
  // Include other fields as needed
}
```

### Fields
- **first_name, middle_name, last_name:** User's names.
- **phone_number:** User's phone number.
- **nida_number:** User's National Identification Number.
- **birth_date:** User's date of birth (string representing a date).
- **marital_status:** User's marital status (integer).
- **gender:** User's gender (integer).
- **job:** User's job.
- **region:** User's region.
- **street:** User's street address.
- **house:** User's house number.
- **avatar:** User's avatar image (binary file).
- **national_identification:** User's national identification document (binary file).
- **letter:** User's letter document (binary file).

## Errors

### 1. Field Validation Errors

- **Status Code:** 400 Bad Request
- **Response:**
  ```json
  {
    "field_name": ["Error message 1", "Error message 2", ...]
  }
  ```

### 2. File Type Validation Error

- **Status Code:** 400 Bad Request
- **Response:**
  ```json
  {
    "field_name": ["Invalid file type. Allowed types are JPEG and PNG."]
  }
  ```

### 3. File Size Validation Error

- **Status Code:** 400 Bad Request
- **Response:**
  ```json
  {
    "field_name": ["File size exceeds the maximum allowed size (5 MB)."]
  }
  ```

### 4. Null Field Validation Error

- **Status Code:** 400 Bad Request
- **Response:**
  ```json
  {
    "field_name": ["Field cannot be null."]
  }
  ```

## Success

- **Status Code:** 200 OK
- **Response:**
  ```json
  {
    "message": "Profile updated successfully"
  }
  ```

## User Flow

1. Authenticated user makes a PATCH request to the `/api/profile/update/` endpoint with the desired fields in the request body.
2. The API validates the fields based on their types and specific rules.
    - If there are validation errors, the API responds with detailed error messages.
3. If the validation is successful, the API updates the user's profile information.
4. The API responds with a success message indicating that the profile has been updated successfully.

## Example Usage (cURL)

```bash
curl -X PATCH \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{"first_name": "John", "last_name": "Doe", "gender": 1, "avatar": (binary file), "marital_status": 2, "street": "123 Main Street"}' \
  http://example.com/api/profile/update/
```

## Example Usage (Python - requests library)

```python
import requests

url = "http://example.com/api/profile/update/"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": 1,
    "avatar": (binary file),
    "marital_status": 2,
    "street": "123 Main Street"
}
response = requests.patch(url, headers=headers, json=data)
print(response.json())
```
