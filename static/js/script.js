document.addEventListener('DOMContentLoaded', function() {
    const sendButton = document.getElementById('sendButton');
    const messageDiv = document.getElementById('message');
    const outputPre = document.getElementById('output');

    // Ensure elements were found before adding listener
    if (sendButton) {
        sendButton.addEventListener('click', () => {
            // Check if messageDiv and outputPre exist before using them
            if (messageDiv) {
                messageDiv.textContent = 'Acionando script...';
                messageDiv.className = ''; // Reset class
            }
            if (outputPre) {
                outputPre.textContent = ''; // Clear previous output
                outputPre.style.display = 'none'; // Hide output initially
            }

            fetch('/trigger_send', {
                method: 'POST',
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    if (messageDiv) {
                        messageDiv.textContent = data.message || 'Script acionado com sucesso!';
                        messageDiv.className = 'success';
                    }
                    if (outputPre && data.output) {
                        outputPre.textContent = data.output;
                        outputPre.style.display = 'block'; // Show output block
                    }
                } else {
                    if (messageDiv) {
                        messageDiv.textContent = data.message || 'Falha ao acionar o script.';
                        messageDiv.className = 'error';
                    }
                    if (outputPre && data.output) { // Show output even on error if available
                        outputPre.textContent = data.output;
                        outputPre.style.display = 'block'; // Show output block
                    }
                    console.error("Error from server:", data);
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
                console.error('Fetch Error:', error);
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
}); 