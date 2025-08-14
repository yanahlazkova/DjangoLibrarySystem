var modal = document.getElementById("myModal");


// Функція для відкриття модального вікна
function openModal() {
  modal.style.display = "block";
}

// Функція для закриття модального вікна
function closeModal() {
  modal.style.display = "none";
}

// Закриття вікна, якщо користувач клацне за межами модального вікна
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


function autofill() {

    window.autofill = function () {
        const form = document.getElementById('formUser');
        if (form) {
            const fakeData = {
                firstname: faker.person.firstName(),
                lastname: faker.person.lastName(),
                age: faker.number.int({ min: 18, max: 90 }),
                email: faker.internet.email(),
            };

            form.querySelector('input[name="firstname"]').value = fakeData.firstname;
            form.querySelector('input[name="lastname"]').value = fakeData.lastname;
            form.querySelector('input[name="age"]').value = fakeData.age;
            form.querySelector('input[name="email"]').value = fakeData.email;
        }
    }
}