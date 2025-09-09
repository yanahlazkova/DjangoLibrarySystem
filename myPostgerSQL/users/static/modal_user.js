var modal = document.getElementById("myModal");
var form = document.querySelector(".formUser");
var formEdit = document.querySelector(".formEditUser");
var formTitle = document.getElementById("userModalTitle");
var userIdField = document.querySelector('input[name="user_id"]');
var submitButton = document.querySelector('input[name="submit"]');

// Функція для відкриття модального вікна
function openModal(userId) {
    form.reset();
    formEdit.reset();
  if (userId) { // режим редагування користувача
    formTitle.textContent = `Редагування користувача з id ${userId}`;
    formEdit.action = `edit_user/${userId}/`;
    submitButton.value = "Save";
    getDataUser(userId);
    form.style.display = "none";
    formEdit.style.display = "block";
    }
  else {
    console.log('New user')
    formTitle.textContent = "Додати нового користувача";
    form.action = `new_user/`;
    userIdField.value = '';
    submitButton.value = "Додати нового";
    formEdit.style.display = "none";
    form.style.display = "block";
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
//                formTitle.textContent = "Редагування користувача";
                userIdField.value = userId;
//                form.action = `edit_user/${userId}/`;
                formEdit.querySelector('input[name="id"]').value = user.id;
                formEdit.querySelector('input[name="firstname"]').value = user.firstname;
                formEdit.querySelector('input[name="lastname"]').value = user.lastname;
                formEdit.querySelector('input[name="age"]').value = user.age;
                formEdit.querySelector('input[name="email"]').value = user.email;
                formEdit.querySelector('input[name="login"]').value = user.login;
                formEdit.querySelector('input[name="password"]').value = user.password;
                formEdit.querySelector('input[name="phone"]').value = user.phone;
                formEdit.querySelector('input[type="submit"]').value = 'Save';
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
