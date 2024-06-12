# Pushing a FastAPI Hello World App to Google Container Registry (GCR)

This README provides step-by-step instructions on how to build and push a Docker image of a FastAPI Hello World application to Google Container Registry (GCR) using Colima as the container runtime.

## Prerequisites

Before you begin, ensure that you have the following:

- Google Cloud SDK installed: [Installation Guide](https://cloud.google.com/sdk/docs/install)
- Docker installed: [Installation Guide](https://docs.docker.com/get-docker/)
- Colima installed (if not using Docker Desktop): [Installation Guide](https://github.com/abiosoft/colima)
- Git installed: [Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Python installed: [Installation Guide](https://www.python.org/downloads/)

## Steps

1. **Clone the FastAPI Hello World repository:**

   ```
   git clone https://github.com/yourusername/fastapi-hello-world.git
   cd fastapi-hello-world
   ```

2. **Create a virtual environment (choose one of the following methods):**

   - Using pyenv:
     ```
     pyenv install 3.9.0
     pyenv local 3.9.0
     python -m venv venv
     source venv/bin/activate
     ```
   - Using conda:
     ```
     conda create --name myenv python=3.9
     conda activate myenv
     ```
   - Using mamba:
     ```
     mamba create --name myenv python=3.9
     mamba activate myenv
     ```

3. **Install the required dependencies:**

   ```
   pip install -r requirements.txt
   ```

4. **Ensure Colima is started (if using Colima instead of Docker Desktop):**

   ```
   colima status
   ```

   If Colima is not running, start it using:

   ```
   colima start
   ```

5. **Authenticate with Google Cloud:**

   ```
   gcloud auth login
   ```

   Follow the prompts to log in to your Google Cloud account.

6. **Configure Docker to use GCR:**

   ```
   gcloud auth configure-docker us-central1-docker.pkg.dev
   ```

7. **Build the Docker image:**

   ```
   docker build -t us-central1-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/fastapi-hello-world:[TAG] .
   ```

   Replace `[PROJECT_ID]`, `[REPOSITORY_NAME]`, and `[TAG]` with your specific values.

8. **Push the Docker image to GCR:**
   ```
   docker push us-central1-docker.pkg.dev/[PROJECT_ID]/[REPOSITORY_NAME]/fastapi-hello-world:[TAG]
   ```

After completing these steps, your FastAPI Hello World Docker image will be available in the specified GCR repository.

## Running the FastAPI Hello World App Locally

To run the FastAPI Hello World application locally, follow these steps:

1. Ensure you have activated the virtual environment (see step 2 above).

2. Start the FastAPI server:

   ```
   uvicorn main:app --reload
   ```

3. Open your web browser and visit `http://localhost:8000` to see the Hello World message.

4. To stop the server, press `Ctrl + C` in the terminal.

Here's the updated documentation with instructions on how to call the FastAPI endpoint from the terminal using `curl`:

```python
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def get_current_time(name: str):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"message": f"Hello, {name}! The current time is: {current_time}"}
```

## Calling the FastAPI Endpoint from the Terminal

To call the FastAPI endpoint from the terminal, you can use the `curl` command. Here's how you can make a request to the `/` endpoint with the `name` parameter:

1. Make sure your FastAPI server is running (see the "Running the FastAPI Hello World App Locally" section in the previous response).

2. Open a new terminal window.

3. Use the following `curl` command to make a GET request to the `/` endpoint:
   ```
   curl -X GET "http://localhost:8000/?name=John"
   ```
   Replace `John` with the desired name value.

4. Press Enter to execute the command.

The server will respond with a JSON object containing the personalized greeting message and the current time. For example:
```json
{"message": "Hello, John! The current time is: 2023-06-12 10:30:45"}
```

You can modify the `name` parameter in the `curl` command to get a personalized greeting with a different name.

## Alternative: Using a Web Browser

Alternatively, you can call the FastAPI endpoint using a web browser:

1. Make sure your FastAPI server is running (see the "Running the FastAPI Hello World App Locally" section in the previous response).

2. Open a web browser.

3. Enter the following URL in the address bar:
   ```
   http://localhost:8000/?name=John
   ```
   Replace `John` with the desired name value.

4. Press Enter to navigate to the URL.

The browser will display the JSON response with the personalized greeting message and the current time.

That's it! You can now call the FastAPI endpoint from the terminal using `curl` or through a web browser, passing the `name` parameter to get a personalized greeting.

## Additional Resources

- FastAPI Documentation: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Google Cloud SDK Documentation: [https://cloud.google.com/sdk/docs](https://cloud.google.com/sdk/docs)
- Docker Documentation: [https://docs.docker.com/](https://docs.docker.com/)
- Colima GitHub Repository: [https://github.com/abiosoft/colima](https://github.com/abiosoft/colima)

If you encounter any issues or have questions, please refer to the respective documentation or seek assistance from the community.
