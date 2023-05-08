document.addEventListener('DOMContentLoaded', function () {
    const promptForm = document.getElementById('prompt-form');
    const modalities = document.getElementById('modalities');
    const resultElement = document.getElementById('result');
    const downloadButton = document.getElementById('download-pdf');
    const skeletonScreen = document.getElementById('skeleton-screen');
    const spinner = document.querySelector('.spinner');

    function activateModalityButton(button) {
        const activeButton = modalities.querySelector('.btn.active');
        if (activeButton) {
            activeButton.classList.remove('active');
        }
        button.classList.add('active');
    }

    function displayResult(result) {
        resultElement.innerHTML = result;
    }

    function toggleSpinner(visible) {
        spinner.style.display = visible ? 'flex' : 'none';
        skeletonScreen.classList.toggle('d-none', !visible);
    }

    async function fetchData(modality, prompt) {
        try {
            const response = await fetch("/get_completion", {
                method: "POST",
                body: new FormData(promptForm),
            });
        
            if (response.ok) {
                const data = await response.json();
                logInfo("Data received: " + JSON.stringify(data));
                return data;
            } else {
                logError("Error occurred while fetching data", response.statusText);
                return { success: false, error: "An error occurred while fetching data. Please try again later." };
            }
        } catch (error) {
            logError("Error occurred while fetching data", error);
            return { success: false, error: "An error occurred while fetching data. Please try again later." };
        }
    }
    
    async function handleFormSubmit(event) {
        event.preventDefault();
        toggleSpinner(true);
        
        const prompt = promptForm.elements["prompt"].value;
        const modality = promptForm.elements["modality"].value;
        
        try {
            const result = await fetchData(modality, prompt);
        
            if (result.success) {
                displayResult(`<h3>Modality: ${modality}</h3><h5 class="text-lightgrey">Company: ${prompt}</h5><pre>${result.response}</pre>`);
            } else {
                displayError(result.error, resultElement);
            }
        } catch (error) {
            displayError("An error occurred while processing the request. Please try again later.", resultElement);
        }
        
        toggleSpinner(false);
    }

    async function downloadPdf(modality, prompt, response) {
    try {
        const { PDFDocument, rgb } = pdfLib;
        const doc = await PDFDocument.create();

        // Customize the PDF format based on the modality
        let title = "";
        if (modality === "business analyst") {
            title = "Business Analyst Report";
        } else if (modality === "investigator") {
            title = "Investigator Report";
        } else if (modality === "financial analyst") {
            title = "Financial Analyst Report";
        }

        const fontBytes = await fetch("https://pdf-lib.github.io/examples/fonts/Roboto-Regular.ttf").then((res) => res.arrayBuffer());
        const font = await doc.embedFont(fontBytes);

        const page = doc.addPage([595, 842]);
        const content = `${title}\nCompany: ${prompt}\n\n${response}`;
        const contentArray = content.split('\n');

        page.setFont(font);
        page.setFontSize(18);
        page.drawText(title, { x: 50, y: 792 });
        page.setFontSize(12);

        let yOffset = 50;
        contentArray.forEach((line, index) => {
            yOffset += 20;
            page.drawText(line, { x: 50, y: 792 - yOffset });
        });

            const pdfBytes = await doc.save();
            const blob = new Blob([pdfBytes], { type: "application/pdf" });
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = `${modality}_report.pdf`;
            link.click();
            logInfo("Download completed");
        } catch (error) {
            logError("Error occurred while downloading PDF", error);
            alert("An error occurred while downloading the PDF. Please try again later.");
        }
    }

    function handleDownloadButtonClick(event) {
        const modality = document.getElementById("modality").value;
        const prompt = document.getElementById("prompt").value;
        const response = document.querySelector("#result pre").innerText;

        toggleSpinner(true);
        downloadPdf(modality, prompt, response);
        toggleSpinner(false);

        alert("Download completed. Please check your download folder.");
    }

    function handleModalityButtonClick(event) {
        const button = event.target;
        const modalityValue = button.dataset.value;
        document.getElementById('modality').value = modalityValue;
        activateModalityButton(button);
    }

    modalities.addEventListener('click', function (event) {
        if (event.target.tagName === 'BUTTON') {
            handleModalityButtonClick(event);
        }
    });

    promptForm.addEventListener('submit', handleFormSubmit);
    downloadButton.addEventListener('click', handleDownloadButtonClick);
});
