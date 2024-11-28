async function sendForm(event) {
  event.preventDefault(); // Prevent the default form submission

  const form = document.getElementById("email_form");
  const formData = new FormData(form);

  const data = Object.fromEntries(formData.entries());

  try {
    const response = await fetch("/api/send-email", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (result.success) {
      alert("Email sent successfully!");
      form.reset();
    } else {
      alert("Failed to send email: " + result.message);
    }
  } catch (error) {
    alert("An error occurred: " + error.message);
  }
}
