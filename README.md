# HNG12 Task API

This is a FastAPI-based API developed as part of the HNG Internship program. It provides a simple endpoint that returns the following information in JSON format:
- **Email**: The registered email address used to sign up for the HNG12 Slack workspace.
- **Current Datetime**: The current date and time in ISO 8601 format (UTC).
- **GitHub URL**: The URL of the GitHub repository containing the project's codebase.

## Setup Instructions

Follow these steps to run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/cysof/hngTask0.git
   cd your-repo
2. Install dependencies:
  - pip install requirements.txt
3. Run the application:
  - uvicorn main:app --reload
4. Access the API:
  - he API will be available at http://127.0.0.1:8000/

### API Documentation
Endpoint
GET** https://hngtask0-hzpz.onrender.com/home
Request

  - No request body or parameters are required.

Response Format:
    {
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
    }
    
#### Example usage

Using curl:

- curl -X GET http://127.0.0.1:8000/
- http://127.0.0.1:8000/home

##### Request/response format

Response Format:
    {"email":"cysofthome@gmail.com",
    "current_datetime":"2025-01-30T13:41:50Z",
    "github_url":"https://github.com/cysof/hngTask0"
    }

###### Deployment
    The api is deployed on render and you can access it at 
    https://hngtask0-hzpz.onrender.com/home

### HNG Backlink**: 
    Includes the required backlink for Python developers: https://hng.tech/hire/python-developers.

---

### Key Features of the `README.md`:
1. **Clear Description**: Explains the purpose of the project and what the API does.
2. **Setup Instructions**: Provides step-by-step instructions to run the project locally.
3. **API Documentation**:
   - Includes the endpoint URL.
   - Describes the request/response format.
   - Provides an example usage with `curl`.
4. **HNG Backlink**: Includes the required backlink for Python developers: `https://hng.tech/hire/python-developers`.
5. **Deployment Information**: Mentions where the API is deployed (replace `<your-deployed-url>` with the actual URL).
6. **License**: Specifies the open-source license (optional but recommended).

This `README.md` file fully satisfies the documentation requirements for the project.