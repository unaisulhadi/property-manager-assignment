# Property Manager API Request/Response Examples

This document provides sample request bodies and responses for all implemented endpoints.

Base URL: `http://localhost:8000`

Authentication:
- Use JWT access token in header for protected routes:
- `Authorization: Bearer <access_token>`

---

## 1) Auth APIs

### POST `/api/auth/register/`

**Request Body**
```json
{
  "email": "staff1@example.com",
  "first_name": "Staff",
  "last_name": "User",
  "password": "StrongPassword123!"
}
```

**Success Response (200)**
```json
{
  "success": true,
  "message": "Registration Successful!",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
    "email": "staff1@example.com",
    "first_name": "Staff",
    "last_name": "User",
    "full_name": "Staff User"
  }
}
```

**Validation Error (400)**
```json
{
  "success": false,
  "message": "Registration failed",
  "error_code": "reg_error",
  "errors": [
    "email: This field must be unique."
  ]
}
```

---

### POST `/api/auth/login/`

**Request Body**
```json
{
  "email": "staff1@example.com",
  "password": "StrongPassword123!"
}
```

**Success Response (200)**
```json
{
  "success": true,
  "message": "Login Successful!",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
    "email": "staff1@example.com",
    "first_name": "Staff",
    "last_name": "User",
    "full_name": "Staff User"
  }
}
```

**Auth Error (401)**
```json
{
  "success": false,
  "message": "Authentication failed",
  "error_code": "authentication_failed",
  "errors": [
    "Invalid credentials"
  ]
}
```

---

## 2) Property APIs

### POST `/api/properties/`

**Headers**
- `Authorization: Bearer <access_token>`

**Request Body**
```json
{
  "name": "Sunrise Residency",
  "address": "123 Main Street, Singapore"
}
```

**Success Response (200)**
```json
{
  "success": true,
  "message": "Property created successfully",
  "data": {
    "id": 1,
    "name": "Sunrise Residency",
    "address": "123 Main Street, Singapore"
  }
}
```

**Validation Error (400)**
```json
{
  "success": false,
  "message": "Property creation failed",
  "errors": {
    "name": [
      "This field is required."
    ]
  }
}
```

---

### GET `/api/properties/`

**Headers**
- `Authorization: Bearer <access_token>`

**Success Response (200)**
```json
{
  "success": true,
  "message": "Properties fetched successfully",
  "data": [
    {
      "id": 1,
      "name": "Sunrise Residency",
      "address": "123 Main Street, Singapore"
    }
  ]
}
```

---

### GET `/api/properties/:property_id/`

**Example URL**
- `/api/properties/1/`

**Headers**
- `Authorization: Bearer <access_token>`

**Success Response (200)**
```json
{
  "success": true,
  "message": "Property fetched successfully",
  "data": {
    "id": 1,
    "name": "Sunrise Residency",
    "address": "123 Main Street, Singapore"
  }
}
```

---

## 3) Unit APIs

### POST `/api/properties/:property_id/units/`

**Example URL**
- `/api/properties/1/units/`

**Headers**
- `Authorization: Bearer <access_token>`

**Request Body**
```json
{
  "unit_number": "A-101",
  "monthly_rent": "2500.00",
  "status": "AVAILABLE"
}
```

**Success Response (200)**
```json
{
  "success": true,
  "message": "Unit created successfully",
  "data": {
    "id": 1,
    "property": 1,
    "unit_number": "A-101",
    "monthly_rent": "2500.00",
    "status": "AVAILABLE"
  }
}
```

---

### GET `/api/properties/units/`

> Note: Current implemented route is `/api/properties/units/` (not `/api/units`).

**Headers**
- `Authorization: Bearer <access_token>`

**Optional Query**
- `?status=AVAILABLE`
- `?status=OCCUPIED`

**Success Response (200)**
```json
{
  "success": true,
  "message": "Units fetched successfully",
  "data": [
    {
      "id": 1,
      "property": 1,
      "unit_number": "A-101",
      "monthly_rent": "2500.00",
      "status": "AVAILABLE"
    }
  ]
}
```

---

## 4) Member APIs

### POST `/api/members/`

**Headers**
- `Authorization: Bearer <access_token>`

**Request Body**
```json
{
  "full_name": "John Tenant",
  "email": "john.tenant@example.com"
}
```

**Success Response (200)**
```json
{
  "success": true,
  "message": "Member created successfully",
  "data": {
    "id": 1,
    "full_name": "John Tenant",
    "email": "john.tenant@example.com"
  }
}
```

---

### GET `/api/members/`

**Headers**
- `Authorization: Bearer <access_token>`

**Success Response (200)**
```json
{
  "success": true,
  "message": "Members fetched successfully",
  "data": [
    {
      "id": 1,
      "full_name": "John Tenant",
      "email": "john.tenant@example.com"
    }
  ]
}
```

---

## 5) Contract APIs

### POST `/api/contracts/`

**Headers**
- `Authorization: Bearer <access_token>`

**Request Body (monthly_rent omitted to use unit rent)**
```json
{
  "unit": 1,
  "member": 1,
  "start_date": "2026-04-01",
  "end_date": "2027-03-31"
}
```

**Success Response (200)**
```json
{
  "success": true,
  "message": "Contract created successfully",
  "data": {
    "id": 1,
    "total_contract_value": 30333.33,
    "start_date": "2026-04-01",
    "end_date": "2027-03-31",
    "monthly_rent": "2500.00",
    "unit": 1,
    "member": 1
  }
}
```

**Overlap Error (400)**
```json
{
  "success": false,
  "message": "Contract creation failed",
  "errors": {
    "non_field_errors": [
      "This unit is already booked for the selected date range"
    ]
  }
}
```

---

### GET `/api/contracts/`

**Headers**
- `Authorization: Bearer <access_token>`

**Success Response (200)**
```json
{
  "success": true,
  "message": "Contracts fetched successfully",
  "data": [
    {
      "id": 1,
      "total_contract_value": 30333.33,
      "start_date": "2026-04-01",
      "end_date": "2027-03-31",
      "monthly_rent": "2500.00",
      "unit": 1,
      "member": 1
    }
  ]
}
```

---

### GET `/api/contracts/?active=true`

**Headers**
- `Authorization: Bearer <access_token>`

**Success Response (200)**
```json
{
  "success": true,
  "message": "Contracts fetched successfully",
  "data": [
    {
      "id": 1,
      "total_contract_value": 30333.33,
      "start_date": "2026-04-01",
      "end_date": "2027-03-31",
      "monthly_rent": "2500.00",
      "unit": 1,
      "member": 1
    }
  ]
}
```

---

## Common Auth Error (Protected Endpoints)

**Missing/Invalid JWT (401)**
```json
{
  "success": false,
  "message": "JWT Authentication failed. Invalid token or credentials.",
  "error_code": "authentication_failed",
  "errors": [
    "Given token not valid for any token type"
  ]
}
```
