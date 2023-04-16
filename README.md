# AnalystGPT

AnalystGPT is a web application that uses the Flask framework for the backend, a modular Blueprint structure, and a combination of HTML, CSS, and JavaScript for the frontend. The application utilizes the OpenAI library to interact with the GPT-4 model, generating text completions based on user input. The application is containerized using Docker and can be deployed on a cloud service for easy access and scalability.

Via future posts on __[johncollins.ai](https://johncollins.ai/)__ I will develop AnalystGPT into a full blown "analyst" chatbot. I will look at the improvements to its performance obtained from zero-shot vs few-shot vs Chain-of-Thought (CoT) vs automatic prompt setups, and various prompt optimization methods. 

I will also host it under its __[own domain](www.analyst-gpt.com)__, and deploy via GKE/nginix to improve performance.  I will probably re-write the UXUI with React JS to obtain a more intuitive analyst experience.

# Current setup

AnalystGPT is a web application that uses the Flask framework for the backend, a modular Blueprint structure, and a combination of HTML, CSS, and JavaScript for the frontend. The application utilizes the OpenAI library to interact with the GPT-4 model, generating text completions based on user input. The application is containerized using Docker and can be deployed on a cloud service for easy access and scalability.

Flask app: A lightweight web application framework for Python is used to build the backend of the AnalystGPT application. It handles incoming requests, processes them, and returns the desired output to the user.

Blueprint structure: The application is organized using Flask's Blueprint, which allows for a modular and scalable structure. It helps separate different parts of the application and makes the code more maintainable.

CSS and HTML: The frontend of the application is built using HTML and styled with CSS. The HTML structure defines the layout of the web page, while the CSS enhances the appearance, making it more visually appealing and user-friendly.

JavaScript: JavaScript is used to make the frontend more interactive and dynamic, enabling client-side processing, and providing a better user experience. It handles user input, form submissions, and communication with the backend.

UX/UI concepts: User Experience (UX) and User Interface (UI) concepts are employed to create a user-friendly and visually appealing application. This includes designing an intuitive layout, user-friendly navigation, and clear presentation of information.

completions.py: This Python module contains the functions that interact with the OpenAI library to generate responses using the GPT-4 model. It fetches the API key and handles requests to the OpenAI API to obtain the desired output based on user input.

OpenAI library: The OpenAI library is a Python package that provides an interface to interact with the OpenAI API, enabling easy access to the GPT-4 model for generating text completions.

Deployment: The application is containerized using Docker, which simplifies deployment and ensures consistency across different environments. The Dockerfile is used to build a Docker image of the application, which can then be deployed on a cloud service like Google Cloud Run.
