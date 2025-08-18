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
  if (event.target == editModal) {
    secondModal.style.display = "none";
  }
}


function autofill() {
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


// Функції модального вікна для редагування даних користувача
var editModal = document.getElementById("editModal");

function editUser(userId) {

    const user = allUsers[userId];
    const message = `Edit of user ${user.firstname}`
    console.log(message);
    // Find the form elements inside the modal
    const form = document.querySelector('#editModal form');

    if (form && user) {
        // Find the input fields by their name and populate them
        document.getElementById('editUserTitle').textContent  = `Edit user with id: ${userId}`;
        form.querySelector('input[name="id"]').value = userId;
        form.querySelector('input[name="firstname"]').value = user.firstname;
        form.querySelector('input[name="lastname"]').value = user.lastname;
        form.querySelector('input[name="age"]').value = user.age;
        form.querySelector('input[name="email"]').value = user.email;

        // Change the form action to point to the edit URL
//        form.action = `edit_user/${userId}`;

        // Open the modal
        openEditModal();
    } else {
        console.error("User data or form not found!");
    }
}


function openEditModal() {
  editModal.style.display = "block";
}

function closeEditModal() {
  editModal.style.display = "none";
}

// Функции, которые будут вызываться из второго модального окна
function firstAction() {
  alert('Выполнено первое действие!');
  closeSecondModal();
}

function secondAction() {
  alert('Выполнено второе действие!');
  closeSecondModal();
}