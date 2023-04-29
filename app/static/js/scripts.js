document.addEventListener('DOMContentLoaded', function () {
    // DOM elements
    const promptForm = document.getElementById('prompt-form');
    const modalities = document.getElementById('modalities');
    const resultElement = document.getElementById('result');
    const downloadButton = document.getElementById('download-pdf');
    const skeletonScreen = document.getElementById('skeleton-screen');
    const spinner = document.querySelector('.spinner');

    // Helper functions
    // Activate the selected modality button
    function activateModalityButton(button) {
        const activeButton = modalities.querySelector('.btn.active');
        if (activeButton) {
            activeButton.classList.remove('active');
        }
        button.classList.add('active');
    }

    // Display the result in the result element
    function displayResult(result) {
        resultElement.innerHTML = result;
    }

    // Show or hide the spinner based on the visible parameter
    function toggleSpinner(visible) {
        spinner.style.display = visible ? 'flex' : 'none';
    }

    // Event handlers
    // Handle form submission
    function handleFormSubmit(event) {
        event.preventDefault();
        toggleSpinner(true);
        // Fetch data from the API and display it
    }

    // Handle download button click
    function handleDownloadButtonClick(event) {
        // Handle download PDF action
    }

    // Handle modality button click
    function handleModalityButtonClick(event) {
        const button = event.target;
        const modalityValue = button.dataset.value;
        document.getElementById('modality').value = modalityValue;
        activateModalityButton(button);
    }

    // Event listeners
    modalities.addEventListener('click', function (event) {
        if (event.target.tagName === 'BUTTON') {
            handleModalityButtonClick(event);
        }
    });

    promptForm.addEventListener('submit', handleFormSubmit);
    downloadButton.addEventListener('click', handleDownloadButtonClick);
});
