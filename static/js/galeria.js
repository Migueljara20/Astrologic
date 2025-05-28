// Función para abrir el modal
function openModal(src, alt) {
    const modal = document.getElementById('imageModal');
    
    // Mostrar loader
    modal.innerHTML = `
        <span class="close" onclick="closeModal()">&times;</span>
        <div class="modal-content-container">
            <div class="modal-loader">Cargando imagen...</div>
            <img class="modal-content" id="modalImage">
            <div id="caption"></div>
        </div>
    `;
    
    // Configurar la imagen
    const img = new Image();
    img.src = src;
    img.onload = function() {
        document.querySelector('.modal-loader').style.display = 'none';
        document.getElementById('modalImage').src = src;
        document.getElementById('caption').textContent = alt;
        adjustImageSize();
    };
    
    img.onerror = function() {
        document.querySelector('.modal-loader').textContent = 'Error al cargar la imagen';
    };
    
    modal.style.display = "block";
    document.body.style.overflow = 'hidden';
    window.addEventListener('resize', adjustImageSize);
}

// Ajustar tamaño de imagen en el modal
function adjustImageSize() {
    const modalImg = document.getElementById('modalImage');
    if (!modalImg || !modalImg.complete) return;
    
    const windowRatio = window.innerWidth / window.innerHeight;
    const imgRatio = modalImg.naturalWidth / modalImg.naturalHeight;
    
    if (imgRatio > windowRatio) {
        modalImg.style.width = '90%';
        modalImg.style.height = 'auto';
    } else {
        modalImg.style.width = 'auto';
        modalImg.style.height = '80vh';
    }
}

// Función para cerrar el modal
function closeModal() {
    document.getElementById('imageModal').style.display = "none";
    document.body.style.overflow = 'auto';
    window.removeEventListener('resize', adjustImageSize);
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Cerrar al hacer clic fuera
    document.getElementById('imageModal').addEventListener('click', function(e) {
        if (e.target === this) closeModal();
    });
    
    // Cerrar con ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && document.getElementById('imageModal').style.display === 'block') {
            closeModal();
        }
    });
});