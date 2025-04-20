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

    if (dashboardForm && messageTemplateInput && includeImageCheckbox && statusArea) {
        dashboardForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent default form submission

            const messageTemplate = messageTemplateInput.value;
            const includeImage = includeImageCheckbox.checked;

            statusArea.textContent = 'Iniciando processo de envio... Aguarde.';
            statusArea.className = 'processing'; // Use class for styling
            statusArea.style.display = 'block';
            dashboardForm.querySelector('button[type="submit"]').disabled = true; // Disable button

            fetch('/send_messages', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message_template: messageTemplate,
                    include_image: includeImage // Send image flag even if unused by backend for now
                }),
            })
            .then(response => response.json()) // Always expect JSON back
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
    }
}); 