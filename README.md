# AnalystGPT

AnalystGPT is a GPT app that currently provides responses from __[text-davinci-003](https://platform.openai.com/docs/models/gpt-3-5)__ and __[GPT4](https://platform.openai.com/docs/models/gpt-4)__.  It is hosted as a web application using a Flask framework for the webapp backend, a modular Blueprint structure, and a combination of HTML, CSS, and JavaScript for the frontend. The application utilizes the __[OpenAI Python Library](https://pypi.org/project/openai/)__ to interact with the GPT-4 model, generating text completions based on user input. The application is containerized with Docker and currently deployed as a Cloud Run service on GCP.

Via future posts on __[johncollins.ai](https://johncollins.ai/)__ I will develop AnalystGPT into a full blown "analyst" chatbot. I want to look at the improvements to its performance obtained from zero-shot vs few-shot vs Chain-of-Thought (CoT) vs automatic prompt setups, and various prompt optimization methods. 

I will also deploy via www.analyst-gpt.com, using GKE/nginix to improve performance.  I will probably re-write the UXUI with React JS to obtain a more intuitive analyst experience.

# Current setup

Flask app: A lightweight Flask web application framework in Python is used to build the backend of the AnalystGPT webapp. It handles incoming requests, processes them, and returns the desired output to the user.

Blueprint structure: The webapp is organized using Flask's Blueprint, which allows for a modular and scalable structure. This will help separate different parts of the application and makes the code more maintainable.

CSS and HTML: The frontend of the webapp is built using HTML and styled with CSS. 

JavaScript: JavaScript is used to make the frontend more interactive and dynamic, enabling client-side processing, and providing a better user experience. It currently handles user input, form submissions, and communication with the backend.

UX/UI concepts: User Experience (UX) and User Interface (UI) concepts are employed to create a user-friendly and visually appealing application. This includes designing an intuitive layout, user-friendly navigation, and clear presentation of information. I have kept things clean and minimal.

completions.py: This Python module contains the functions that interact with the OpenAI library to generate responses using the text-davinci-003 and GPT-4 models. It handles requests to the OpenAI API to obtain the desired output based on user input.

OpenAI library: The the __[OpenAI Python Library](https://pypi.org/project/openai/)__ is a Python package that provides an interface to interact with the OpenAI API, enabling access to the GPT-4 model for generating text completions.

Deployment: The application is containerized with Docker and currently deployed as a Cloud Run service on GCP.
