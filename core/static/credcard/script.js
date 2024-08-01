function formatMonthYear(input) {
    let value = input.value;
    if (/^\d{2}\/\d{4}$/.test(value)) {
        return; // Already in MM/YYYY format
    }

    // Remove non-numeric characters
    value = value.replace(/[^\d]/g, '');

    if (value.length >= 5) {
        value = value.substring(0, 2) + '/' + value.substring(2, 6);
    }

    input.value = value;
}

function validateForm() {
    let startMonthYear = document.getElementById('start_month_year').value;
    let endMonthYear = document.getElementById('end_month_year').value;

    if (!/^(0[1-9]|1[0-2])\/\d{4}$/.test(startMonthYear) || !/^(0[1-9]|1[0-2])\/\d{4}$/.test(endMonthYear)) {
        alert("Por favor, insira as datas no formato MM/YYYY.");
        return false;
    }

    return true;
}