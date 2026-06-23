/*
  script.js — Faaji & Brew Palace custom JavaScript

  Handles two things:
    1. Auto-dismiss Django flash messages after 5 seconds so they do
       not sit on screen indefinitely.
    2. Set the correct cancel URL on the confirmation modal before it
       opens, so one shared modal works for every booking card.
*/

document.addEventListener('DOMContentLoaded', function () {

    // Auto-dismiss flash messages after 5 seconds using Bootstrap's
    // Alert component to trigger the built-in fade-out transition.
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
    setTimeout(function () {
        // it click the built-in close button so Bootstrap's
        // own fade-out animation runs correctly in Bootstrap 5.0.x
        const closeBtn = alert.querySelector('[data-bs-dismiss="alert"]');
        if (closeBtn) {
            closeBtn.click();
        }
    }, 5000);
});

    // Cancel booking modal — runs only on the My Bookings page where
    // the modal exists. I write that URL into the hidden
    // form action so the right booking gets cancelled on confirm.
    const cancelModal = document.getElementById('cancelModal');
    if (cancelModal) {
        cancelModal.addEventListener('show.bs.modal', function (event) {
            const triggerButton = event.relatedTarget;
            const cancelUrl = triggerButton.getAttribute('data-cancel-url');
            const cancelForm = document.getElementById('cancelForm');
            if (cancelForm && cancelUrl) {
                cancelForm.setAttribute('action', cancelUrl);
            }
        });
    }

});
