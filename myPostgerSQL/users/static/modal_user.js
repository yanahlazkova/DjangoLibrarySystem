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
            phone: faker.phone.number({ style: 'international' }),
        };

        form.querySelector('input[name="firstname"]').value = fakeData.firstname;
        form.querySelector('input[name="lastname"]').value = fakeData.lastname;
        form.querySelector('input[name="age"]').value = fakeData.age;
        form.querySelector('input[name="email"]').value = fakeData.email;
        form.querySelector('input[name="login"]').value = fakeData.login;
        form.querySelector('input[name="password"]').value = fakeData.password;
        form.querySelector('input[name="phone"]').value = fakeData.phone;
    }
}


// Функції модального вікна для редагування даних користувача
var editModal = document.getElementById("editModal");

function editUser(userId) {
    fetch(`/users/${userId}/`)
        .then(response => {
            if (!response.ok) {
                // Если ответ не OK, обрабатываем ошибку от сервера
                return response.json().then(errorData => {
                    throw new Error(errorData.error || "Помилка мережі");
                });
            }
            return response.json();
        })
        .then(user => {
            // знайти форму всередині модалки
            const form = document.querySelector('#editModal form');
            if (form) {
                document.getElementById('editUserTitle').textContent  = `User id: ${userId}`;
                document.getElementById('edit').textContent = 'Edit user:';
                form.querySelector('input[name="id"]').value = userId;
                form.querySelector('input[name="firstname"]').value = user.firstname;
                form.querySelector('input[name="lastname"]').value = user.lastname;
                form.querySelector('input[name="age"]').value = user.age;
                form.querySelector('input[name="email"]').value = user.email;
                form.querySelector('input[name="login"]').value = user.login;
                form.querySelector('input[name="password"]').value = user.password;
                form.querySelector('input[name="phone"]').value = user.phone;
            }
            openEditModal();
        })
        .catch(error => alert(error));//console.error("Error fetching user:", error));
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