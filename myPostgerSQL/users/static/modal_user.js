var modal = document.getElementById("myModal");
var form = document.querySelector(".formUser");
var formTitle = document.getElementById("userModalTitle");
var userIdField = document.getElementById("userIdField");

// Функція для відкриття модального вікна
function openModal(userId) {
    form.reset();
  if (userId) { // режим редагування користувача
    formTitle.textContent = `Редагування користувача з id ${userId}`;
    getDataUser(userId);
    }
  else {
    console.log('New user')
    formTitle.textContent = "Додати нового користувача";
    form.action = `new_user/`;
    userIdField.value = '';
    }

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
      console.log('autoFill')
    if (form) {
        const fakeData = {
            firstname: faker.person.firstName(),
            lastname: faker.person.lastName(),
            age: faker.number.int({ min: 18, max: 90 }),
            email: faker.internet.email(),
            phone: faker.phone.number('+380 (##) ###-##-##'),
        };

        form.querySelector('input[name="firstname"]').value = fakeData.firstname;
        form.querySelector('input[name="lastname"]').value = fakeData.lastname;
        form.querySelector('input[name="age"]').value = fakeData.age;
        form.querySelector('input[name="email"]').value = fakeData.email;
        form.querySelector('input[name="login"]').value = fakeData.firstname;
        form.querySelector('input[name="password"]').value = fakeData.lastname;
        form.querySelector('input[name="phone"]').value = fakeData.phone;
    }
}

function delUser(userId) {
    if (!confirm(`Видалити користувача з id '${userId}' ?`)) {
        return;
    }

    fetch(`delete_user/${userId}/`, {
        method: "DELETE",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "X-Requested-With": "XMLHttpRequest"
        }
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            alert(`Користувача з email ${result.email} було видалено.`);
            // опційно: видаляємо рядок із таблиці
            const tr_id = `row-${userId}`
            const row = document.querySelector(`tr[id="${tr_id}"]`);
            if (row) {
              row.remove();
              console.log(`Видалено рядок з id ${tr_id}`)
            }
            else console.log(`Не знайдено рядок p id ${tr_id}`)
        } else {
            alert(`Помилка: ${result.error}`);
        }
    })
    .catch(error => console.error("Помилка fetching user:", error));
}


// функція для отримання CSRF токена з cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// Функції модального вікна для редагування даних користувача

function getDataUser(userId) {
    console.log('Edit');

    fetch(`get_user/${userId}/`)
        .then(response => {
            // Перевіряємо, чи був запит успішним
            if (!response.ok) {
                // Якщо відповідь не 200 OK, викидаємо помилку
                // Щоб отримати більш детальні дані про помилку, парсимо відповідь
                return response.json().
                    then(errorData => {
                        throw new Error(errorData.error || "Невідома помилка мережі");
                });
            }
            return response.json();
        })
        .then(data => {
            if (data.success && data.user) {
                const user = data.user;
                formTitle.textContent = "Редагування користувача";
                userIdField.value = userId;
                form.action = `/edit_user/${userId}`;

                form.querySelector('#userIdField').value = user.id;
                form.querySelector('input[name="firstname"]').value = user.firstname;
                form.querySelector('input[name="lastname"]').value = user.lastname;
                form.querySelector('input[name="age"]').value = user.age;
                form.querySelector('input[name="email"]').value = user.email;
                form.querySelector('input[name="login"]').value = user.login;
                form.querySelector('input[name="password"]').value = user.password;
                form.querySelector('input[name="phone"]').value = user.phone;
            } else {
                alert(`Помилка: ${data.error}`);
            }
        })
        .catch(error => alert(`Помилка fetching user, ${error}.`));
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

//function openEditModal() {
//  editModal.style.display = "block";
//}
//
//function closeEditModal() {
//  editModal.style.display = "none";
//}
