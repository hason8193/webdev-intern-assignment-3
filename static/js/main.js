// Main JavaScript for G-Scores

document.addEventListener("DOMContentLoaded", function () {
  // Initialize tooltips
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // Form validation
  const forms = document.querySelectorAll(".needs-validation");
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener(
      "submit",
      function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add("was-validated");
      },
      false
    );
  });

  // Auto-dismiss alerts after 5 seconds
  const alerts = document.querySelectorAll(".alert:not(.alert-permanent)");
  alerts.forEach(function (alert) {
    setTimeout(function () {
      if (alert) {
        const bsAlert = new bootstrap.Alert(alert);
        bsAlert.close();
      }
    }, 5000);
  });

  // SBD input formatting
  const sbdInput = document.getElementById("id_sbd");
  if (sbdInput) {
    sbdInput.addEventListener("input", function (e) {
      // Remove non-digits
      let value = e.target.value.replace(/\D/g, "");
      // Limit to 8 digits
      if (value.length > 8) {
        value = value.substring(0, 8);
      }
      e.target.value = value;
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  });

  // Table row highlighting
  const tableRows = document.querySelectorAll("table tbody tr");
  tableRows.forEach((row) => {
    row.addEventListener("mouseenter", function () {
      this.style.backgroundColor = "rgba(102, 126, 234, 0.1)";
    });
    row.addEventListener("mouseleave", function () {
      this.style.backgroundColor = "";
    });
  });

  // Loading state for forms
  const submitButtons = document.querySelectorAll('button[type="submit"]');
  submitButtons.forEach((button) => {
    const form = button.closest("form");
    if (form) {
      form.addEventListener("submit", function () {
        button.disabled = true;
        const originalText = button.innerHTML;
        button.innerHTML = '<span class="loading"></span> Processing...';

        // Re-enable button after 3 seconds (fallback)
        setTimeout(() => {
          button.disabled = false;
          button.innerHTML = originalText;
        }, 3000);
      });
    }
  });
});

// Utility functions
function formatNumber(num) {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(function () {
    // Show success message
    const toast = document.createElement("div");
    toast.className = "toast-notification";
    toast.textContent = "Copied to clipboard!";
    document.body.appendChild(toast);

    setTimeout(() => {
      document.body.removeChild(toast);
    }, 2000);
  });
}

// Export functionality for tables
function exportTableToCSV(tableId, filename = "export.csv") {
  const table = document.getElementById(tableId);
  if (!table) return;

  let csv = [];
  const rows = table.querySelectorAll("tr");

  for (let i = 0; i < rows.length; i++) {
    const row = [],
      cols = rows[i].querySelectorAll("td, th");

    for (let j = 0; j < cols.length; j++) {
      let cellText = cols[j].innerText;
      // Clean up the text (remove extra whitespace, badges, etc.)
      cellText = cellText.replace(/\s+/g, " ").trim();
      row.push('"' + cellText + '"');
    }

    csv.push(row.join(","));
  }

  // Download CSV
  const csvFile = new Blob([csv.join("\n")], { type: "text/csv" });
  const downloadLink = document.createElement("a");
  downloadLink.download = filename;
  downloadLink.href = window.URL.createObjectURL(csvFile);
  downloadLink.style.display = "none";
  document.body.appendChild(downloadLink);
  downloadLink.click();
  document.body.removeChild(downloadLink);
}
