document.getElementById("loanForm").addEventListener("submit", function(event) {

    event.preventDefault();

    const data = {
        Gender: document.getElementById("Gender").value,
        Married: document.getElementById("Married").value,
        Dependents: document.getElementById("Dependents").value,
        Education: document.getElementById("Education").value,
        Self_Employed: document.getElementById("Self_Employed").value,

        ApplicantIncome:
            document.getElementById("ApplicantIncome").value,

        CoapplicantIncome:
            document.getElementById("CoapplicantIncome").value,

        LoanAmount:
            document.getElementById("LoanAmount").value,

        Loan_Amount_Term:
            document.getElementById("Loan_Amount_Term").value,

        Credit_History:
            document.getElementById("Credit_History").value,

        Property_Area:
            document.getElementById("Property_Area").value
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    .then(response => response.json())

    .then(result => {

        document.getElementById("result").innerText =
            "Logistic Regression: " + result.prediction +
            "\nDecision Tree: " + result.decision_tree_prediction;

        alert(
            "Logistic Regression: " + result.prediction +
            "\nDecision Tree: " + result.decision_tree_prediction
        );

    })

    .catch(error => {

        console.error(error);

        document.getElementById("result").innerText =
            "Error occurred. Please try again.";

    });

});