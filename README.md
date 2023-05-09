# Analyst-GPT

### Summary
AnalystGPT is a versatile AI-powered analysis tool that generates comprehensive reports in various domains such as business, investigation, and finance. The application leverages the state-of-the-art GPT-4 language model from OpenAI to generate tailored reports based on user inputs.

### Features
1. AI-powered analysis using the GPT-4 language model
2. Support for multiple report types (business, investigation, finance)
3. Asynchronous data fetching using the JavaScript fetch API
4. Structured report display on the webpage
5. PDF report generation with custom formatting
6. Responsive design for optimal user experience across devices

### Usage
To use AnalystGPT:

1. Choose a report type (business, investigation, finance) by clicking on the corresponding button.
2. Enter the company name you wish to analyse in the input field and click the "Submit" button.
3. Wait for the AI-generated report to appear on the webpage.
4. Optionally, click the "Download PDF" button to download the report as a PDF file.

### User Interface
The UI of AnalystGPT is built using HTML, CSS, and JavaScript. Users can choose from three different types of reports (business, investigation, and finance) and submit their queries. The interface includes a spinner animation to indicate the processing time while the AI generates the report.

### AI-powered Analysis
AnalystGPT employs GPT-4, the current state-of-the-art language model from OpenAI, to generate comprehensive reports based on user queries. Users can expect relevant and accurate information tailored to their specific requirements.

### Asynchronous Data Fetching
The application leverages the JavaScript fetch API to communicate with the server and retrieve report data. The implementation uses async/await to handle asynchronous requests, ensuring a smooth user experience.

### Report Display and Download
Once the AI has generated the report, it is displayed in a structured format on the webpage. Users can also download the report as a PDF file with a custom format based on the chosen report type. The PDF generation is powered by the pdf-lib library, which provides a flexible and efficient way to create, modify, and save PDF files in the browser.

### Responsive Design
AnalystGPT uses a responsive design that ensures the application looks and functions well on different devices and screen sizes. The CSS styling, in particular, adapts to different viewports, providing an optimal user experience across devices.

### Technologies Used
1. GPT-4: OpenAI's current state-of-the-art language model for report generation
2. HTML, CSS, and JavaScript: Frontend development
3. pdf-lib: PDF report generation and manipulation in the browser
4. Fetch API: Asynchronous data fetching and communication with the server

### Deployment
AnalystGPT is deployed on a Google Kubernetes Engine (GKE) cluster with three nodes, each running Kubernetes. The cluster leverages Nginx Ingress controller to route external traffic to the application.

The application is deployed using a Deployment resource, with its container image pulled from Google Artifact Registry. The Deployment specifies resource requests and limits, as well as required environment variables such as the OpenAI API key, which is obtained from a Kubernetes Secret resource. The application is exposed on port 8080 via a NodePort Service resource.

To secure the application, Cert-Manager is installed to manage SSL certificates. The certificate issuer, Let's Encrypt, is configured using an Issuer resource, specifying the ACME server, email, and privateKeySecretRef along with the http01 solver for domain validation.

An Ingress resource is created to route traffic to the service, using an allocated static IP address, and hosting both analyst-gpt.com and www.analyst-gpt.com domains. TLS termination is configured using a Certificate resource, which is issued by Let's Encrypt and managed by cert-manager, ensuring HTTPS for all connections.

### Speed up

The GPT4 response is quite slow.  The asynchronous function I am using is already optimized to a great extent. It is running the OpenAI API call in a separate thread, which is the best approach to speed up I/O-bound tasks like this one.

However, the speed of this function is primarily dependent on the response time of the OpenAI API, which is out of my control. If the API is slow, my function will also be slow because it has to wait for the response.

Remember that AI computations can be quite intensive, and the speed will also depend on the complexity of the task I am asking the model to perform. In this case, I am asking the model to generate a fairly complex and detailed output, which could take some time.

Here are some tips to potentially improve the performance:

Reduce the amount of data: If possible, try to reduce the max_tokens value. This could speed up the response time but at the cost of potentially less detailed responses.

Concurrency: If you have multiple independent tasks, you can run them concurrently. For example, if I am calling this function multiple times with different prompts and modalities, you can use asyncio.gather() to run these tasks concurrently. However, be aware of the API rate limits.

Check my internet connection: A slow internet connection could also impact the response time.

Upgrade my OpenAI plan: OpenAI may offer different plans with different performance characteristics. Upgrading to a better plan might speed up the response time.

Remember, the time taken by an AI model to generate a response is due to the computational complexity of the task, and there is a limit to how much you can speed it up. It's always a balance between speed and quality of the output.

### License
AnalystGPT is released under the MIT License.