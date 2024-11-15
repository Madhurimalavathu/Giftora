const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

const sign_up_form = document.querySelector(".sign-up-form");
const sign_up_username = document.querySelector("#sign-up-username");
const sign_up_email = document.querySelector("#sign-up-email");
const sign_up_password = document.querySelector("#sign-up-password");
const sign_up_confirm_password = document.querySelector("#sign-up-confirm-password");

// Sign-in form fields
const sign_in_form = document.querySelector(".sign-in-form");
const sign_in_username = document.querySelector("#sign-in-username");
const sign_in_password = document.querySelector("#sign-in-password");

// Regular expression for email validation
const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

// Function to validate the sign-up form
function validateSignUpForm() {
  let isValid = true;

  // Validate username (should not be empty)
  if (!sign_up_username.value.trim()) {
    isValid = false;
    alert("Username is required!");
  }

  // Validate email (should match the pattern)
  if (!emailPattern.test(sign_up_email.value)) {
    isValid = false;
    alert("Please enter a valid email address.");
  }

  // Validate password (should not be empty)
  if (!sign_up_password.value.trim()) {
    isValid = false;
    alert("Password is required!");
  }

  // Validate password confirmation (should match password)
  if (sign_up_password.value !== sign_up_confirm_password.value) {
    isValid = false;
    alert("Passwords do not match!");
  }

  // Ensure confirm password is not empty
  if (!sign_up_confirm_password.value.trim()) {
    isValid = false;
    alert("Please confirm your password!");
  }

  return isValid;
}
// Function to validate the sign-in form
function validateSignInForm() {
  let isValid = true;

  // Validate username (should not be empty)
  if (!sign_in_username.value.trim()) {
    isValid = false;
    alert("Username is required!");
  }

  // Validate password (should not be empty)
  if (!sign_in_password.value.trim()) {
    isValid = false;
    alert("Password is required!");
  }

  return isValid;
}


sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});