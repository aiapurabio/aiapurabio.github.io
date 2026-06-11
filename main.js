document.addEventListener('DOMContentLoaded', () => {
    // Navigazione basilare per la dashboard (Vibe Coding micro-interactions)
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Remove active class from all
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked
            e.currentTarget.classList.add('active');
            
            // Subtle animation feedback
            const targetId = e.currentTarget.getAttribute('href').substring(1);
            const targetCard = document.getElementById(`card-${targetId}`);
            
            if(targetCard) {
                targetCard.style.transform = 'scale(1.05)';
                setTimeout(() => {
                    targetCard.style.transform = '';
                }, 300);
            }
        });
    });

    // Event listeners per le azioni dei moduli
    const actionBtns = document.querySelectorAll('.action-btn');
    actionBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const moduleName = e.target.parentElement.querySelector('h3').innerText;
            console.log(`Modulo attivato: ${moduleName}`);
            // Qui implementeremo le logiche specifiche per ogni area (Digital Strategy, Copyright, Content).
            alert(`Azione registrata per il modulo: ${moduleName}. In attesa di istruzioni strategiche.`);
        });
    });
});
