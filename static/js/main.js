// Custom JavaScript for Plant Disease Detection App

// Intialize AOS 
AOS.init()

document.addEventListener('DOMContentLoaded', function() {
    // Add 'active' class to current nav item
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.link');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (currentPath === linkPath || 
            (linkPath !== '/' && currentPath.startsWith(linkPath))) {
            link.parentElement.classList.add('active');
            link.classList.add('active');
        }
    });
    
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // Add animation class to elements with 'data-animate' attribute
    const animateElements = document.querySelectorAll('[data-animate]');
    animateElements.forEach(element => {
        element.classList.add('fade-in');
    });
    
    // Handle file input for image upload
    const fileInput = document.getElementById('file-input');
    if (fileInput) {
        fileInput.addEventListener('change', function() {
            const fileLabel = document.querySelector('.custom-file-label');
            if (fileLabel) {
                fileLabel.textContent = this.files[0] ? this.files[0].name : 'Choose file';
            }
            
            // Preview image if available
            const previewElement = document.getElementById('image-preview');
            if (previewElement && this.files && this.files[0]) {
                const reader = new FileReader();
                
                reader.onload = function(e) {
                    previewElement.src = e.target.result;
                    previewElement.style.display = 'block';
                };
                
                reader.readAsDataURL(this.files[0]);
            }
        });
    }
    
    // Handle form submission with AJAX if needed
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Simulate form submission (replace with actual AJAX call)
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.innerHTML;
            
            submitButton.disabled = true;
            submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Sending...';
            
            // Simulate API call
            setTimeout(() => {
                const formElements = this.elements;
                for (let i = 0; i < formElements.length; i++) {
                    if (formElements[i].type !== 'submit') {
                        formElements[i].value = '';
                    }
                }
                
                // Show success message
                const successAlert = document.createElement('div');
                successAlert.className = 'alert alert-success mt-3';
                successAlert.innerHTML = '<i class="fas fa-check-circle me-2"></i> Your message has been sent successfully!';
                this.appendChild(successAlert);
                
                // Reset button
                submitButton.disabled = false;
                submitButton.innerHTML = originalText;
                
                // Hide alert after 5 seconds
                setTimeout(() => {
                    successAlert.remove();
                }, 5000);
            }, 1500);
        });
    }
}); 