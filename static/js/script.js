document.addEventListener('DOMContentLoaded', function() {
    const sendButton = document.getElementById('sendButton');
    const messageDiv = document.getElementById('message');
    const outputPre = document.getElementById('output');

    // Sidebar elements
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    const closeBtn = document.querySelector('.sidebar-close-btn'); // Use querySelector for class

    // Function to toggle sidebar
    function toggleSidebar() {
        document.body.classList.toggle('sidebar-open');
    }

    // Event listener for hamburger button
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', toggleSidebar);
    } else {
        console.error('Sidebar toggle button not found.');
    }

    // Event listener for close button inside sidebar
    if (closeBtn) {
        closeBtn.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent default anchor behavior
            toggleSidebar();
        });
    } else {
        console.error('Sidebar close button not found.');
    }

    // Ensure elements were found before adding listener
    if (sendButton) {
        sendButton.addEventListener('click', () => {
            // Check if messageDiv and outputPre exist before using them
            if (messageDiv) {
                messageDiv.textContent = 'Acionando script (individual)...';
                messageDiv.className = ''; // Reset class
            }
            if (outputPre) {
                outputPre.textContent = ''; // Clear previous output
                outputPre.style.display = 'none'; // Hide output initially
            }

            fetch('/trigger_single_send', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        if (messageDiv) {
                            messageDiv.textContent = data.message || 'Script individual acionado!';
                            messageDiv.className = 'success';
                        }
                        if (outputPre && data.output) {
                            outputPre.textContent = data.output;
                            outputPre.style.display = 'block'; // Show output block
                        }
                    } else {
                        if (messageDiv) {
                            messageDiv.textContent = data.message || 'Falha ao acionar script individual.';
                            messageDiv.className = 'error';
                        }
                        if (outputPre && data.output) { // Show output even on error if available
                            outputPre.textContent = data.output;
                            outputPre.style.display = 'block'; // Show output block
                        }
                        console.error("Single send response:", data);
                    }
                })
                .catch(error => {
                    if (messageDiv) {
                        messageDiv.textContent = 'Erro de comunicação com o servidor.';
                        messageDiv.className = 'error';
                    }
                    if (outputPre) {
                        outputPre.textContent = ''; // Clear output on fetch error
                        outputPre.style.display = 'none';
                    }
                    console.error('Single Send Fetch Error:', error);
                });
        });
    } else {
        console.error('Button with ID "sendButton" not found.');
        // Optionally display an error to the user on the page itself
        if (messageDiv) {
            messageDiv.textContent = 'Erro: Botão principal não encontrado.';
            messageDiv.className = 'error';
        }
    }

    // --- Dashboard Form Logic (if elements exist) ---
    const dashboardForm = document.getElementById('dashboard-form');
    const messageTemplateInput = document.getElementById('messageTemplate');
    const includeImageCheckbox = document.getElementById('includeImage');
    const statusArea = document.getElementById('status-area');
    const imageFileInput = document.getElementById('imageFile'); // Get the file input

    if (dashboardForm && messageTemplateInput && includeImageCheckbox && statusArea && imageFileInput) {
        dashboardForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent default form submission

            const messageTemplate = messageTemplateInput.value;
            const includeImage = includeImageCheckbox.checked;
            const imageFile = imageFileInput.files[0]; // Get the selected file

            // Basic validation
            if (includeImage && !imageFile) {
                statusArea.textContent = 'Erro: Marcou "Incluir Imagem" mas nenhum arquivo foi selecionado.';
                statusArea.className = 'error';
                statusArea.style.display = 'block';
                return; // Stop submission
            }

            statusArea.textContent = 'Iniciando processo de envio... Aguarde.';
            statusArea.className = 'processing'; // Use class for styling
            statusArea.style.display = 'block';
            dashboardForm.querySelector('button[type="submit"]').disabled = true; // Disable button

            // Use FormData to send text and file
            const formData = new FormData();
            formData.append('message_template', messageTemplate);
            formData.append('include_image', includeImage);
            if (includeImage && imageFile) {
                formData.append('imageFile', imageFile);
            }

            fetch('/send_messages', {
                method: 'POST',
                // DO NOT set Content-Type header when using FormData;
                // the browser sets it automatically with the correct boundary.
                body: formData, 
            })
            .then(response => response.json()) // Still expect JSON back
            .then(data => {
                console.log("Bulk send response:", data);
                statusArea.textContent = `Status: ${data.status}\n\nOutput:\n${data.output || 'Nenhum output recebido.'}`;
                if (data.success) {
                    statusArea.className = 'success';
                } else {
                    statusArea.className = 'error';
                }
            })
            .catch(error => {
                console.error('Bulk Send Fetch Error:', error);
                statusArea.textContent = `Erro de comunicação com o servidor ao tentar enviar em massa.\nDetalhes: ${error}`;
                statusArea.className = 'error';
            })
            .finally(() => {
                 dashboardForm.querySelector('button[type="submit"]').disabled = false; // Re-enable button
            });
        });
    } else {
        // console.log('Dashboard form elements not found on this page.');
        // Add checks for imageFileInput if needed
    }

    // --- Focus WhatsApp Button Logic ---
    const focusBtn = document.getElementById('focus-whatsapp-btn');
    const focusStatusSpan = document.getElementById('focus-status');

    if (focusBtn && focusStatusSpan) {
        focusBtn.addEventListener('click', () => {
            focusStatusSpan.textContent = 'Focando...';
            focusBtn.disabled = true; // Disable button during request

            fetch('/trigger_focus', { method: 'POST' })
                .then(response => {
                    if (!response.ok) {
                        // Handle HTTP errors (like 500 Internal Server Error)
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log("Focus script response:", data);
                    if (data.success) {
                        focusStatusSpan.textContent = 'Foco OK!';
                    } else {
                        focusStatusSpan.textContent = `Falha no foco. (${data.message || 'Erro desconhecido'})`;
                    }
                    // Optional: Log full output for debugging
                    // console.log("Focus script output:", data.output);
                })
                .catch(error => {
                    console.error('Focus Trigger Fetch Error:', error);
                    focusStatusSpan.textContent = 'Erro ao comunicar.';
                })
                .finally(() => {
                    focusBtn.disabled = false; // Re-enable button
                    // Clear status message after a delay
                    setTimeout(() => { focusStatusSpan.textContent = ''; }, 5000); 
                });
        });
    } else {
        if (!focusBtn) console.error('Button #focus-whatsapp-btn not found.');
        if (!focusStatusSpan) console.error('Span #focus-status not found.');
    }
    // --- End Focus WhatsApp Button Logic ---

    // --- Clear Log Button Logic ---
    const clearLogButton = document.getElementById('clearLogButton');
    const logMessageDiv = document.getElementById('logMessage');

    if (clearLogButton && logMessageDiv) {
        clearLogButton.addEventListener('click', () => {
            logMessageDiv.textContent = 'Limpando log...';
            logMessageDiv.className = ''; // Reset class
            clearLogButton.disabled = true; // Disable button during request

            fetch('/clear-log', { method: 'POST' })
                .then(response => {
                    if (!response.ok) {
                        // Try to get error message from JSON body if possible
                        return response.json().then(errData => {
                            throw new Error(errData.message || `HTTP error! status: ${response.status}`);
                        }).catch(() => {
                            // Fallback if response isn't JSON or has no message
                            throw new Error(`HTTP error! status: ${response.status}`);
                        });
                    }
                    return response.json();
                })
                .then(data => {
                    console.log("Clear log response:", data);
                    logMessageDiv.textContent = data.message || 'Resposta recebida do servidor.';
                    logMessageDiv.className = data.success ? 'success' : 'error';
                })
                .catch(error => {
                    console.error('Clear Log Fetch Error:', error);
                    logMessageDiv.textContent = `Erro: ${error.message || 'Não foi possível limpar o log.'}`;
                    logMessageDiv.className = 'error';
                })
                .finally(() => {
                    clearLogButton.disabled = false; // Re-enable button
                    // Optional: Clear the message after a few seconds
                    // setTimeout(() => { logMessageDiv.textContent = ''; logMessageDiv.className = ''; }, 5000);
                });
        });
    } else {
        if (!clearLogButton) console.error('Button #clearLogButton not found.');
        if (!logMessageDiv) console.error('Div #logMessage not found.');
    }
    // --- End Clear Log Button Logic ---

}); // End of DOMContentLoaded 