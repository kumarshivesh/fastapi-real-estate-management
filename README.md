# Worko API Application

This project is a web application for managing real estate properties using FastAPI and PostgreSQL. The application allows users to add, update, delete, and fetch properties, each belonging to a specific locality.

## Features

- Add new properties with details such as property name, locality, and owner name.
- Fetch all properties within a specified locality.
- Update property details.
- Delete property records.
- Fetch all localities.

## Technologies Used

- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn
- Pydantic
- Python-dotenv

## Prerequisites

- Python 3.8 or higher
- PostgreSQL

## Getting Started

Follow these steps to clone and run the application locally.

### 1. Clone the Repository

```bash
git clone https://github.com/kumarshivesh/node-real-estate-management.git
cd node-real-estate-management
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory of the project and add the following:

```bash
DATABASE_URL=postgres://myuser:mypassword@localhost:5432/real_estate
PORT=3000
```


### 4. Run the Application

Start the development server.

```bash
npm start
```

## App Demo

Refer this YouTube video for App demo

[![RESTful API Demo](https://i.ibb.co/sHwK1VD/node-rem-thumbnail.png)](https://youtu.be/wrsCoRv-CnI)

Here are the next steps you can take to test your API and ensure everything is working correctly:


### 1. Add New Property API

1. Open Postman and create a new request.
2. Select the Method: Choose `POST` from the dropdown menu.
3. Enter the URL: Type http://localhost:3000/api/properties/add into the URL field. 
4. Select `Body` as `raw (JSON)`. Paste the follwing in the `Body`:
```
{
    "property_name": "Example8 Property",
    "locality": "Example8 Locality",
    "owner_name": "Example8 Owner"
}
```
5. Send the Request: Click the "Send" button.
6. View the Response: Verify the response.

### 2. Fetch All Properties API

1. Open Postman and create a new request.
2. Select the Method: Choose `GET` from the dropdown menu.
3. Enter the URL: Type http://localhost:3000/api/properties/fetch?locality_id=property_id into the URL field. Replace `property_id` with an actual property_id. 
4. Select `Body` as `none`.
5. Send the Request: Click the "Send" button.
6. View the Response: Verify the response.

### 3. Update Property Details API

1. Open Postman and create a new request.
2. Select the Method: Choose `PUT` from the dropdown menu.
3. Enter the URL: Type http://localhost:3000/api/properties/update into the URL field.
4. Select `Body` as `raw (JSON)`. Paste the follwing in the `Body`:
```
{
    "property_id": 8,
    "locality_id": 8,
    "owner_name": "Updated Example8 Owner"
}
```
5. Send the Request: Click the "Send" button.
6. View the Response: Verify the response.

### 4. Delete Property Record API

1. Open Postman and create a new request.
2. Select the Method: Choose `DELETE` from the dropdown menu.
3. Enter the URL: Type http://localhost:3000/api/properties/delete into the URL field.
4. Select `Body` as `raw (JSON)`. Paste the follwing in the `Body`:
```
{
    "property_id": 8
}
```
5. Send the Request: Click the "Send" button.
6. View the Response: Verify the response.

### 5. Get All Localities API

1. Open Postman and create a new request.
2. Select the Method: Choose `GET` from the dropdown menu.
3. Enter the URL: Type http://localhost:3000/api/localities/all into the URL field. 
4. Select `Body` as `none`.
5. Send the Request: Click the "Send" button.
6. View the Response: Verify the response.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
[Node.js](https://nodejs.org/en)
[express.js](https://expressjs.com/)


